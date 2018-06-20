
from app import *
from forms import LoginForm, RegForm
from flask import flash, Flask
from flaskext.mysql import MySQL
from flask import Flask,request,render_template, redirect, url_for
from werkzeug.wrappers import Response
from model import *
import jwt
import datetime
from datetime import datetime, timedelta
import json
from flask import make_response
import urllib.request
import requests

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 1800
API_URL='http://localhost:81/appleservicechallenge_tokenvalidationapi.php?token='

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'GET':
		return render_template('login.html', form=form)
	elif request.method == 'POST' and form.validate():
		username = request.form['username']
		password = request.form['password']
		data=retrieveUser(username,password)
		if data is False:
			flash("Username or Password is wrong")
			return render_template('login.html', form=form)
		else:
			flash("Logged in successfully")
			token= generatetoken(username)
			response=make_response(redirect(url_for('greeting')))
			response.set_cookie('Authorization', value=token)
			return response
	else:
		flash(form.errors)
		return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
	# here we are only removing the token from client but we can also create a toek blacklist
	flash("Logged out successfully")
	response=make_response(redirect(url_for('index')))
	response.set_cookie('Authorization', value='')
	return response

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegForm(request.form)
	if form.validate_on_submit():
		username=request.form['username']
		email=request.form['email']
		password=request.form['password']
		data=checkUser(username,email)
		if data is not None:
			flash('username or email already exist!')
		else:
			affected_count=insertUser(username,email,password)
			if affected_count==0:
				flash('unable to register')
			else:
				flash('Thanks for registering')
				return redirect(url_for('index'))
	elif request.method == 'POST' and not form.validate():
		flash('failed validation!')
	return render_template('register.html', form=form)

@app.route('/greeting')
def greeting():
	if 'Authorization' in request.cookies:
		headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
		response= requests.get(API_URL+request.cookies.get('Authorization'), headers=headers)
		data= response.json() 
		status = data['status']
		if "invalid" in status:
			flash("Invalid Session! Login Again!")
		else:
			flash('Greetings '+ data['data'])
			return render_template('greeting.html')
		return redirect(url_for('index'))
	else:
		flash("Unauthorized!")
		return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
	return redirect(url_for('login'))

def generatetoken(username):
	payload = {
        'user_id': username,
        'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    }
	jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
	return jwt_token

def checkvalidtoken(token):
	try:
		payload_data = jwt.decode(token,JWT_SECRET, JWT_ALGORITHM)
		#print(payload_data['user_id'])
		#print(payload_data['exp'])
		user=checkUser(payload_data['user_id'],'')
		if user is None:
			return -2
		return 1
	except jwt.ExpiredSignatureError:
		return -1
	except jwt.InvalidTokenError:
		return 0
	