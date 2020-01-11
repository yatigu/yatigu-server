import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


# define
HOST_ADDR = '127.0.0.1'  # localhost 주소
PORT_NUM = '8000'  # 서버 포트
DEBUG = False  # 디버그모드


# connect db
USER = 'yatigu'  # username
PASSWOLRD = 'root'  # postgresql pw
PORT = '5432'  # postgresql port
NAME = 'yatigu'  # db name
POSTGRESQL = f'postgresql://{USER}:{PASSWOLRD}@{HOST_ADDR}:{PORT}/{NAME}'  # postgresql uri


# app settings
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL  # db connect
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# select operation mode
if os.environ.get('MODE') == 'DEV':  # mode - development
    HOST_ADDR = '127.0.0.1'
    DEBUG = True
elif os.environ.get('MODE') == 'RUN':  # mode - release
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
