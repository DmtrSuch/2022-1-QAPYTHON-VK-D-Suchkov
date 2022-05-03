import pytest

from mysql.client import MysqlClient


@pytest.fixture(scope='session')
def mysql_client():
    my_sql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    my_sql_client.connect()
    yield my_sql_client
    my_sql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')

        mysql_client.recreate_db()

        mysql_client.connect()
        mysql_client.create_all_tables_from_base()
        mysql_client.connection.close()