from code.mysql.models.models import Model


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def add_user(self, name, surname, username, email, password, middle_name, access = 1, active = 0):
        user = Model(
            name=name,
            surname=surname,
            username=username,
            email=email,
            password=password,
            middle_name=middle_name,
            access = access,
            active = active
        )
        self.client.session.add(user)
        self.client.session.commit()