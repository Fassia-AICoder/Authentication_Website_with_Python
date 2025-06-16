from flask import Flask #import the Flask class from the flask module
"""The class Flask used to create a Flask application instance,When I write app = Flask(__name__),
I'm creating an instance of the Flask class, which represents my web application and provides methods
for configuring routes, handling requests, and more."""


#This fonction permits to create an app configurate a key and return this app to be used elewhere int he code
def create_app():
    app = Flask(__name__) #Create an instance of the flask class
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    #I import my blueprint views from my file views and also auth
    from .views import views
    from .auth import auth

    #I used my blueprint view
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app