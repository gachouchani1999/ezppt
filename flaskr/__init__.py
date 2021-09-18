import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=('GET', 'POST'))
    def index():
        if request.method == 'POST':
            # replace this with an insert into whatever database you're using
            # result = store_result_in_database(request.args)
            # return redirect(url_for('success', result_id=result.id))
            return redirect(url_for('download'))
        return render_template('upload.html')

    @app.route('/download')
    def download():
        return render_template('download.html')

    Bootstrap(app)
    return app
