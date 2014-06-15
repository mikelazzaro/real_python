# config.py

import os

# Grab the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__name__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = 'WexhB0vbW&ni^xzQQN0Qgfoqx%#KAOn7HAnpAVPm^yJ!S5G9d@'

# Defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
