'''
print("Arithematic Operators")
price_per_book=500
quantity=25
total_price= price_per_book*quantity
average_price=total_price/quantity
extra_charge=50
final_price= total_price+extra_charge
discount=25
final_price-=discount
remainder=final_price%quantity
floor_division=final_price//7
squared_value=final_price**2


print("Price of one book is: ",price_per_book)
print("Quantity of books: ",quantity)
print("Total_price: ", total_price)
print("Average amount of the book: ", average_price)
print("Final Price: ",final_price)
print("Discount: ",discount)
print("Remainder: ",remainder)
print("floor division: ",floor_division)
print("Squared value: ",squared_value)

print("Assignment Operators")
score=100
score+=50
print(score)
score-=20
print(score)
score*=2
print(score)


print("Final Score: ",score)

print("Logical Operators")
username="abhinand"
password="qwerty123"
enter_username=input("Enter your username: ")
enter_password=input("Enter your password: ")
if enter_username==username and enter_password==password:
    print("Login Successful")
else:
    print("Invalid Login")


day=input("Enter a Day: ")
if day=="Saturday" or day=="Sunday":
    print("Holiday")
else:
    print("Working Day")

logged_in=False
if not logged_in:
    print("Please Log In")
else:
    print("Login Succesful! Welcome User!!!")

print("Membership Operator")
movies=["Transformers","Avengers","The Intern"]
movie=input("Enter Your Favourite Movie:")
if movie in movies:
    print("Movie Available")
else:
    ("Movie is not Available")

employees=["Akash","Reshma","Vimal"]
employee_name=input("Enter employee name: ")
if employee_name not in employees:
    print("Access Denied.")
else:
    print("Access Granted.")

print("Identity Operator")
value1=30
value2=30
print(value1 is value2)
print(value1==value2)

list1=[10,20,30,40]
list2=[10,25,30,45]
print(list1 is list2)
print(list2==list1)

print(list1[0] is list2[0])

languages=[10,30,50]
selected_language=languages[0]
print(selected_language is languages[0])
print(selected_language == 10)


list3=[10,20,30]
list4=[10,20,30]
print(list3 is list4)
print(list3==list4)
list5=list3

print(list5 is list3)

print("Bitwise Operators")
num3=5 #0101
num4=3 #0011
print(bin(num3))
print(bin(num4))
print(bin(num3 & num4))
print(bin(num3 | num4))
print(bin(num3^num4))
print(bin(~num3))
print(num3<<1)
print(num3>>2)
'''