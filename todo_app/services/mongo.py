import os

import pymongo
from pymongo import MongoClient
from bson import ObjectId

from flask import current_app as app

from todo_app.todoItem import ToDoItem

from datetime import datetime

def get_connection():
    connection_string = 'mongodb+srv://' + os.environ['MONGO_USER'] + ':' + os.environ['MONGO_PASSWORD'] + '@' + os.environ['MONGO_CLUSTER'] + '/' + os.environ['MONGO_DB']
    client = MongoClient(connection_string)       
    return client

def create_board(name):
    return get_connection()[name]

def get_board():
    dbs = get_connection().list_database_names()

    if os.environ['MONGO_DB'] in dbs:
        return get_connection()[os.environ['MONGO_DB']]
    else:
        return create_board(os.environ['MONGO_DB'])

def get_list():
    board = get_board()
    return board['List']

def get_named_list(list_name):
    lists = get_list()
    
    for list_item in lists:
        if (list_item['name'] == list_name):
            return list_item
    
    return None

def get_items():
    boardlist = get_list()
    board_list_items = boardlist.find()

    items = []
    for card in board_list_items:
        items.append(ToDoItem.convertFromMongo(card))

    return items

def add_item(title):
    boardlist = get_list()
    
    #from dateutil import parser
    #expiry_date = '2021-07-13T00:00:00.000Z'
    #expiry = parser.parse(expiry_date)
    item = {
        "name" : title,
        "desc" : title,
        "start" : datetime.utcnow(),
        "due" : datetime.utcnow(),
        "dateLastActivity" : datetime.utcnow(),
        "boardList" : "To Do"
    }
    insert_id = boardlist.insert_one(item)

def update_item(id, list_name, start, due):
    boardlist = get_list()
    boardlist.find_one_and_update({'_id' : ObjectId(id)},
    {
        "$set": {"boardList": list_name}#,
        #"$set": {"start": start},
        #"$set": {"due": due},
        #"$set": {"dateLastActivity": datetime.utcnow()}
    })

def start_item(id):
    update_item(id, 'Doing', datetime.utcnow(), datetime.utcnow())

def complete_item(id):
    update_item(id, 'Done', datetime.utcnow(), datetime.utcnow())

def reset_item(id):
    update_item(id, 'To Do', None, None)

def filter_todo(item):
	return item.status == 'To Do'

def filter_doing(item):
	return item.status == 'Doing'

def filter_done(item):
	return item.status == 'Done'