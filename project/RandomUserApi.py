from time import sleep
import requests
import logging


class RandomUserApi:
	"""
	
	"""
	
	def __init__(self, **kwargs):
		self.root_uri = kwargs.get('root_uri')
		self.retry_count = kwargs.get('retry_count')
		self.retry_sleep = kwargs.get('retry_sleep')
	
	class RandomUserException(Exception):
		pass
	
	def _get(self, endpoint_uri):
		response = None
		for attempt in range(self.retry_count):
			try:
				response = requests.get(endpoint_uri)
				if response.status_code == 404:
					logging.error(f"attempted contacting {endpoint_uri}")
					logging.error(f"got response: {response.text}")
					return None
				else:
					response.raise_for_status()
			except requests.exceptions.Timeout as e:
				sleep(self.retry_sleep)
			except requests.exceptions.HTTPError as e:
				if response:
					logging.error(f"got response: {response.text}")
				raise self.RandomUserException(e)
			except requests.exceptions.RequestException as e:
				if response:
					logging.error(f"got response: {response.text}")
				raise self.RandomUserException(e)
			else:
				return response.json()
		else:
			logging.error(f"{endpoint_uri}, returned an unexpected response!")
			raise self.RandomUserException()
