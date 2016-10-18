
##Determines credit card balance after making the minimum payment for 12 months based on the initial balance

Balance=float(input('What is your oustanding balance? '))
Annual_interest_rate=float(input('Enter the annual interest rate as a decimal: '))
Min_monthly_rate=float(input('Enter the minimum monthly payment rate as a decimal: '))

#monthly interest rate calculation
Monthly_rate=float(Annual_interest_rate/12.0)

#Initial Variables
Month=1
Total_paid=0


while Month <=12:

    #Calculates minimum monthly payment, subtracts payment from balance, adds payment to total paid variable
    Min_monthly_payment = round(Min_monthly_rate * Balance,2)
    Balance -= Min_monthly_payment
    Total_paid += Min_monthly_payment

    #Monthly interest payment calculated and added to balance
    Interest= round(Monthly_rate * Balance,2)
    Balance += Interest

    #Principal Payment calculation
    Principal_paid = round(Min_monthly_payment-Interest,2)

    print('Month = ', Month)
    print('Minimum monthly payment: ', Min_monthly_payment)
    print('Remaining balance (month): ', Balance)
    print('You paid ', Principal_paid, ' of the principal.')
    print('You paid ', Interest, ' in interest.  ')
    Month += 1
    print(' ')

print('Result')
print('Total Ammount Paid: ', Total_paid)
print('Remaining Balance: ', Balance)
    
    
