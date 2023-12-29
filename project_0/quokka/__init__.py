from flask import Flask


app = Flask(__name__)

import quokka.views.ui_views
# A fenti import azért kell az 'app' def alá, hogy a körkörös importot
# feloldjuk; ha az app fölött lenne, akkor a ui_views importjában az app-ot
# importálja de még azelőtt, hogy az app létre lett volna hívva.
# QFS-03 26-ik perc

from flask_sqlalchemy import SQLAlchemy # adding database functionalty
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Getting rid of some 
                                                     # modification
db = SQLAlchemy(app)

class Device(db.Model):

    '''Defining the class, what columns should be in the database'''

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, unique = True, nullable = False) 
    # unique = True: names should be different
    # nullable = False : name should always be there
    ip_address = db.Column(db.Text)
    vendor = db.Column(db.Text)
    os = db.Column(db.Text)
    hostname = db.Column(db.Text)


db.create_all()

from quokka.controller.util import import_devices
for device in import_devices():
    device_object = Device(**device) # an instance of class Device
    db.session.add(device_object)

db.session.commit() # Writing data to the database