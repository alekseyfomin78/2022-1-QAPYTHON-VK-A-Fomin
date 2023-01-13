import pytest

from base import Base


class TestMock(Base):
    def test_post_user(self):
        self.post_create_user_surname(self.user.name, self.user.surname, expected_status=201)

    def test_post_existent_user(self):
        self.post_create_user_surname(self.user.name, self.user.surname, expected_status=201)
        self.post_create_user_surname(self.user.name, self.user.surname, expected_status=400)

    def test_get_user(self):
        self.post_create_user_surname(self.user.name, self.user.surname, expected_status=201)
        surname = self.get_user_surname(self.user.name, expected_status=200)

        assert surname == self.user.surname

    def test_get_not_user(self):
        self.get_user_surname(self.user.name, expected_status=404)

    def test_put_user(self):
        self.post_create_user_surname(self.user.name, self.user.surname, expected_status=201)
        user = self.put_update_user_surname(self.user.name, 'Ivanov', expected_status=201)

        assert user[self.user.name] == 'Ivanov'

    def test_put_not_user(self):
        self.post_create_user_surname(self.user.name, self.user.surname, expected_status=201)
        resp = self.put_update_user_surname('Ivan', 'Ivanov', expected_status=400)

        assert resp == f'User Ivan and his surname Ivanov are not exists'

    def test_delete_user(self):
        self.post_create_user_surname(self.user.name, self.user.surname, expected_status=201)
        self.delete_user_surname(self.user.name, expected_status=204)
        self.get_user_surname(self.user.name, 404)

    def test_delete_not_user(self):
        self.delete_user_surname(self.user.name, expected_status=400)
