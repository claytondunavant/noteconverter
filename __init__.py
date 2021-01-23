from flask import Flask, render_template, send_file, send_from_directory, flash, request, redirect, url_for
import flaskFileService
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "/get-files/<path:path>"
ALLOWED_EXTENSIONS = {"pdf"}

app = Flask(__name__)

DOWNLOAD_DIRECTORY = "get-files"

@app.route('/')
def home():
	# flaskFileService.get_files('get-files')
	return render_template('home.html')

@app.route('/download/')
def download():
	return render_template('home.html')

@app.route('/', methods = ['GET', 'POST'])
def uploadFiles():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		return 'file uploaded successfully'

@app.route('/get-files/<path:path>', methods = ['GET', 'POST'])
def get_files(path):
    try:
        return send_from_directory(DOWNLOAD_DIRECTORY, path, as_attachment=True)
    except FileNotFoundError:
        return False
	
	return render_template(download.html)

'''
@app.route('/upload/')
def upload():
	return render_template('upload.html')'''

if __name__ == '__main__':
	app.run()
