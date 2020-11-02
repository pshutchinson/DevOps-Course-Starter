from flask import Flask, render_template, request

from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    #return 'Hello World!'
    items = get_items()
    return render_template('/index.html', items=items)

@app.route('/add', methods = ['POST'])
def add():
    add_item(request.form.get('title'))
    items = get_items()
    return render_template('/index.html', items=items)

if __name__ == '__main__':
    app.run()
