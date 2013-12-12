from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required


class LoginForm(Form):
    staff_id = TextField('Staff ID', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
