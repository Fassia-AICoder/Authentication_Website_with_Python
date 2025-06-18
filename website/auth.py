from flask import Blueprint
"""Blueprints are used to group related routes, templates, and static files, 
making it easier to organize large applications or reuse code across multiple projects."""
from flask import render_template # permit to print all page I create in frontend
from flask import request #permit to save all information the user will put in sign up
from flask import flash #permit to send a flash message to th user when he put wrong information

#This line creates an instance of the Blueprint class
auth = Blueprint('auth', __name__) #the second auth in argument is the name of my blueprint to represent it 

# Here are views I create for each page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")# permit to print my login page

@auth.route('/logout')
def logout():
    return "<p>logout</p>" 

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    #Here is the way to save the information th user will put in sign up
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #Here is the way to verifie if the iformation that the user enter is value
        #if it's not that he have to recommence
        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category='error')
        elif len(firstName) < 2 :
            flash("First name must be greater than 1 characters.", category='error')
        elif password1 != password2:
            flash("Password don\'t match, try again.", category='error')
        elif len(password1) < 7:
            flash("Password must be at least 7 characters.", category='error')
        else:
            #add user to database
            flash("Acount created!", category='success')



    return render_template("sign_up.html") 