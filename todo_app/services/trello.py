import os
import requests

from flask import current_app as app

from todo_app.todoItem import ToDoItem

from datetime import datetime

#board_url = "https://api.trello.com/1/boards/{id}"

headers = {
   "Accept": "application/json"
}

def get_trello_creds():
    return { 'key': app.config['TRELLO_KEY'], 'token': app.config['TRELLO_TOKEN'] }

def create_board_creds(name):
    return { 'key': app.config['TRELLO_KEY'], 'token': app.config['TRELLO_TOKEN'], 'name': name }

def get_list_params():
    return { 'key': app.config['TRELLO_KEY'], 'token': app.config['TRELLO_TOKEN'], 'cards': 'open' }

def add_card_params(title, item_list):
    return { 'key': app.config['TRELLO_KEY'], 'token': app.config['TRELLO_TOKEN'], 'name': title, 'idList': item_list['id'] }

#def update_card_params(start, due, item_list):
#    return { 'key': app.config['TRELLO_KEY'], 'token': app.config['TRELLO_TOKEN'], 'start': start, 'due': due, 'idList': item_list['id'] }

def update_card_params(item_list):
    return { 'key': app.config['TRELLO_KEY'], 'token': app.config['TRELLO_TOKEN'], 'idList': item_list['id'] }

def get_url(endpoint):
    return "https://api.trello.com/1/" + endpoint

def create_board(name):

    print("In create_board")
    params = create_board_creds(name)
    print(params)
    url = get_url('boards')

    response = requests.post(url, params)

    response.raise_for_status()
    
    return response.json()

def delete_board(id):
    
    params = get_trello_creds()
    url = get_url('boards/%s' % id)

    response = requests.delete(url, params=params)

    response.raise_for_status()
    
    return response.json()

def get_boards():
    
    params = get_trello_creds()
    url = get_url('members/me/boards')

    response = requests.get(url, params)
    
    response.raise_for_status()

    return response.json()

def get_lists():

    get_boards()
    
    params = get_list_params()
    #url = get_url('boards/%s/lists' % app.config['TRELLO_BOARD_ID'])
    url = get_url('boards/%s/lists' % os.environ['TRELLO_BOARD_ID'])
    
    response = requests.get(url, params)

    response.raise_for_status()

    return response.json()

def get_named_list(list_name):

    lists = get_lists()
    
    for list_item in lists:
        if (list_item['name'] == list_name):
            return list_item
    
    return None

def get_items():

    lists = get_lists()

    items = []
    for card_list in lists:
        for card in card_list['cards']:
            items.append(ToDoItem.convertFromTrello(card, card_list))

    return items

def add_item(title):

    item_list = get_named_list('To Do')
    if (item_list != None):
        params = add_card_params(title, item_list)
        url = get_url('cards')
        response = requests.post(url, params = params)
        card = response.json()
        return ToDoItem.convertFromTrello(card, item_list)

    return None

def update_item(id, list_name, start, due):
    move_to_list = get_named_list(list_name)
    updated_card = move_card(id, move_to_list, start, due)
    return ToDoItem.convertFromTrello(updated_card, move_to_list)

def start_item(id):
    update_item(id, 'Doing', datetime.utcnow(), datetime.utcnow())

def complete_item(id):
    update_item(id, 'Done', datetime.utcnow(), datetime.utcnow())

def reset_item(id):
    update_item(id, 'To Do', None, None)

def move_card(card_id, list, start, due):
    #params = update_card_params(list, start, due)
    params = update_card_params(list)
    url = get_url('cards/%s' % card_id)
    response = requests.put(url, params = params)
    card = response.json()
    return card

def filter_todo(item):
	return item.status == 'To Do'

def filter_doing(item):
	return item.status == 'Doing'

def filter_done(item):
	return item.status == 'Done'