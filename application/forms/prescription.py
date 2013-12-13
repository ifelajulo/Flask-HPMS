from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, IntegerField
from wtforms.validators import Required


class PrescriptionForm(Form):
    staff_id = TextField('Medicine Name', validators=[Required()])
    frequency = IntegerField('Frequency', validators=[Required()])
    dosage = TextField('Dosage', validators=[Required()])