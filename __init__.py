from flask import Flask, render_template
import flaskFileService
import slides2notes

app = Flask(__name__)

@app.route('/')
def home():
	# flaskFileService.get_files('get-files')
	return render_template('home.html')

@app.route('/download/')
def download():
	return render_template('download.html')
'''
@app.route('/upload/')
def upload():
	return render_template('upload.html')'''

if __name__ == '__main__':
	app.run(debug=True)
