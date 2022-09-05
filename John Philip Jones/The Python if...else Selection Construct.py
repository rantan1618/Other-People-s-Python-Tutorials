bank_charge = 10
bank_bonus = 1
account_balance = 50
if account_balance < 0:
    account_balance = account_balance - bank_charge
else:
    account_balance = account_balance + bank_bonus
print("The account balance is " + str(account_balance))