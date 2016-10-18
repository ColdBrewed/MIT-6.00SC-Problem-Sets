
##Determines the minimum fixed monthly payment needed to pay off the balance in 12 months

## get input

Initial_balance=float(input('What is your oustanding balance? '))
Annual_interest_rate=float(input('Enter the annual interest rate as a decimal: '))

#Initial Variables
Monthly_payment=0
Balance=Initial_balance
Monthly_rate=float(Annual_interest_rate/12.0)

#Test an increasing monthly payment (increments of $10 until balance can be paid in a year
while Balance > 0:

    Monthly_payment += 10
    Balance = Initial_balance
    Months=0

    #For each month in loop, Calc. interest, subtract monthly payment from balance, add Interest to Balance
    while Months < 12 and Balance > 0:
        Months += 1
        Interest=Monthly_rate*Balance
        Balance -= Monthly_payment
        Balance += Interest

        
print('Result')
print('Monthly payment required to pay off in one year: $', Monthly_payment)
print('Number of months needed: ', Months)
print('Balance: $', Balance)
    
    

