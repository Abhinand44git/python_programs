customer_name=input("Customer Name: ")
card_number=int(input("Card Number: "))
pin_number=input("PIN Number: ")
account_type=input("Account Type: ")
available_balance=float(input("Available Balance: "))
withdrawal_amount=float(input("Withdrawal Amount: "))

remaining_balance=available_balance

valid_account_types=["Savings","Current"]
valid_account_type=account_type in valid_account_types

stored_pin="0987"
pin_verified=stored_pin==pin_number
sufficient_balance=withdrawal_amount<=available_balance
balance_greater_than_zero=available_balance>0

print("\n-------SMART ATM SYSTEM-------")
print("Customer Name: ",customer_name)
print("Card Number: ",card_number)
print("Account Type: ",account_type)
print("Available Balance: ",available_balance)
print("Withdrawal Amount: ",withdrawal_amount)
print("\n")

print("PIN Verified: ",pin_verified)
print("Valid Account Type: ",valid_account_type)
print("Sufficient Balance: ",sufficient_balance)
print("\n")

if pin_verified and valid_account_type and sufficient_balance:
    print("Transaction Status: Successful")
    print("\n")
    remaining_balance-=withdrawal_amount
    processing_fee_rate=0.2
    processing_fee=withdrawal_amount
    processing_fee*=processing_fee_rate
    total_deducted_amount=withdrawal_amount
    total_deducted_amount+=processing_fee
else:
    print("Transaction Status: Failed")

print("Remaining Balance: ",remaining_balance)
print("\n")

account1= account_type
account2= account_type

#print("Datatype of Customer Name: ",type(customer_name))
#print("Datatype of PIN Number: ",type(pin_number))
print("Datatype of Balance: ",type(available_balance))
print("Datatype of Withdrawal: ",type(withdrawal_amount))
print("\n")
#print("Datatype of Account Type: ",type(account_type))

print("Is Balance float?: ",isinstance(available_balance,float))
print("Is Withdrawal Amount float?: ",isinstance(withdrawal_amount,float))
print("\n")
#print("Is Customer Name string?: ",isinstance(customer_name,str))

print("ID of Balance: ",id(available_balance))
print("ID of Remaining_Balance: ",id(remaining_balance))
#print("ID of Account_type: ",id(account_type))
print("\n")
print("Account1 is Account2: ",account1 is account2)
print("Account1 is not Account2: ",account1 is not account2)