from flask_wtf import Form
from wtforms import TextField, DateField, DecimalField, SubmitField
from wtforms import validators, ValidationError

class TransactForm(Form):
   date = DateField('Date of Transaction', [validators.required()])
   description = TextField('Description', [validators.required()])
   amount = DecimalField('Amount', [validators.required()])
   submit = SubmitField("Add Transaction")