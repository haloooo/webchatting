from flask import Flask
from flask import render_template
from flask import send_from_directory
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')

@app.route('/')
def index():
    return render_template('halo-hello.html')

if __name__ == '__main__':
    app.run()
