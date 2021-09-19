import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from flask import Flask, send_file
from . import doc_reader

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    @app.route('/', methods=['GET', 'POST'])
    def upload_file():
     return render_template('upload.html')
    
    
    @app.route('/uploader', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
             global f
             f = request.files['file']
             theme = request.form['theme']
             f.save(secure_filename(f.filename))
             path = '../'+f.filename
             doc_reader.final_create(int(theme),path)
        return render_template('download.html')

    @app.route('/download')
    def download():
         filename_new = f.filename[:f.filename.find('.')]
         path = '../'+filename_new + '.pptx'
         return send_file(path, as_attachment=True)
         

    Bootstrap (app)
    return app
