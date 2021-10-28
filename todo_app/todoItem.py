from datetime import datetime

class ToDoItem:

    def __init__(self, id, name, description, start, due, last_modified, status = 'To Do'):
        self.id = id
        self.name = name
        self.description = description
        self.start = start
        self.due = due
        self.status = status
        self.last_modified_string = last_modified
        self.last_modified = last_modified
        #self.last_modified = datetime.strptime(last_modified, '%Y-%m-%dT%H:%M:%S.%fZ')

    @classmethod
    def convertFromTrello(item, card, board_list):
        return item(card['id'], card['name'], card['desc'], card['start'], card['due'], card['dateLastActivity'], board_list['name'])

    @classmethod
    def convertFromMongo(item, card):
        return item(card['_id'], card['name'], card['desc'], card['start'], card['due'], card['dateLastActivity'], card['boardList'])
        
    def reset(self):
        self.status = 'To Do'

    def complete(self):
        self.status = 'Done'
