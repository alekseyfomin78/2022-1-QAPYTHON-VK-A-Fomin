from urllib.parse import urljoin

import requests

from api.custom_exceptions import ResponseStatusCodeException


class ApiClient:

    def __init__(self, base_url, user, password):
        self.base_url = base_url
        self.user = user
        self.password = password
        self.csrf_token = None

        self.session = requests.Session()

    def _request(self, method, location, headers=None, data=None, expected_status=200, jsonify=False, params=None,
                 json=None, files=None):

        url = urljoin(self.base_url, location)

        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params, json=json,
                                        files=files)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"')

        if jsonify:
            return response.json()

        return response

    def get_csrf_token(self):
        location = '/csrf/'

        headers = self._request('GET', location=location).headers['set-cookie'].split(';')
        cookies = [c for c in headers if 'csrftoken' in c]
        csrf_token = cookies[0].split('=')[-1]

        return csrf_token

    def post_login(self):
        url = 'https://auth-ac.my.com/auth'

        headers = {
            "Referer": "https://account.my.com/",
        }

        data = {
            'email': self.user,
            'password': self.password,
            "continue": "https://account.my.com/login_continue/?continue=https%3A%2F%2Faccount.my.com%2Fprofile%2Fuserinfo%2F",
            "failure": "https://account.my.com/login/?continue=https%3A%2F%2Faccount.my.com%2Fprofile%2Fuserinfo%2F",
            "nosavelogin": "0",
        }

        response = self.session.post(url=url, headers=headers, data=data)
        self.csrf_token = self.get_csrf_token()
        return response

    def post_create_campaign(self, name, image_id, url_id):
        location = "/api/v2/campaigns.json"

        headers = {
            "X-CSRFToken": self.csrf_token
        }

        json = {
            "banners": [{"content": {"image_90x75": {"id": image_id}},
                         "textblocks": {"title_25": {"text": name}, "text_90": {"text": name}, "cta_sites_full": {
                             "text": "visitSite"}},
                         "urls": {"primary": {"id": url_id}}}],
            "name": name,
            "objective": "traffic",
            "package_id": 1029,
        }

        return self._request('POST', location=location, headers=headers, json=json, jsonify=True)

    def post_upload_image(self, file):
        location = "/api/v2/content/static.json"

        files = {
            'file': open(file, 'rb')
        }

        headers = {
            "X-CSRFToken": self.csrf_token
        }

        return self._request('POST', location=location, headers=headers, files=files, jsonify=True)

    def get_id_url(self, url):
        location = f"/api/v1/urls/?url={url}"

        return self._request('GET', location=location, jsonify=True)

    def get_campaign_status(self, campaign_id):
        location = f"/api/v2/campaigns/{campaign_id}.json?fields=issues"

        return self._request('GET', location=location, jsonify=True)

    def delete_campaign(self, campaign_id):
        location = f"api/v2/campaigns/{campaign_id}.json"

        headers = {
            "X-CSRFToken": self.csrf_token
        }

        return self._request('DELETE', location=location, headers=headers, expected_status=204)

    def post_create_segment(self, name):
        location = "/api/v2/remarketing/segments.json?fields=id,name"

        headers = {
            "X-CSRFToken": f'{self.csrf_token}'
        }

        json = {
            "name": name,
            "pass_condition": 1,
            "relations": [{
                "object_type": "remarketing_player",
                "params": {
                    "left": 365,
                    "right": 0,
                    "type": 'positive'
                }
            }]
        }

        return self._request('POST', location=location, headers=headers, json=json, jsonify=True)

    def get_check_segment_status_code(self, segment_id, expected_status):
        location = f"/api/v2/remarketing/segments/{segment_id}/relations.json"

        return self._request('GET', location=location, expected_status=expected_status)

    def delete_segment(self, segment_id):
        location = f'/api/v2/remarketing/segments/{segment_id}.json'

        headers = {
            "X-CSRFToken": self.csrf_token
        }

        return self._request('DELETE', location=location, headers=headers, expected_status=204)
