import pytest

from base import BaseApi


class TestApi(BaseApi):
    @pytest.mark.API
    def test_campaign(self, campaign):
        campaign_id = campaign
        self.check_campaign_status(campaign_id=campaign_id, status="NO_ALLOWED_BANNERS")

    @pytest.mark.API
    def test_create_segment(self):
        name = self.random_info(10)
        created_segment_id = self.create_segment(name=name)
        self.check_segment(segment_id=created_segment_id)

    @pytest.mark.API
    def test_delete_segment(self):
        name = self.random_info(10)
        created_segment_id = self.create_segment(name=name)
        self.check_segment(segment_id=created_segment_id)
        self.delete_segment(segment_id=created_segment_id)
