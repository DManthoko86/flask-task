from flask import Flask, render_template
from data import Transactions

app = Flask(__name__)

Transactions = Transactions()

@app.route('/')
def index():
	return render_template('home.html', transactions=Transactions)

if __name__ == '__main__':
	app.run()