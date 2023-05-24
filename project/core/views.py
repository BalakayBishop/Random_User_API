# project/core/views.py
import logging
import os
import sys

from flask import render_template, Blueprint
from sqlalchemy.orm import sessionmaker
from pprint import pprint

from project.RandomUserApi import RandomUserApi
from project.config import engine

Session = sessionmaker(bind=engine)
session = Session()

core = Blueprint('core', __name__)

logging.basicConfig(format='%(levelname)s:%(asctime)s:  %(message)s', datefmt="%Y-%m-%d %H:%M", level=logging.INFO)
ROOTDIR = os.path.dirname(os.path.abspath(sys.argv[0]))


def get_json():
	api_obj = RandomUserApi(
		root_uri=os.getenv('ROOT_URI'),
		retry_count=os.getenv('RETRY_COUNT'),
		retry_sleep=os.getenv('RETRY_SLEEP')
	)
	
	try:
		response = api_obj.get_status()
		if response == 200:
			random_user_json_data = api_obj.get_data()
			return random_user_json_data
		else:
			return None
	except RandomUserApi.RandomUserException as e:
		logging.error(f'Exception caught from getting json: {e}')


# ---------- ROUTE: INDEX ----------
@core.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@core.route('/get_user_data', methods=['GET'])
def get_user_data():
	response = get_json()
	return response
