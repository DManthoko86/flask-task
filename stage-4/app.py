from flask import Flask, render_template, redirect, flash, request, redirect
from data import getTransactions, newTransaction
from forms import TransactForm

#export FLASK_APP=app.py
#export FLASK_ENV=development
#flask run

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods=['GET', 'POST'])
def index():
	form = TransactForm(request.form)
	if request.method == 'POST':
		return addTransaction(form)

	return render_template('home.html', transactions=getTransactions(), form = form)

def addTransaction(form):
	date=request.form['date']
	description=request.form['description']
	amount=request.form['amount']
	
	try:
		float(amount)
	except ValueError:
		flash('Value for amount should be integer(40) or float(40.00)')
		return redirect('/')

	newTransaction(date,description,amount)

	return render_template('success.html')

if __name__ == '__main__':
	app.run()