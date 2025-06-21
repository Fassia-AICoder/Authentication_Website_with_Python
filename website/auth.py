from flask import Blueprint
"""Blueprints are used to group related routes, templates, and static files, 
making it easier to organize large applications or reuse code across multiple projects."""
from flask import render_template # permit to print all page I create in frontend
from flask import request #permit to save all information the user will put in sign up
from flask import flash #permit to send a flash message to th user when he put wrong information
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash #Use to make secure a password
from flask import redirect
from flask import url_for
from website import db
from flask_login import login_user, login_required, logout_user, current_user



#This line creates an instance of the Blueprint class
auth = Blueprint('auth', __name__) #the second auth in argument is the name of my blueprint to represent it 

# Here are views I create for each page

#For Login

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #Here I verify if the information of the user in my data base is the same he is entering
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True) #permit to remember a user was already login
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist', category='error')


    return render_template("login.html", user=current_user)# permit to print my login page


#For logout

@auth.route('/logout')
@login_required #it's mean we can't access this page that the user loged in
def logout():
    logout_user()
    return redirect(url_for('auth.login')) 


# For sign up

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    #Here is the way to save the information th user will put in sign up
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #Here is the way to verifie if the iformation that the user enter is value
        #if it's not that he have to recommence
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)