from dataclasses import dataclass

import faker

fake = faker.Faker()


@dataclass
class User:
    name: str = None
    surname: str = None
    Midddleename: str = None
    username: str = None
    email: str = None
    password: str = None


class UserBuilder:
    users = []

    @staticmethod
    def create_user(name=None, surname=None, Midddleename=None,
                    username=None, email=None, password=None, length_name = 10, \
                    length_surname = 10, length_middleename = 10, length_username = 10, \
                    length_email = 15, length_password = 10):

        if name is None:
            name = fake.password(length = length_name, special_chars=False, digits=True)

        if surname is None:
            surname = fake.password(length = length_surname, special_chars=False, digits=True)

        if Midddleename is None:
            Midddleename = fake.password(length = length_middleename, special_chars=False, digits=True)

        if username is None:
            username = fake.password(length = length_username, special_chars=False, digits=True)

        if email is None:
            email = fake.password(length = length_email - 4, special_chars=False, digits=True) + "@m.r"

        if password is None:
            password = fake.password(length = length_password, special_chars=False, digits=True)

        user = User(name=name, surname=surname, Midddleename=Midddleename, username=username,
                    email=email, password=password)

        return user

