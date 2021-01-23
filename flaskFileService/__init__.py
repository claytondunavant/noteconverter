from flask import Flask, render_template, send_file, send_from_directory


app = Flask(__name__)

DOWNLOAD_DIRECTORY = "get-files"

@app.route('/get-files/<path:path>', methods = ['GET', 'POST'])
def get_files(path):
    try:
        return send_from_directory(DOWNLOAD_DIRECTORY, path, as_attachment=True)
    except FileNotFoundError:
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000, threaded = True, debug = True)
