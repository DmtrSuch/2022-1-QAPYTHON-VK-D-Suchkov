import pytest
import os
from faker import Faker
from test_api.base import ApiBase

fake = Faker()
COUNT = 10



class TestApi(ApiBase):
	@pytest.mark.API
	def test_create_segment(self):
		name = self.random_text(COUNT)
		created_id = self.create_segment(name=name, pass_condition=1, obj_type='remarketing_player')
		self.check_segment(segment_id=created_id, exp_status=200)
		return created_id

	@pytest.mark.API
	def test_delete_segment(self):
		created_id=self.test_create_segment()
		deleted_id = self.delete_segment(segment_id=created_id)
		self.check_segment(segment_id=deleted_id, exp_status=404)

	@pytest.mark.API
	def test_campaign(self, campaign):
		campaign_id = campaign
		self.check_campaign_status(campaign_id=campaign_id, status="NO_ALLOWED_BANNERS")
