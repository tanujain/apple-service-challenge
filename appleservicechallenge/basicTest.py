from flask import Flask
from flask_testing import TestCase
import unittest
from app import *
import string, random
import urllib.request

API_URL='http://localhost:81/appleservicechallenge_tokenvalidationapi.php?token='

class MyTest(TestCase):
	def create_app(self):
		#app = Flask(__name__)
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		return app

	def test_index(self):
		#try:
		print("**Testing Index Page Status Code**")
		app = self.create_app().test_client()
		self.assert_200(app.get("/index"))
		print("**Succeeded**\n\n")

	def test_login_page(self):
		print("**Testing Login Page Status Code**")
		app = self.create_app().test_client()
		data = app.get("/login")
		self.assertEqual(data.status_code, 200)
		self.assertTrue('Log In' in data.get_data(as_text=True))
		print("**Succeeded**\n\n")

	def test_register_page(self):
		print("**Testing Register Page Status Code**")
		app = self.create_app().test_client()
		data = app.get("/register")
		self.assertEqual(data.status_code, 200)
		self.assertTrue('Register' in data.get_data(as_text=True))
		print("**Succeeded**\n\n")

	def test_greeting_page(self):
		#unauthorized access. client redirects to login page via 302
		print("**Try accessing greeting Page directly**")
		app = self.create_app().test_client()
		data=app.get("/greeting")
		self.assertRedirects(data, url_for("index"))
		print("**Succeeded**\n\n")

	def test_logout_page(self):
		print("**Testing Logout page**")
		app = self.create_app().test_client()
		data=app.get("/logout")
		self.assertRedirects(data, url_for("index"))
		print("**Succeeded**\n\n")

	def test_badurl_page(self):
		#check for any invalid url
		print("**Testing Wrong Page**")
		app = self.create_app().test_client()
		data=app.get("/badpage")
		self.assertRedirects(data, url_for("login"))
		print("**Succeeded**\n\n")

	def test_login_functionality(self):
		print("**Testing Login Functionality**")
		app = self.create_app().test_client()
		
		#check if correct username password sets the Authorization cookie
		data= app.post("/login",data= dict(username='tanujain', password= 'qwertyuiop'))
		setheaders=data.headers['Set-Cookie']
		self.assertTrue('Authorization=' in setheaders)
		
		#check if correct username password takes us to the page where Log OUt text is defined
		data= app.post("/login",data= dict(username='tanujain', password= 'qwertyuiop'), follow_redirects=True )
		self.assertEqual(data.status_code, 200)
		self.assertTrue('Log Out' in data.get_data(as_text=True))

		#check if greetings page accessed with the cookie generated with correct username and password gives greeting message
		#here api is also verified that with correct token it gives correct message 
		data=app.get("/greeting",headers={"COOKIE": setheaders})
		self.assertTrue(b"Greetings tanujain" in data.data)
		print("**Succeeded**\n\n")

	def test_register_functionality(self):
		print("**Testing Register Functionality**")
		app = self.create_app().test_client()
		char_set = string.ascii_uppercase + string.digits
		randomid = ''.join(random.sample(char_set*6, 6))
		data= app.post("/register",data= dict(username=randomid, email= randomid+"@gmail.com", password = '1234567890', confirm='1234567890'), follow_redirects=True)
		self.assertTrue('Thanks for registering' in data.get_data(as_text=True))
		print("**Succeeded**\n\n")

	def test_api_expiredtoken(self):
		print("**Testing API with expired token**")
		response= requests.get(API_URL+"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjkyNTA0MzksInVzZXJfaWQiOiJ0YW51amFpbiJ9.sEoVLgb2M7MFWUoIH-D9aWe2zHDgyRRasWlgvTgvu00")
		data= response.json() 
		status = data['status']
		self.assertTrue( "invalid" in status)
		print("**Succeeded**\n\n")

	def test_api_withouttoken(self):
		print("**Testing API with without token**")
		response= requests.get(API_URL)
		data= response.json() 
		status = data['status']
		self.assertTrue( "invalid" in status)
		print("**Succeeded**\n\n")


if __name__ == '__main__':
	unittest.main()