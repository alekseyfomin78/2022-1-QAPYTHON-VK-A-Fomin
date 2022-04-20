import pytest
from mysql import scripts
from mysql.builder import MySQLBuilder
from mysql.models import *


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


class TestCountRequests(BaseMySQL):

    def prepare(self):
        req_types = scripts.count_requests()
        self.builder.create_count_requests(req_types)
        self.count = 1

    def test_count_requests(self):
        req_types = self.get_all_from_table(CountRequests)
        assert len(req_types) == self.count


class TestCountRequestsByType(BaseMySQL):

    def prepare(self):
        req_types_count = scripts.count_requests_by_type()
        for req_type in req_types_count:
            self.builder.create_count_requests_by_type(req_type=req_type[0], count=req_type[1])
        self.count = len(req_types_count)

    def test_count_requests_by_type(self):
        req_types_count = self.get_all_from_table(CountRequestsByType)
        assert len(req_types_count) == self.count


class TestMostFrequentRequests(BaseMySQL):

    def prepare(self):
        most_freq_reqs = scripts.most_frequent_requests(top=10)
        for most_freq_req in most_freq_reqs:
            self.builder.create_most_frequent_request(url=most_freq_req[0], count=most_freq_req[1])
        self.count = len(most_freq_reqs)

    def test_most_frequent_requests(self):
        most_freq_reqs = self.get_all_from_table(MostFrequentRequest)
        assert len(most_freq_reqs) == self.count


class TestLargestRequestsWith4xx(BaseMySQL):

    def prepare(self):
        largest_reqs_4xx = scripts.largest_requests_with_4xx(top=5)
        for req in largest_reqs_4xx:
            self.builder.create_largest_requests_with_4xx(url=req[0], size=req[1], ip=req[2])
        self.count = len(largest_reqs_4xx)

    def test_largest_requests_with_4xx(self):
        largest_reqs_4xx = self.get_all_from_table(LargestRequestsWith4xx)
        assert len(largest_reqs_4xx) == self.count


class TestUsersWith5xxRequests(BaseMySQL):

    def prepare(self):
        users_with_5xx_reqs = scripts.users_with_5xx_requests(top=5)
        for user in users_with_5xx_reqs:
            self.builder.create_users_with_5xx_requests(ip=user[0], requests_number=user[1])
        self.count = len(users_with_5xx_reqs)

    def test_users_with_5xx_requests(self):
        users_with_5xx_reqs = self.get_all_from_table(UserWith5xxRequests)
        assert len(users_with_5xx_reqs) == self.count
