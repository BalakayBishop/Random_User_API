# project/core/views.py
from flask import render_template, Blueprint, request, jsonify, send_file
from sqlalchemy.orm import sessionmaker
from project.config import engine
import os

Session = sessionmaker(bind=engine)
session = Session()

core = Blueprint('core', __name__)


# ---------- ROUTE: INDEX ----------
@core.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')
