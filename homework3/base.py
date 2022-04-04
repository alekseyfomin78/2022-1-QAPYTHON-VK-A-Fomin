import string

import random
import pytest


class BaseApi:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

        if self.authorize:
            self.api_client.post_login()

    def random_info(self, max_length):
        return ''.join(random.choice(string.ascii_letters + string.digits + ' ') for _ in range(
            random.randint(1, max_length)))

    def upload_image(self, file):
        response_json = self.api_client.post_upload_image(file=file)
        return response_json['id']

    def get_url_id(self, target_url):
        response_json = self.api_client.get_id_url(target_url=target_url)
        return response_json['id']

    def create_campaign(self, name, image_id, url_id):
        response_json = self.api_client.post_create_campaign(name=name, image_id=image_id, url_id=url_id)
        return response_json['id']

    def check_campaign_status(self, campaign_id, status):
        response_json = self.api_client.get_campaign_status(campaign_id=campaign_id)
        assert response_json['issues'][0]['code'] == status

    def delete_campaign(self, campaign_id):
        self.api_client.delete_campaign(campaign_id=campaign_id)
        self.check_campaign_status(campaign_id=campaign_id, status='ARCHIVED')

    @pytest.fixture()
    def campaign(self, file_path):
        name = self.random_info(10)
        url_id = self.get_url_id('https://www.google.com/')
        image_id = self.upload_image(file_path)

        campaign_id = self.create_campaign(name=name, image_id=image_id, url_id=url_id)

        yield campaign_id

        self.delete_campaign(campaign_id=campaign_id)

    def create_segment(self, name):
        response_json = self.api_client.post_create_segment(name=name)
        return response_json['id']

    def check_segment(self, segment_id):
        # проверка того, что при переходе на страницу сегмента в _request получен статус 200
        assert self.api_client.get_check_segment(segment_id=segment_id)

    def delete_segment(self, segment_id):
        self.api_client.delete_segment(segment_id=segment_id)

