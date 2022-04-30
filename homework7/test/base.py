import pytest

from utils.builder import Builder


class BaseTest:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mock_client):
        self.mock_client = mock_client
        self.user = Builder.create_user()

    def get_surname(self, name, expected_status):
        return self.mock_client.get_surname(name, expected_status)
