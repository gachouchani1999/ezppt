import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from flask import Flask, send_file
from . import doc_reader
from . import requesting


app = Flask(__name__, instance_relative_config=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
     return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])

def index():
     if request.method == 'POST':
          f = request.files['file']
          requesting.store_file(f)
          file_name = f.filename
          file_name = file_name.replace(" ","_")
          theme = request.form['theme']
          file_name = file_name.replace(" ","_")
          file_name = file_name.replace("(","")
          file_name = file_name.replace(")","")
          f.save(secure_filename(file_name))
          doc_reader.final_create(int(theme),file_name)
          
          return render_template('download.html')



@app.route('/download')
def download():
          file_name = requesting.store_file()
          filename_new = file_name[:file_name.find('.')]
          path = '../'+filename_new + '.pptx'
          return send_file(path, as_attachment=True)

         

Bootstrap (app)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=False)