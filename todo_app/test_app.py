import pytest
from todo_app import app
from todo_app.todoItem import ToDoItem
from dotenv import find_dotenv, load_dotenv
from unittest.mock import patch, Mock
from pymongo import MongoClient


TEST_MONGO_CLUSTER='cluster0.duj0p.mongodb.net'
TEST_MONGO_DB='Board'
TEST_MONGO_USER='user'
TEST_MONGO_PWD='pwd'

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')

    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    
    with test_app.test_client() as client:
        return client

def populateItems():
    item = ToDoItem('id', 'name', 'desc', 'start', 'due', 'last modified')
    items = []
    items.append(item)
    return items

@patch('todo_app.services.mongo.get_items')
def test_client_view(mock_get_items, client):
    mock_get_items.side_effect = populateItems
    response = client.get('/')