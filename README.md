# apple-service-challenge

The basic flow of the application is: 


New user visits the website and registers

Logs in with his username and password

credentials are validated at the backend

the JSON Web token is generated which is valid for thirty minutes

JWT sets as a cookie on the client browser 

Makes a request internally to the rest API  to validate the token

If validated the username is returned (fetched from token itself- no DB access) 

The user is greeted with his username

Redirected to the greetings page

Finally, the user can log out of his account




Build and Run Instructions:

To run the Website:
Python 3.4 is needed. All the packages in requirements.txt needs to be installed. follow the instruction in https://www.youtube.com/watch?v=kDRRtPO0YPA for setting up the server, creating the virtual environment and running the application code using gunicorn. Once done you will be able to access the website.

To setup and run the API:
php version>= 5 should be installed. Copy the contents of the API code folder to a folder in /var/www/html. Go to that folder and run php -S localhost:81. This will run the api locally on port 81 which will be called by website. (Live deployment is also done the same way and api and is hosted locally on the server. It is not accessible from outside.)

To setup the database:
create a database with database name, username and password as given in config.py file. Run the sql script given in the MySQL Script folder which will create the table with some data.



Technologies/Framework used and Functionality:

1. Website Service: 

The website service is created in Python using the Flask Framework. Flask is simple and lighweight and is a choice for building web applications which need fine-grained control. Flask MVC framework is used for better code organization and readability.

It has the following pages:

Index-> provide option to login or register.

Login-> provide login form (Username and password). Once user provides the correct credentials, he/she will be redirected to the Greetings page.

Register-> provide new user registration form (Username, Email, Password, Confirm Password). Once user submits the form with the required data, his details will be added to the database and user will be redirected to the index page. No two users can have the same Email or Username.

Greeting-> A validated user will reach this page after successful login. User credentials on the login page are validated with the entries in database. Once validated, a call is made to the greeting API with the generated token. API would validate the token and return json response.

All the basic validations are added to the login and register forms. field length checks, email validation etc have been added. CSRF protection is also enabled. User input is passed as query parameter to prevent SQL injection. XSS protection is there. Unauthorized access is also checked. No one can directly access the greetings page. Passwords stored in the database are hashed using the sha256 hashing algorithm rather than storing them in cleartext.

2. Greeting API:

The API is written in PHP. It would take the input token, decode it using the secret key and predefined algorithm. If the token is invalid i.e expired (older than 30 minutes) or Empty token or invalid length etc, API reponse would be {"status":"invalid token", "data":""} otherwise the decoded token will return the username {"status":"validtoken", "data": "username"}

3. Database: 

Mysql database is used to store the user information and all the database connection configuration is stored in config.py. Mysql is free and easy to use relational database. For now, there is only one existing table which stores the registered users information.

Basic Unit test cases are written in basictest.py file. In order to run them locally on the setup server from command line- use the command 'python <path to basictest.py>/basictest.py. It will check for all the basic functionalities such as index, login, logout, wrong url, register and greeting page responses, unauthorized access without token, login functionality etc but still there is a great scope to add more functionality and security to this application. This application can be customized to add the functionality to invalidate tokens (if a user logs out and tries to login within 30 minutes again using the same token then he/she shouldn't be able to do so), storing credentials and secret code on the server in environment variable etc rather than in files present in application code, setting up the server to allow https and application also to support it, email validation by sending a confirm email etc.  

For testing the functionality of the whole application, it is deployed at the given below URL.

URL: http://192.241.202.85/


[![Alt text for your video](https://img.youtube.com/vi/T-D1KVIuvjA/0.jpg)](https://youtu.be/-8EtpLd5zzo)
