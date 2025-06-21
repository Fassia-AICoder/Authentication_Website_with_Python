from flask import Flask #import the Flask class from the flask module
"""The class Flask used to create a Flask application instance,When I write app = Flask(__name__),
I'm creating an instance of the Flask class, which represents my web application and provides methods
for configuring routes, handling requests, and more."""
from flask_sqlalchemy import SQLAlchemy #permit to create a dabase
from os import path #path permit to verify all 
from flask_login import LoginManager


db = SQLAlchemy() #create an instance of the class SQLALchemy
DB_NAME = "database.db" # name tha database


#This fonction permits to create a new app with flask  
def create_app():
    app = Flask(__name__) #Create an instance of the flask class
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs' # Configuration of a new key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #configue where my data will be located
    db.init_app(app) #initialyse a database for my app


    #I import my blueprint views from my file views and also auth
    from .views import views
    from .auth import auth

    #I used my blueprint view
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #Here I imports all model I created and I create my db
    from .models import User, Note
    #I call my function create_database
    create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

#I create a new function to verify if my database exist
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')