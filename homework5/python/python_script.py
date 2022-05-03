import os
import json
import sys
from collections import Counter
from fnmatch import fnmatch
from pprint import pprint

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'access.log')


def count_requests():
    with open(LOG, 'r') as log:
        total_num_of_reqs = len(log.readlines())

    return {'Total number of requests': total_num_of_reqs}


def count_requests_by_type():
    with open(LOG, 'r') as log:
        req_type_column = []
        for req in log.readlines():
            req_type_column.append(req.split()[5][1:])

    req_types = Counter(req_type_column).most_common()

    num_of_reqs_by_type = {}
    for req in req_types:
        num_of_reqs_by_type[req[0]] = req[1]

    return num_of_reqs_by_type


def top_10_most_frequent_requests():
    with open(LOG, 'r') as log:
        url_column = []
        for req in log.readlines():
            url_column.append(req.split()[6])

    freq_reqs = Counter(url_column).most_common(10)

    most_freq_reqs = {}
    for i, req in zip(range(len(freq_reqs)), freq_reqs):
        most_freq_reqs[i + 1] = {'URL': req[0], 'Number_of_requests': req[1]}

    return most_freq_reqs


def top_5_largest_requests_with_4xx():
    with open(LOG, 'r') as log:
        url_status_size_ip_columns = []
        for req in log.readlines():
            if fnmatch(req.split()[8], '4??'):
                url_status_size_ip_columns.append((req.split()[6], int(req.split()[8]), int(req.split()[9]), req.split()[0]))
        url_status_size_ip_columns.sort(key=lambda column: column[2], reverse=True)

    top_5_url_status_size_ip_columns = url_status_size_ip_columns[:5]

    largest_reqs = {}
    for i, req in zip(range(len(top_5_url_status_size_ip_columns)), top_5_url_status_size_ip_columns):
        largest_reqs[i + 1] = {'URL': req[0], 'Status_code': req[1], 'Size': req[2], 'IP': req[3]}

    return largest_reqs


def top_5_users_with_5xx_requests():
    ip_with_5xx = []
    with open(LOG, 'r') as log:
        for req in log.readlines():
            if fnmatch(req.split()[8], '5??'):
                ip_with_5xx.append(req.split()[0])

    freq_ip = Counter(ip_with_5xx).most_common(5)

    users_with_5xx = {}
    for i, req in zip(range(len(freq_ip)), freq_ip):
        users_with_5xx[i + 1] = {'IP': req[0], 'Number_of_requests': req[1]}

    return users_with_5xx


results = {
    'Count requests': count_requests(),
    'Total number of requests by type': count_requests_by_type(),
    'Top 10 most frequent requests': top_10_most_frequent_requests(),
    'Top 5 largest requests with 4XX response codes': top_5_largest_requests_with_4xx(),
    'Top 5 users by the requests with 5XX response codes': top_5_users_with_5xx_requests(),
}


def write_results_to_json(result, folder, file_name):
    root = os.path.dirname(os.path.abspath(__file__))
    file_dir = os.path.join(root, folder, file_name)
    with open(file_dir, 'w') as f:
        json.dump(result, f, indent=4)


if '--json' in sys.argv:
    write_results_to_json(results, 'results', 'python_results.json')
else:
    pprint(results)
