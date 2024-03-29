import pytest
import faker

fake = faker.Faker()


class BaseApi:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

        if self.authorize:
            self.api_client.post_login()

    def random_info(self, max_length):
        return fake.lexify(text='?' * max_length)

    def upload_image(self, file):
        response_json = self.api_client.post_upload_image(file=file)
        return response_json['id']

    def get_url_id(self, url):
        response_json = self.api_client.get_id_url(url=url)
        return response_json['id']

    def create_campaign(self, name, image_id, url_id):
        response_json = self.api_client.post_create_campaign(name=name, image_id=image_id, url_id=url_id)
        return response_json['id']

    def get_campaign_status(self, campaign_id):
        response_json = self.api_client.get_campaign_status(campaign_id=campaign_id)
        return response_json['issues'][0]['code']

    def delete_campaign(self, campaign_id):
        self.api_client.delete_campaign(campaign_id=campaign_id)
        assert self.get_campaign_status(campaign_id=campaign_id) == 'ARCHIVED'

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
