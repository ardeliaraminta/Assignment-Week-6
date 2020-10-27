#Loop through each key in prices. For each key, print out the key along with its price and stock information. 
prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

# add stock to be able to create stock output
stock = {
"banana":8,
"apple":0,
"orange":9,
"pear":2
}

#for loop is used for iterations

for key in prices:
    print(key)
    print(" price: %s " % prices[key])
    print(" stock: %s " % stock[key])
    
   or 
#Use the key to access value of the dictionary values
#.format allow us do a string formatting and if {} is blank, it will pass values in str.format()

for key in prices:
    print(key)
    print('price: {}'.format(prices[key]))
    print('stock: {}'.format(stock[key]))
    
# new variable : total 

total = 0 
for key in prices:
    print(prices[key]*stock[key])
    total = total + prices[key] * stock[key]

print(" The total is: ", total )
  
