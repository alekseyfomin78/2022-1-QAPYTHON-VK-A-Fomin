import logging
import os
import shutil
import signal
import subprocess
import sys
from copy import copy
import time

import pytest

import settings
import requests
from requests.exceptions import ConnectionError

from client.socket_client import MockClient
from mock_server import flask_mock_server


repo_root = os.path.abspath(os.path.join(__file__, os.pardir))
python_root = os.path.join(repo_root, '../venv/Scripts/python.exe') if sys.platform.startswith('win') else 'python3'


# функция ожидающая запуск сервера
def wait_ready(host: str, port: str):
    started = False
    st = time.time()
    while time.time() - st <= 15:
        try:
            requests.get(f'http://{host}:{port}')
            print('Ready')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError(f'{host}:{port} did not started in 15s!')


# use case 1
# конфиг запуска сервера на отдельном процессе
# def mock_config():
#     mock_path = os.path.join(repo_root, 'mock_server', 'flask_mock_server.py')
#
#     env = copy(os.environ)
#     env.update({
#         'MOCK_HOST': settings.MOCK_HOST,
#         'MOCK_PORT': settings.MOCK_PORT,
#     })
#
#     mock_stderr = open(os.path.join(repo_root, 'logs', 'mock_stderr.log'), 'w+')
#     mock_stdout = open(os.path.join(repo_root, 'logs', 'mock_stdout.log'), 'w+')
#
#     mock_proc = subprocess.Popen([python_root, mock_path], stderr=mock_stderr, stdout=mock_stdout, env=env)
#     wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)
#
#     return mock_proc, mock_stderr, mock_stdout

# use case 2
# запуск сервера на отдельном потоке
def start_mock():
    flask_mock_server.run_mock()
    wait_ready(host=settings.MOCK_HOST, port=settings.MOCK_PORT)


# use case 2
# завершение работы сервера
def stop_mock():
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

        # use case 1
        # config.mock_proc, config.mock_stderr, config.mock_stdout = mock_config()

        # use case 2
        start_mock()

    config.base_temp_dir = base_dir


# use case 1
# функция для завершения процесса, на котором работал сервер
# def stop_process(proc):
#     if sys.platform.startswith('win'):
#         proc.send_signal(signal.CTRL_BREAK_EVENT)
#     else:
#         proc.send_signal(signal.SIGINT)
#     exit_code = proc.wait()
#     assert exit_code == 0, f'Server exited abnormally with exit code: {exit_code}'


# use case 1
# def mock_unconfig(config):
#     stop_process(config.mock_proc)
#
#     config.mock_stderr.close()
#     config.mock_stdout.close()


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        # use case 1
        # mock_unconfig(config)

        # use case 2
        stop_mock()


@pytest.fixture(scope='function')
def client_fixture() -> MockClient:
    mock_client = MockClient(settings.MOCK_HOST, int(settings.MOCK_PORT))
    yield mock_client
    mock_client.close()


@pytest.fixture(scope='session')
def base_temp_dir():
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    return base_dir


@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_temp_dir, request._pyfuncitem.nodeid)
    if sys.platform.startswith('win'):
        test_dir = "".join((test_dir[:2], test_dir[2:].replace(':', "_")))
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='function')
def logger(temp_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'client.log')
    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('client')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()
