from server.mock_server import SURNAME_DATA
from base import BaseTest


class Test(BaseTest):
    def test_post(self):
        SURNAME_DATA[self.user.name] = self.user.surname
        surname = self.get_surname(self.user.name, 200)
        assert self.user.surname == surname

    def test_get(self):
        surname = self.get_surname(self.user.name, 404)
        assert f'Surname for user {self.user.name} not found' == surname
