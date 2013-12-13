from application import pdb
from flask.ext.security import UserMixin, RoleMixin
import os
import hashlib
from datetime import datetime, date


prescriptions = pdb.Table('prescriptions', 
                          pdb.Column('prescription_id', pdb.Integer, pdb.ForeignKey('prescription.id')),
                          pdb.Column('patient_id', pdb.Integer, pdb.ForeignKey('patient.id')))

diagnoses = pdb.Table("diagnoses",
                      pdb.Column('diagnosis_id', pdb.Integer, pdb.ForeignKey('diagnosis.id')),
                      pdb.Column('patient_id', pdb.Integer, pdb.ForeignKey('patient.id')))

class Diagnosis(pdb.Model):
    id = pdb.Column(pdb.Integer, primary_key=True)
    name=pdb.Column(pdb.String)

    def __repr__(self):
        return self.name


class Doctor(pdb.Model, UserMixin):
    id = pdb.Column(pdb.Integer, primary_key=True)
    staff_id = pdb.Column(pdb.String(4), unique=True)
    password = pdb.Column(pdb.String(80))
    first_name = pdb.Column(pdb.String(80))
    last_name = pdb.Column(pdb.String(80))


class User(pdb.Model, UserMixin):
    id = pdb.Column(pdb.Integer, primary_key=True)
    staff_id = pdb.Column(pdb.String(4), unique=True)
    password = pdb.Column(pdb.String(80))
    first_name = pdb.Column(pdb.String(80))
    last_name = pdb.Column(pdb.String(80))
    doctor_id = pdb.Column(pdb.Integer, pdb.ForeignKey('user.id'))
    role = pdb.Column(pdb.Integer)
    patients = pdb.relationship('Patient', backref="user", lazy="dynamic")


    def __repr__(self):
        if (self.role == 0):
            return "Nurse " + self.last_name
        else:
            return "Doctor " + self.last_name

    def set_password(self, password):
        """ Hash password on the fly """
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        password_salt = hashlib.sha1(os.urandom(60)).hexdigest()
        crypt = hashlib.sha1(password + password_salt).hexdigest()
        self.password = unicode(password_salt + crypt, 'utf-8')

    def verify_password(self, password):
        """ Check the password against existing credentials  """
        if isinstance(password, unicode):
            password = password.encode('utf-8')

        password_salt = self.password[:40]
        crypt_pass = hashlib.sha1(password + password_salt).hexdigest()
        if crypt_pass == self.password[40:] or password == self.password:
            return True
        else:
            return False

    def get_id(self):
        return self.staff_id

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

class Patient(pdb.Model):
    id = pdb.Column(pdb.Integer, primary_key=True)
    first_name = pdb.Column(pdb.String(50))
    last_name = pdb.Column(pdb.String(50))
    nurse_id = pdb.Column(pdb.Integer, pdb.ForeignKey('user.id'))
    sex = pdb.Column(pdb.Integer)
    date_of_birth = pdb.Column(pdb.Date)
    date_of_admission = pdb.Column(pdb.DateTime)
    prescriptions = pdb.relationship('Prescription', secondary=prescriptions,
                                    backref=pdb.backref('patients', lazy="dynamic"))
    diagnoses = pdb.relationship('Diagnosis', secondary=diagnoses,
                                 backref=pdb.backref('patients', lazy="dynamic"))

    other_info = pdb.Column(pdb.String)

    def __repr__(self):
        return self.first_name + " " + self.last_name


class Prescription(pdb.Model):
    id = pdb.Column(pdb.Integer, primary_key=True)
    name=pdb.Column(pdb.String)
    frequency = pdb.Column(pdb.String)
    dosage = pdb.Column(pdb.String)

    def __repr__(self):
        return self.name
