from flaskext.mysql import MySQL
from app import *
import traceback
from passlib.hash import pbkdf2_sha256 as sha256


def checkUser(username,email):
	con = mysql.connect()
	cursor=con.cursor()
	cursor.execute("SELECT * from member where username= %s or email=%s" , (username,email))
	data = cursor.fetchone()
	con.close()
	return data

def insertUser(username,email,password):
	con = mysql.connect()
	cursor=con.cursor()
	affected_count=0
	try:
		affected_count=cursor.execute("INSERT into appleservicechallenge.member(username,email,password) values (%s,%s,%s)" , (username,email,generate_hash(password)))
		con.commit()
	except Exception as e:
		print(traceback.format_exc())
	finally:
		con.close()
	return affected_count

def retrieveUser(username,password):
	con = mysql.connect()
	cursor=con.cursor()
	hash=generate_hash(password)
	print(hash)
	cursor.execute("SELECT password from member where username= %s" , (username))
	data =None
	data = cursor.fetchone()
	returnvalue=False
	if data is not None:
		returnvalue= verify_hash(password,data[0])
	con.close()
	return returnvalue

def generate_hash(password):
	return sha256.hash(password)
def verify_hash(password, hash):
	return sha256.verify(password, hash)