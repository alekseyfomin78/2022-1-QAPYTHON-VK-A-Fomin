from server.mock_server import SURNAME_DATA
from base import BaseTest


class Test(BaseTest):
    def test_post(self):
        SURNAME_DATA[self.user.name] = self.user.surname
        surname = self.get_user_surname(self.user.name, 200)
        assert self.user.surname == surname

    def test_get(self):
        surname = self.get_user_surname(self.user.name, 404)
        assert f'Surname for user {self.user.name} not found' == surname

    def test_put(self):
        SURNAME_DATA[self.user.name] = self.user.surname
        self.user.surname = 'Fomin'
        self.put_update_user_surname(self.user.name, self.user.surname, 201)
        assert self.get_user_surname(self.user.name, 200) == self.user.surname

    def test_delete(self):
        SURNAME_DATA[self.user.name] = self.user.surname
        self.delete_user_surname(self.user.name, 204)
        surname = self.get_user_surname(self.user.name, 404)
        assert 'not found' in surname
