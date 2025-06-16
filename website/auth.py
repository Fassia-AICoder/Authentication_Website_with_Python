from flask import Blueprint
"""Blueprints are used to group related routes, templates, and static files, 
making it easier to organize large applications or reuse code across multiple projects."""


#This line creates an instance of the Blueprint class
auth = Blueprint('auth', __name__) #the second auth in argument is the name of my blueprint to represent it 

@auth.route('/login')
def login():
    return "<p>login</p>" 

@auth.route('/logout')
def logout():
    return "<p>logout</p>" 

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>" 