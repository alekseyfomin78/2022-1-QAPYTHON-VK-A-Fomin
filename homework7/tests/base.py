import pytest
from utils.builder import Builder


class Base:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, client_fixture, logger):
        self.client = client_fixture
        self.logger = logger
        self.user = Builder.create_user()

    def post_create_user_surname(self, name: str, surname: str, expected_status: int):
        return self.client.create_user_surname(name, surname, expected_status)

    def get_user_surname(self, name: str, expected_status: int):
        return self.client.get_user_surname(name, expected_status)

    def put_update_user_surname(self, name: str, surname: str, expected_status: int):
        return self.client.put_update_user_surname(name, surname, expected_status)

    def delete_user_surname(self, name: str, expected_status):
        self.client.delete_user_surname(name, expected_status)
