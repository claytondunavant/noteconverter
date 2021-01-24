from flask import Flask, render_template, send_file, send_from_directory, flash, request, redirect, url_for
import flaskFileService
import os
from werkzeug.utils import secure_filename
import slides2notes

UPLOAD_FOLDER = "/get-files/<path:path>"
ALLOWED_EXTENSIONS = {"pdf"}

app = Flask(__name__)

DOWNLOAD_DIRECTORY = "get-files"

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/', methods = ['POST'])
def uploadFiles():
	uploadedFile = request.files['file']
	if uploadedFile.filename != '':
		uploadedFile.save(uploadedFile.filename)
	return redirect(url_for('home'))
	

@app.route('/get-files/<path:path>', methods = ['GET', 'POST'])
def get_files(path):
    try:
        return send_from_directory(DOWNLOAD_DIRECTORY, path, as_attachment=True)
    except FileNotFoundError:
        return False

@app.route('/upload', methods=["GET","POST"])
def upload():

	if request.method == "POST":

		if request.files:

			uploadedFile = request.files["pdf"]

			s2n = slides2notes.Slides2Notes(1,uploadedFile,"docx")

			return redirect(request.url)

	return render_template('upload.html')

if __name__ == '__main__':
	app.run()