import os

import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
import pdb
from code.mysql.models.models import Base, Model
from code.utils.userbuilder import User


class MysqlClient:

    def __init__(self, db_name):
        self.user = os.environ['MYSQL_USER']
        self.port = os.environ['MYSQL_PORT']
        self.password = os.environ['MYSQL_PASSWORD']
        self.host = os.environ['MYSQL_HOST']
        self.db_name = db_name

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_created=True):

        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()
        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def create_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database IF EXISTS {self.db_name}')
        self.execute_query(f'CREATE database {self.db_name}')
        self.connection.close()

    def create_table(self, table_name):
        if not inspect(self.engine).has_table(table_name):
            Base.metadata.tables[table_name].create(self.engine)
            self.execute_query(
                f"INSERT INTO {table_name}(name, surname, middle_name, username, password, email, access, active, start_active_time)"
                f"VALUES ('admin', 'admin', 'admin', 'Adminadmin', 'Adminadmin', 'admin@mail.ru', NULL ,NULL, NULL)")

    def get_users(self, **filters):
        self.session.commit()
        res = self.session.query(Model).filter_by(**filters)
        return res.all()

    def get_users_by_username(self, username):
        return self.get_users(**{"username": username})

    def get_current_user(self):
        return self.get_users(**{"active": 1})

    def user_was_created_with_right_data(self, username, userB : User):
        user = self.get_users_by_username(username)[0]
        return user.name == userB.name and user.surname == userB.surname \
               and user.middle_name == userB.Midddleename \
               and user.username == userB.username and user.email == userB.email \
               and user.password == userB.password

