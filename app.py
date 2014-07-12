from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
	return '<H1>Measure Anything</H1>'

if __name__ == '__main__':
	manager.run()