from flask import Flask
from application.config import Config as wconfig
from application.config import DevelopmentConfig
from application.config import ProductionConfig
from flask.ext.assets import Environment
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
import dataset
from datetime import datetime, date

import os


# setup Flask app
app = Flask(__name__)

admin = Admin(app)

# check APP_ENV environment variable and load the approprite config
if 'APP_ENV' in os.environ and os.environ['APP_ENV'] == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

var = wconfig.SQLALCHEMY_DATABASE_URI
pdb = SQLAlchemy(app)
ds = dataset.connect(var)

#print ds.tables
#print ds
migrate = Migrate(app, pdb)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
#print pdb

# load assets plugin
assets = Environment(app)

# connect to the database



# load the login manager
login_manager = LoginManager()
login_manager.setup_app(app)

from application.models.user import User

# login extension
@login_manager.user_loader
def load_user(email):
	#print "Load-user method"

   	try:
		#print "Loading."
		user = User.query.filter_by(staff_id=email).first()
		#print user
		return user
	except:
		print "User doesn't exist?"
		return None


# import models
#from application.models.staff import User as PUser, Role
#from application.models.nurse import Nurse, Doctor, Patient
from application.models.user import User, Doctor, Patient, Diagnosis, Prescription

# Setup Flask Security
#user_datastore = SQLAlchemyUserDatastore(pdb, User2, Role)
#security = Security(app, user_datastore)

#admin.add_view(ModelView(PUser, pdb.session))
#admin.add_view(ModelView(Role, pdb.session))
admin.add_view(ModelView(User, pdb.session))
admin.add_view(ModelView(Doctor, pdb.session))
admin.add_view(ModelView(Patient, pdb.session))
admin.add_view(ModelView(Diagnosis, pdb.session))
admin.add_view(ModelView(Prescription, pdb.session))



# import forms
import application.forms.login

# import controllers
import application.controllers.site

#Custom helper functions
def get_age(person):
	today = date.today()
	born = person.date_of_birth
	try: 
		birthday = born.replace(year=today.year)
	except ValueError: # raised when birth date is February 29 and the current year is not a leap year
		birthday = born.replace(year=today.year, day=born.day-1)
	if birthday > today:
		return today.year - born.year - 1
	else:
		return today.year - born.year

app.jinja_env.globals.update(get_age=get_age)