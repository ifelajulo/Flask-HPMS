from application import pdb
from flask.ext.security import UserMixin, RoleMixin

roles_users = pdb.Table('roles_users', 
	pdb.Column('user_id', pdb.Integer(), pdb.ForeignKey('user.id')), 
	pdb.Column('role_id', pdb.Integer(), pdb.ForeignKey('role.id')))
#
#nurse_doctors = pdb.Table('doctors_nurses')


class Role(pdb.Model):
	id = pdb.Column(pdb.Integer(), primary_key = True)
	name = pdb.Column(pdb.String(80), unique=True)
	description = pdb.Column(pdb.String(255))

class User(pdb.Model):
	id = pdb.Column(pdb.Integer, primary_key = True)
	#staff_id = pdb.Column(pdb.String(5), unique=True)
	password = pdb.Column(pdb.String(80))
	name = pdb.Column(pdb.String(80))
	#roles = pdb.relationship('Role', secondary=roles_users, backref=pdb.backref('users', lazy='dynamic'))
