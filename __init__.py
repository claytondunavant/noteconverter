from flask import Flask, render_template, send_file, send_from_directory
import flaskFileService

app = Flask(__name__)

DOWNLOAD_DIRECTORY = "get-files"

@app.route('/')
def home():
	# flaskFileService.get_files('get-files')
	return render_template('home.html')

@app.route('/download/')
def download():
	return render_template('download.html')

@app.route('/get-files/<path:path>', methods = ['GET', 'POST'])
def get_files(path):
    try:
        return send_from_directory(DOWNLOAD_DIRECTORY, path, as_attachment=True)
    except FileNotFoundError:
        return False

'''
@app.route('/upload/')
def upload():
	return render_template('upload.html')'''

if __name__ == '__main__':
	app.run()
