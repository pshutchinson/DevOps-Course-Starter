import os


class Config:
    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")

    TRELLO_KEY= os.environ.get('TRELLO_KEY')
    TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
    TRELLO_BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
    