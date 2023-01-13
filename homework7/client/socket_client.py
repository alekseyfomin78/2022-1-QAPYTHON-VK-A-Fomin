import json
import logging
import socket

log = logging.getLogger('client')


class ResponseStatusCodeException(Exception):
    pass


class MockClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.client = None

    def connect(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        client.connect((self.host, self.port))
        self.client = client

    def _request(self, req_type: str, location: str, host: str, data: json = None, expected_status: int = 200):
        self.connect()
        request = f'{req_type} {location} HTTP/1.1\r\nHOST:{host}\r\n'
        if data is not None:
            request += f'Content-Type: application/json\r\nContent-Length:{str(len(data))}\r\n\r\n{data}'
        else:
            request += '\r\n'

        self.client.send(request.encode())
        response = self.client_recv()
        status_code = int(response[0].split()[1])
        if status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {status_code} for URL "{location}"!\n'
                                              f'Expected status code: {expected_status}.')
        log.info(request)
        log.info(response)
        return response

    def create_user_surname(self, name: str, surname: str, expected_status: int):
        location = f'/create_surname/'
        data = json.dumps({'name': name, 'surname': surname})
        response = self._request(req_type='POST', location=location, host=self.host, data=data,
                                 expected_status=expected_status)
        return response

    def get_user_surname(self, name: str, expected_status: int):
        location = f'/get_surname/{name}/'
        response = self._request(req_type='GET', location=location, host=self.host, expected_status=expected_status)
        return json.loads(response[-1])

    def put_update_user_surname(self, name: str, surname: str, expected_status: int):
        location = f'/update_surname/{name}/'
        data = json.dumps({'surname': surname})
        response = self._request(req_type='PUT', location=location, host=self.host, data=data,
                                 expected_status=expected_status)
        new_surname = json.loads(response[-1])
        return new_surname

    def delete_user_surname(self, name: str, expected_status: int):
        location = f'/delete_surname/{name}/'
        self._request(req_type='DELETE', location=location, host=self.host, expected_status=expected_status)

    def client_recv(self):
        total_data = []
        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                self.client.close()
                break
        data = ''.join(total_data).splitlines()
        return data

    def close(self):
        self.client.close()
