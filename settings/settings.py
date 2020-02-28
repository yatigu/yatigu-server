import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import create_engine
import sys


# define
HOST_ADDR = '127.0.0.1'  # localhost 주소
PORT_NUM = '8000'  # 서버 포트
DEBUG = False  # 디버그모드
CHROME_DRIVER_PATH = ''
MODE = os.environ.get('MODE')

# connect db
USER = 'yatigu'  # username
PASSWOLRD = 'yatigu'  # postgresql pw
PORT = '5432'  # postgresql port
NAME = 'yatigu'  # db name
POSTGRESQL = f'postgresql://{USER}:{PASSWOLRD}@{HOST_ADDR}:{PORT}/{NAME}'  # postgresql uri
engine = create_engine(POSTGRESQL, connect_args={'connect_timeout': 10})

# app settings
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL  # db connect
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.threaded = True

# select operation mode
if MODE == 'TEST' or sys.argv[0].endswith('test'):  # use only pytest
    HOST_ADDR = '127.0.0.1'
    DEBUG = False
elif MODE == 'DEV':  # mode - development
    CHROME_DRIVER_PATH = 'C:\chromedriver.exe'
    HOST_ADDR = '127.0.0.1'
    DEBUG = True
elif MODE == 'RUN':  # mode - release
    CHROME_DRIVER_PATH = '/home/chromedriver'
    HOST_ADDR = '0.0.0.0'
    DEBUG = False
else:  # select not permission mode
    raise Exception('MODE error')


# manager
app.debug = DEBUG  # 실행 모드에 따라 디버그 온오프

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host=HOST_ADDR, port=PORT_NUM))


# connect models
from .models import *


# connect urls
from .urls import *
