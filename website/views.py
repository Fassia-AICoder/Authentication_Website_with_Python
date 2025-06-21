from flask import Blueprint #import the Blueprint class from the flask module
"""Blueprints are used to group related routes, templates, and static files, 
making it easier to organize large applications or reuse code across multiple projects."""
from flask import render_template 
from flask_login import login_required, current_user
from flask import request
from .models import Note
from flask import flash
from . import db
import json
from flask import jsonify


#This line creates an instance of the Blueprint class
views = Blueprint('views', __name__) #the second views in argument is the name of my blueprint to represent it 

#create a view or a route 
@views.route('/', methods=['GET', 'POST'])
@login_required # we can get a log page without login
def home():
    if request.method == 'POST':
        note = request.form.get('note') #Gets the note from the HTML

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')


    
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note) 
            db.session.commit()
    return jsonify({})