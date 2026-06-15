'''
def password_strength_checker(password):

    def scan_character():
        has_upper= False
        has_digit= False
        for char in password:
            if char.isupper():
                has_upper=True
            if char.isdigit():
                has_digit=True
        return has_digit,has_upper
    
    upper_found,digit_found=scan_character()
    if len(password)>=8 and upper_found and digit_found:
        print("Strong Password")
    elif len(password)>=6:
        print("Medium Password")
    else:
        print("Weak Password")
    
password=input("Enter a Password: ")
password_strength_checker(password)

def event_visitor_counter():
    number_of_visitor=int(input("Enter the number of visitors:"))
    def register_visitor(visitor_id):
        visitor_name=input("Enter visitor name: ")
        visitor_age=int(input("Enter visitor age: "))
        print(f"Welcome {visitor_name}, your visitor number is {visitor_id}")
        
    for visitor in range(1,number_of_visitor+1):
        register_visitor(visitor)
    print("Total munber of visitors are: ",number_of_visitor)

event_visitor_counter()
'''
def bank_account_management():
    balance=1000
    def deposit(amount):
        nonlocal balance
        balance+=amount
        print(f"After Deplosting: {balance}")

    def withdraw(amount):
        nonlocal balance
        if amount<=balance:
            balance-=amount
            print(f"New Balance: {balance}")
        else:
            print("Insufficient Balance")
    while True:
        choice=int(input("!.Deposit, 2.Withdraw, 3.Check balance, 4.Exit: \n"))
        if choice==1:
            amount_to_deposit=int(input("Enter Amount: "))
            deposit(amount_to_deposit)
        elif choice==2:
            amount_to_withdraw=int(input("Enter Amount: "))
            withdraw(amount_to_withdraw)
        elif choice==3:
            print(f"Your Balance is {balance}")
        elif choice==4:
            break
        else:
            print("Wrong Input! Choose from 1,2,3,4")

bank_account_management()