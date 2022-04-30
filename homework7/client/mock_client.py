import json
import socket


class ResponseStatusCodeException(Exception):
    pass


class MockClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = None

    def connect(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        client.connect((self.host, self.port))
        self.client = client

    def _request(self, req_type, params, host, data=None, expected_status=200):
        self.connect()
        request = f'{req_type} {params} HTTP/1.1\r\nHOST:{host}\r\n'
        if data is not None:
            request += f'Content-Type: application/json\r\nContent-Length:{str(len(data))}\r\n\r\n{data}'
        else:
            request += '\r\n'

        self.client.send(request.encode())
        response = self.client_recv()
        status_code = int(response[0].split()[1])
        if status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {status_code} for URL "{params}"!\n'
                                              f'Expected status code: {expected_status}.')
        return response

    def get_surname(self, name, expected_status):
        params = f'/get_surname/{name}'
        response = self._request(req_type='GET', params=params, host=self.host, expected_status=expected_status)
        return json.loads(response[-1])

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
