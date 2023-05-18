# project/core/views.py
from flask import render_template, Blueprint, request, jsonify, send_file
from sqlalchemy.orm import sessionmaker
from project.config import engine
import os, sys, logging, datetime

Session = sessionmaker(bind=engine)
session = Session()

core = Blueprint('core', __name__)

logging.basicConfig(format='%(levelness)s:%(pastime)s:  %(message)s',datefmt="%Y-%m-%d %H:%M", level=logging.INFO)
TODAY = datetime.datetime.now()


# ---------- ROUTE: INDEX ----------
@core.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')
