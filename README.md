# apple-service-challenge

Build and Run Instructions:

Technologies/Framework used and Functionality:

1. Website Service: The website service is created in Python using the Flask Framework. Flask is simple and lighweight and is a choice for building web applications which need fine-grained control. Flask MVC framework is used for better code organization and readability.

It has the following pages:
Index-> provide option to login or register.
Login-> provide login form (Username and password). Once user provides the correct credentials, he/she will be redirected to the Greetings page.
Register-> provide new user registration form (Username, Email, Password, Confirm Password). Once user submits the form with the required data, his details will be added to the database and user will be redirected to the index page. No two users can have the same Email or Username.
Greeting-> A validated user will reach this page after successful login. User credentials on the login page are validated with the entries in database. Once validated, a call is made to the greeting API with the generated token. API would validate the token and return json response.

All the basic validations are added to the login and register forms. 

2. Greeting API: The API is written in PHP.
