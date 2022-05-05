import pytest
from mysql.client import MySQLClient


def pytest_configure(config):
    mysql_client = MySQLClient(user='root', password='pass', db_name='TEST_SQL', host='127.0.0.1', port=3306)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()

    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_table(table_name='total_number_of_requests')
        mysql_client.create_table(table_name='total_number_of_requests_by_type')
        mysql_client.create_table(table_name='most_frequent_requests')
        mysql_client.create_table(table_name='largest_requests_with_4xx')
        mysql_client.create_table(table_name='users_with_5xx_requests')

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MySQLClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()
