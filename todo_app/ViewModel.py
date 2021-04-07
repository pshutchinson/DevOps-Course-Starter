from todo_app.services import trello

from datetime import datetime

def filterOnlyToday(x):
    return x.last_modified >= datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

def filterOlderThanToday(x):
    return x.last_modified < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)


class ViewModel(object):
    def __init__(self, items):
        self._items = items
        self._show_all = False

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        todo_iterator = filter(trello.filter_todo, self._items)
        todo_items = list(todo_iterator)
        return todo_items

    @property
    def doing_items(self):
        doing_iterator = filter(trello.filter_doing, self._items)
        doing_items = list(doing_iterator)
        return doing_items

    @property
    def done_items(self):
        done_iterator = filter(trello.filter_done, self._items)
        done_items = list(done_iterator)
        done_items.sort(key=lambda x: x.last_modified, reverse=True)
        return done_items

    @property
    def show_all_done_items(self):
        return self._show_all

    @show_all_done_items.setter
    def show_all_done_items(self, value):
        self._show_all = value

    @property
    def recent_done_items(self):
        return list(filter(filterOnlyToday, self.done_items))

    @property
    def older_done_items(self):
        return list(filter(filterOlderThanToday, self.done_items))

    @property
    def chosen_done_items(self):
        if (self._show_all):
            return self.older_done_items
        else:
            return self.recent_done_items
