import pytest

from todo_app.ViewModel import ViewModel

from todo_app.todoItem import ToDoItem

from datetime import datetime, timedelta

def test_todo_items():
    items = []
    items.append(ToDoItem(1, 'List saved todo items', '', None, None, datetime.today(), 'To Do'))
    view_model = ViewModel(items)
    todo_items = view_model.todo_items
    assert len(todo_items) == 1

def test_doing_items():
    items = []
    items.append(ToDoItem(1, 'List saved todo items', '', None, None, datetime.today(), 'Doing'))
    view_model = ViewModel(items)
    doing_items = view_model.doing_items
    assert len(doing_items) == 1

def test_done_items():
    items = []
    items.append(ToDoItem(1, 'List saved todo items', '', None, None, datetime.today(), 'Done'))
    view_model = ViewModel(items)
    done_items = view_model.done_items
    assert len(done_items) == 1

def test_recent_done_items():
    items = []
    items.append(ToDoItem(1, 'List saved todo items', '', None, None, datetime.today(), 'Done'))
    view_model = ViewModel(items)
    done_items = view_model.recent_done_items
    assert len(done_items) == 1

def test_older_done_items():
    items = []
    items.append(ToDoItem(1, 'List saved todo items', '', None, None,  datetime.strftime((datetime.today()-timedelta(days=1)), "%Y-%m-%dT%H:%M:%S.%fZ"), 'Done'))
    view_model = ViewModel(items)
    done_items = view_model.older_done_items
    assert len(done_items) == 1

def test_show_all_done_items_getter():
    items = []
    view_model = ViewModel(items)
    assert view_model.show_all_done_items == False

def test_show_all_done_items_setter():
    items = []
    view_model = ViewModel(items)
    view_model.show_all_done_items = True
    assert view_model.show_all_done_items == True