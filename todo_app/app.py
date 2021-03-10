from flask import Flask, redirect, render_template, request, url_for

from todo_app.services import trello

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return view()

@app.route('/add', methods = ['POST'])
def add():
    trello.add_item(request.form.get('title'))
    return redirect(url_for('index'))

def view():
    items = trello.get_items()
    return render_template('/index.html', items=items)

@app.route('/items/<id>/complete')
def complete_item(id):
    trello.update_item(id, 'Done')
    return redirect(url_for('index'))

@app.route('/items/<id>/reset')
def reset_item(id):
    trello.update_item(id, 'To Do')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
