import csv

def Transactions():
	#use to store the transaction data
	transactions = [
		{
			'id':1,
			'Date':'20-05-2018',
			'Description':'Mcd',
			'Amount':'40',
			'Balance': 500
		},
		{
			'id':2,
			'Date':'21-05-2018',
			'Description':'Ster-kinekor',
			'Amount':'97',
			'Balance': 403
		},
		{
			'id':3,
			'Date':'21-05-2018',
			'Description':'Uber',
			'Amount':'30',
			'Balance': 373
		}
	]

	return transactions

def getTransactions():
	file = open('data.csv', 'r+')
	balance = file.readline()
	transactions = []
	for line in file:
		val = [x.strip() for x in line.split(',')]
		newT = {
			'Date': val[0],
			'Description': val[1],
			'Amount':val[2],
			'Balance': val[3]
		}
		transactions.append(newT)

	# print(transactions)
	file.close() 

	return transactions

def newTransaction(date,description,amount):
	with open('data.csv', 'r') as file:
		# read a list of lines into data
		data = file.readlines()

	

if __name__ == '__main__':
	# getTransactions()
	addTransaction()