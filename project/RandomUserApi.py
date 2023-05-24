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
	
	def get_data(self):
		response = None
		retry_count_int = int(self.retry_count)
		retry_sleep_int = int(self.retry_sleep)
		for attempt in range(retry_count_int):
			try:
				logging.info(f"Attempting to contact: {self.root_uri}")
				response = requests.get(self.root_uri)
				if response.status_code == 404:
					logging.error(f"attempted contacting {self.root_uri}")
					logging.error(f"got response: {response.text}")
					return None
				else:
					response.raise_for_status()
			except requests.exceptions.Timeout as e:
				sleep(retry_sleep_int)
			except requests.exceptions.HTTPError as e:
				if response:
					logging.error(f"got response: {response.text}")
				raise self.RandomUserException(e)
			except requests.exceptions.RequestException as e:
				if response:
					logging.error(f"got response: {response.text}")
				raise self.RandomUserException(e)
			else:
				logging.info("Valid response received!")
				return response.json()
		else:
			logging.error(f"{self.root_uri}, returned an unexpected response!")
			raise self.RandomUserException()
	
	def get_status(self):
		response = requests.get(self.root_uri)
		if response.status_code >= 400:
			logging.error("Error response")
			return None
		else:
			return response.status_code
			