from website import db #import my database I created in my file init
from flask_login import UserMixin #for specify the model is for all user input
from sqlalchemy.sql import func #permit for if we add a new note , it automacaly give the date of this day

#Here is a db for all note the user will put
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #foreighkey permit to make a relationship between each note and it user


#Here we have created a db for all user input
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #this id mean all object will be create need to have some key to identify it (each user will be identifie bye a unique key)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
