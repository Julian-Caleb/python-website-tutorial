from . import db
from flask_login import UserMixin # Import UserMixin
from sqlalchemy.sql import func

class Note(db.Model) :
    id = db.Column(db.Integer, primary_key=True) # ID as primary key
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # Get time zone with current time as default
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # user_id as foreign key with one to many relationship

class User(db.Model, UserMixin) : # Create class, inherit database model
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(150), unique=True) # No user has the same email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # Relationship with Note