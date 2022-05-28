from dataclasses import dataclass

import faker

fake = faker.Faker()


@dataclass
class User:
    name: str = None
    surname: str = None


class Builder:

    @staticmethod
    def create_user():
        fake_user = fake.name().split()
        name = fake_user[0]
        surname = fake_user[1]
        return User(name=name, surname=surname)
