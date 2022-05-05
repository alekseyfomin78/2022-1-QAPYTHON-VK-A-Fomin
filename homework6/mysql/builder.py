from mysql.models import *


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_count_requests(self, count):
        req_count = CountRequests(count=count)
        self.client.session.add(req_count)
        self.client.session.commit()
        return req_count

    def create_count_requests_by_type(self, req_type, count):
        req_types = CountRequestsByType(req_type=req_type, count=count)
        self.client.session.add(req_types)
        self.client.session.commit()
        return req_types

    def create_most_frequent_request(self, url, count):
        most_freq_req = MostFrequentRequest(url=url, count=count)
        self.client.session.add(most_freq_req)
        self.client.session.commit()
        return most_freq_req

    def create_largest_requests_with_4xx(self, url, size, ip):
        largest_reqs_4xx = LargestRequestsWith4xx(url=url, size=size, ip=ip)
        self.client.session.add(largest_reqs_4xx)
        self.client.session.commit()
        return largest_reqs_4xx

    def create_users_with_5xx_requests(self, ip, requests_number):
        user_with_5xx_reqs = UserWith5xxRequests(ip=ip, requests_number=requests_number)
        self.client.session.add(user_with_5xx_reqs)
        self.client.session.commit()
        return user_with_5xx_reqs
