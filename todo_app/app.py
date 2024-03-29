import os

from flask import Flask, redirect, render_template, request, url_for
from todo_app.services import mongo
from todo_app.flask_config import Config
from todo_app.ViewModel import ViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    
    @app.route('/')
    def index():
        return view()

    @app.route('/add', methods = ['POST'])
    def add():
        mongo.add_item(request.form.get('title'))
        return redirect(url_for('index'))

    def view():
        item_view_model = ViewModel(mongo.get_items())
        return render_template('/index.html', view_model=item_view_model)

    @app.route('/items/<id>/complete')
    def complete_item(id):
        mongo.complete_item(id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/start')
    def start_item(id):
        mongo.start_item(id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/reset')
    def reset_item(id):
        mongo.reset_item(id)
        return redirect(url_for('index'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
