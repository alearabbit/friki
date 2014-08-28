# -*- coding: utf-8 -*-
from app import db
 
 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    access_token_facebook = db.Column(db.String(255))
    join_date = db.Column(db.DateTime(), default=db.func.now())