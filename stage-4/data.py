import csv, ast, requests

def getTransactions():
	file = open('data.csv', 'r+')
	# balance = file.readline()
	transactions = []
	for line in file:
		val = [x.strip() for x in line.split(',')]

		# access Luno/BitX api to find current Bitcoin value in ZAR
		r = requests.get('https://api.mybitx.com/api/1/ticker?pair=XBTZAR')

		# get the text value from the response, strip any leading or ending whitespace
		# then convert the string representation of the dictionary to an actual dictionary
		r_dict =  ast.literal_eval(r.text.strip())

		# r_dict would be in this format 
		# {"pair":"XBTZAR","timestamp":1527784000706,"bid":"99776.00","ask":"99777.00","last_trade":"99776.00","rolling_24_hour_volume":"412.339248"}
		# use last_trade for current BTC value
		btc_val = float(r_dict['last_trade'])

		newT = {
			'Date': val[0],
			'Description': val[1],
			'Amount':val[2],
			'Balance': val[3],
			'BTCValue': "{:.6f}".format(float(val[3])/btc_val)
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