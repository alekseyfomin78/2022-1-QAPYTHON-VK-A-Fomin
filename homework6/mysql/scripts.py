import os
from collections import Counter
from fnmatch import fnmatch


LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'access.log')


def count_requests():
    with open(LOG, 'r') as log:
        total_num_of_reqs = len(log.readlines())

    return total_num_of_reqs


def count_requests_by_type():
    with open(LOG, 'r') as log:
        req_type_column = []
        for req in log.readlines():
            req_type_column.append(req.split()[5][1:])

    return Counter(req_type_column).most_common()


def most_frequent_requests(top: int):
    with open(LOG, 'r') as log:
        url_column = []
        for req in log.readlines():
            url_column.append(req.split()[6])

    return Counter(url_column).most_common(top)


def largest_requests_with_4xx(top: int):
    with open(LOG, 'r') as log:
        url_code_size_ip_columns = []
        for req in log.readlines():
            if fnmatch(req.split()[8], '4??'):
                url_code_size_ip_columns.append((req.split()[6], int(req.split()[8]), int(req.split()[9]), req.split()[0]))
        url_code_size_ip_columns.sort(key=lambda column: column[2], reverse=True)

    return url_code_size_ip_columns[:top]


def users_with_5xx_requests(top: int):
    ip_with_5xx = []
    with open(LOG, 'r') as log:
        for req in log.readlines():
            if fnmatch(req.split()[8], '5??'):
                ip_with_5xx.append(req.split()[0])

    return Counter(ip_with_5xx).most_common(top)
