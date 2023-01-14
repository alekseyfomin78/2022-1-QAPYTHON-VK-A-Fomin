import pytest
from mysql.builder import MySQLBuilder


class BaseMySQL:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client = mysql_client
        self.builder = MySQLBuilder(self.client)
        self.prepare()

    def get_all_from_table(self, model, **filters):
        self.client.session.commit()
        res = self.client.session.query(model).filter_by(**filters)
        return res.all()
