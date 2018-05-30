from flask import Flask, render_template, redirect, flash, request, redirect
from data import getTransactions, newTransaction
from forms import TransactForm

#export FLASK_APP=app.py
#export FLASK_ENV=development
#flask run
#/mnt/c/Users/Dominic/Documents/flask-task/stage-2

#will need to create database model for the transactions
#will also need to add a form so that you can add new transactions
#probably best to add the form first
#http://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/

app = Flask(__name__)
app.secret_key = 'development key'

Transactions = getTransactions()

@app.route('/', methods=['GET', 'POST'])
def index():
	form = TransactForm(request.form)
	if request.method == 'POST':
		return addTransaction(form)

	return render_template('home.html', transactions=Transactions, form = form)

def addTransaction(form):
	date=request.form['date']
	description=request.form['description']
	amount=request.form['amount']
	# flash(date + " " + description + " " + amount)
	print(date)
	print(description)
	print(amount)
	print('------------------------------------------')

	newTransaction(date,description,amount)

	return redirect('/')


if __name__ == '__main__':
	app.run()