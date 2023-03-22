n = int(input("Enter the number of customers: "))
balances = [] # Array containing each customer's deposit amount

# Enter the deposit amount of each customer
for i in range(n):
    balance = float(input("Enter the deposit amount of the th customer {}: ".format(i+1)))
    balances.append(balance)
    
max_balance = 0
max_customer = 0

# Calculate the amount received and print the result
for i in range(n):
    balance = balances[i]
    earned = balance * (1 + 0.0009) ** 20
    print("The {}th customer receives amount of {:.2f} after 20 years of paying insurance".format(i+1, earned))
    
    # Save the information of the customer with the largest amount of money received
    if earned > max_balance:
        max_balance = earned
        max_customer = i + 1
        
print("The {}th customer with the largest amount of money earned is {:.2f}".format(max_customer, max_balance))

