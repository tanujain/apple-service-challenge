
from flask import Flask
from flaskext.mysql import MySQL
from os import environ

app = Flask(__name__)
app.config.from_pyfile('config.py')
mysql = MySQL()
mysql.init_app(app)
from views import *

if __name__ == '__main__':
	HOST = environ.get('SERVER_HOST', 'localhost')
	try:
		PORT = int(environ.get('SERVER_PORT', '5555'))
	except ValueError:
		PORT = 5555
	app.run(HOST, PORT, debug=True)
