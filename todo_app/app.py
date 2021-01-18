from flask import Flask, redirect, render_template, request, url_for

from todo_app.data.session_items import get_items, add_item, remove_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return view()

@app.route('/add', methods = ['POST'])
def add():
    add_item(request.form.get('title'))
    return redirect(url_for('index'))

def view():
    items = get_items()
    return render_template('/index.html', items=items)

if __name__ == '__main__':
    app.run()
