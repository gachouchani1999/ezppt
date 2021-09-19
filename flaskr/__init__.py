import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from flask import Flask, send_file
from . import doc_reader


app = Flask(__name__, instance_relative_config=True)
global f
@app.route('/', methods=['GET', 'POST'])
def upload_file():
     return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def index():
     if request.method == 'POST':
          f = request.files['file']
          theme = request.form['theme']
          f.filename = f.filename.replace(" ","_")
          f.save(secure_filename(f.filename))
          doc_reader.final_create(int(theme),f.filename)
          os.remove(f.filename)
          return render_template('download.html')



@app.route('/download')
def download():
          filename_new = f.filename[:f.filename.find('.')]
          path = '../'+filename_new + '.pptx'
          return send_file(path, as_attachment=True)

         

Bootstrap (app)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=False)