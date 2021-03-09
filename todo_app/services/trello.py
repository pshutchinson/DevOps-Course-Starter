import requests

from flask import current_app as app

from todo_app.todoItem import ToDoItem

board_url = "https://api.trello.com/1/boards/{id}"

headers = {
   "Accept": "application/json"
}

def get_trello_creds():
    return { 'key': app.config['TRELLO_KEY'], 'token': app.config['TRELLO_TOKEN'] }

def get_list_params():
    return { 'key': app.config['TRELLO_KEY'], 'token': app.config['TRELLO_TOKEN'], 'cards': 'open' }

def add_card_params(title, item_list):
    return { 'key': app.config['TRELLO_KEY'], 'token': app.config['TRELLO_TOKEN'], 'name': title, 'idList': item_list['id'] }

def update_card_params(item_list):
    return { 'key': app.config['TRELLO_KEY'], 'token': app.config['TRELLO_TOKEN'], 'idList': item_list['id'] }

def get_url(endpoint):
    return "https://api.trello.com/1/" + endpoint

def get_boards():
    
    params = get_trello_creds()
    url = get_url('members/me/boards')

    response = requests.get(url, params)
    
    return response.json()

def get_lists():

    get_boards()
    
    params = get_list_params()
    url = get_url('boards/%s/lists' % app.config['TRELLO_BOARD_ID'])
    
    response = requests.get(url, params)

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

def update_item(id, list_name):
    move_to_list = get_named_list(list_name)
    updated_card = move_card(id, move_to_list)
    ToDoItem.convertFromTrello(updated_card, move_to_list)

def move_card(card_id, list):
    params = update_card_params(list)
    url = get_url('cards/%s' % card_id)
    response = requests.put(url, params = params)
    card = response.json()
    return card