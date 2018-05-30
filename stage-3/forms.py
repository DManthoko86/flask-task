from flask_wtf import Form
from wtforms import TextField, DateField, DecimalField, SubmitField

class TransactForm(Form):
   date = DateField('Date of Transaction', format='%d/%m/%Y')
   description = TextField('Description')
   amount = DecimalField('Amount')
   submit = SubmitField("Add Transaction")