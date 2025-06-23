“This project was completed using English as a non-native French speaker (B2 upper-intermediate level), as part of my journey to improve both my technical and communication skills.”


📘 Project Title
Authentication Website with Python

🚀 Overview
A web application built using Flask that allows users to sign up , log in, log out and add note in a simple board.


🙋‍♀️ Motivation
I created this project as a step toward developing my main project, "Studyce"(see the Studyce repository for more information). 
To bring Studyce to life, I needed to learn how to build a simple website using Python in order to test all its features. 
With this goal in mind, I followed the YouTube tutorial 'Python Website Full Tutorial – Flask, Authentication, Databases and More' 
from the channel "Tech With Tim", which enabled me to create the project I'm presenting here.


🛠️ Features
User registration and login
Password hashing for security
Session management
Input validation
Logout functionality
add and delete note 


📌 Folder Structure
__init__.py : This file initializes the Flask application and sets up configurations,
              routes, and extensions. It acts as the central place where the app is created and bundled together.
main.py : This is the entry point of the application. It imports the Flask app from __init__.py and runs the server when the file is executed.
view.py : Contains the main routes of the website (the homepage).
auth.py : Handles all authentication-related routes, like login, registration, and logout.
templates/ : HTML files
static/ : JS
models.py — database models


🧰 Technologies Used
Python
Flask
Flask-WTF
Flask-Login
SQLAlchemy



