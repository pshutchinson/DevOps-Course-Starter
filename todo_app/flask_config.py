import os
class Config:
    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.TRELLO_KEY= os.environ.get('TRELLO_KEY')
        self.TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
        self.TRELLO_BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
    