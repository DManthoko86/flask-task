from flask_wtf import Form
from wtforms import TextField, DateField, DecimalField, SubmitField

class TransactForm(Form):
   date = DateField('Date of Transaction', format='%d/%m/%Y', [validators.required()])
   description = TextField('Description', [validators.required()])
   amount = DecimalField('Amount', [validators.required()])
   submit = SubmitField("Add Transaction")