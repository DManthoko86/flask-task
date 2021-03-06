import csv

def getTransactions():
	file = open('data.csv', 'r+')
	# balance = file.readline()
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

	balance = float(data[len(data)-1].split(',')[3]) - float(amount)
	balance = "{:.2f}".format(balance)
	newT = date + ',' + description + ',' + amount + ',' + balance + '\n'
	data.append(newT)
	
	# and write everything back
	with open('data.csv', 'w') as file:
		file.writelines( data )

# if __name__ == '__main__':
# 	# getTransactions()
# 	newTransaction('1','2','3')