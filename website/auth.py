from flask import Blueprint
"""Blueprints are used to group related routes, templates, and static files, 
making it easier to organize large applications or reuse code across multiple projects."""
from flask import render_template

#This line creates an instance of the Blueprint class
auth = Blueprint('auth', __name__) #the second auth in argument is the name of my blueprint to represent it 

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>" 

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html") 