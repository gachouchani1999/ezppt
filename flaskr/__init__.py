import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=('GET', 'POST'))
    def index():
        if request.method == 'POST':
            pass
        return render_template('index.html')

    @app.route('/loading')
    def loading():
        return render_template('loading.html')

    @app.route('/download')
    def download():
        return render_template('download.html')

    Bootstrap(app)
    return app
