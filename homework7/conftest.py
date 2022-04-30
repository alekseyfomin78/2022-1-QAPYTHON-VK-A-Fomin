import pytest
import time
import settings
import requests
from requests.exceptions import ConnectionError
from server import mock_server
from client.mock_client import MockClient


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError(f'{host}:{port} did not started in 5s!')


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mock_server.run_mock()
        wait_ready(host=settings.MOCK_HOST, port=settings.MOCK_PORT)


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


@pytest.fixture(scope='function')
def mock_client():
    return MockClient(settings.MOCK_HOST, int(settings.MOCK_PORT))
