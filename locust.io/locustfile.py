from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from locust import HttpLocust, TaskSet, task
import io
import json
from requests_oauthlib import OAuth1


class YelpBehavior(TaskSet):
	def on_start(self):
		self.auth = OAuth1(creds['consumer_key'], creds['consumer_secret'], creds['token'], creds['token_secret'])

	@task
	def search_san_francisco(self):
		""" General search for San Francisco, CA """
		self.client.request(method='GET', url='/search/?location=San Francisco, CA', auth=self.auth)
		

	@task
	def business_san_francisco(self):
		""" Coffee shop in San Francisco, CA """
		self.client.request(method='GET', url='/business/coffeeshop-san-francisco', auth=self.auth)


	@task
	def phone_san_francisco(self):
		""" Pizza Hut in San Francisco, CA """
		self.client.request(method='GET', url='/phone_search/?phone=4159284300', auth=self.auth)

	@task
	def search_dc(self):
		""" Highest ranked mexican restaurants in DC """
		self.client.request(method='GET', url='/search/?location=Washington, D.C&sort=2&category_filter=mexican', auth=self.auth)

	@task
	def business_dc(self):
		""" Komi restaurant in Washington D.C. with more query parameters """
		self.client.request(method='GET', url='/business/komi-washington?lang_filter=true&actionlinks=true', auth=self.auth)


	@task
	def phone_dc(self):
		""" GMU admissions phone number """
		self.client.request(method='GET', url='/phone_search/?phone=(703) 993-1000', auth=self.auth)

class YelpUser(HttpLocust):
	task_set = YelpBehavior
	min_wait = 5000
	max_wait = 9000


def setup_creds():
	with io.open('config_secret.json') as cred:
		creds = json.load(cred)
		return creds


creds = setup_creds()
