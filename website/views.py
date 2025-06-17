from flask import Blueprint #import the Blueprint class from the flask module
"""Blueprints are used to group related routes, templates, and static files, 
making it easier to organize large applications or reuse code across multiple projects."""
from flask import render_template 

#This line creates an instance of the Blueprint class
views = Blueprint('views', __name__) #the second views in argument is the name of my blueprint to represent it 

#create a view or a route 
@views.route('/')
def home():
    return render_template("home.html")