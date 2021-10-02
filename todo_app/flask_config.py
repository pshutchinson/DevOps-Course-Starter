import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
class Config:
    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.TRELLO_KEY= os.environ.get('TRELLO_KEY')
        self.TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
        self.TRELLO_BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
        self.MONGO_CLUSTER = os.environ.get('MONGO_CLUSTER')
        self.MONGO_DB = os.environ.get('MONGO_DB')
        self.MONGO_USER = os.environ.get('MONGO_USER')
        self.MONGO_PWD = os.environ.get('MONGO_PWD')
    