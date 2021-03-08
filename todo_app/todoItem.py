class ToDoItem:

    def __init__(self, id, name, description, due, status = 'To Do'):
        self.id = id
        self.name = name
        self.description = description
        self.due = due
        self.status = status

    @classmethod
    def convertFromTrello(item, card, board_list):
        return item(card['id'], card['name'], card['desc'], card['due'], board_list['name'])

    def reset(self):
        self.status = 'To Do'

    def complete(self):
        self.status = 'Done'
