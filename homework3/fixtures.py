import os

import pytest


@pytest.fixture(scope='session')
def credentials():
    with open('files/credentials.txt', 'r') as f:
        user = f.readline().strip()
        password = f.readline().strip()
    return user, password


@pytest.fixture()
def file_path(repo_root):
    return os.path.join(repo_root, 'files', 'image.png')
