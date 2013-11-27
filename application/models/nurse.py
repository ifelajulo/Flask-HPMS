from application import pdb
import hashlib
import os


class Nurse(pdb.Model):
	id = pdb.Column(pdb.Integer, primary_key=True)
	nurse_id = pdb.Column(pdb.String(4), unique=True)
	email = pdb.Column(pdb.String(4))
	password = pdb.Column(pdb.String(80))
	first_name = pdb.Column(pdb.String(80))
	last_name = pdb.Column(pdb.String(80))
	doctor_id = pdb.Column(pdb.Integer, pdb.ForeignKey("doctor.id"))
	#patients = pdb.relationship('Patient', backref='nurse', lazy='dynamic')

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
	    if crypt_pass == self.password[40:]:
	        return True
	    else:
	        return False

	def __repr__(self):
		return "Nurse: " + self.last_name