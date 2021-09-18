import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=['GET', 'POST'])
    def upload_file():
     return render_template('upload.html')
    
    
    @app.route('/uploader', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
             f = request.files['file']
             f.save(secure_filename(f.filename))
        return render_template('download.html')

    Bootstrap (app)
    return app
