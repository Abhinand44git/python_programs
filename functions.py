'''
def function_name(parameters):
    code to be executed
'''
'''
def greeting(user_name,user_age):
    print(f"Welcome {user_name}, you are {user_age} years old.")

user_name=input("Enter Name: ")
user_age=int(input("Enter Age: "))
greeting(user_name,user_age)

def addition(num1,num2):
        return num1+num2

num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
print(addition(num1,num2)) #result=addition(num1,num2) 
#print(result)

def welcome():
    print("Welcome Abhinand")

welcome()

def book_ticket(movie_name,customer_name,seats,ticket_price):
    total=seats*ticket_price
    return f"{customer_name} booked {seats} tickets for {movie_name}. Total Amount: {total}"

print(book_ticket("Aladdin","Ramesh",5,400))
#print(book_ticket(3,200,"Gina","Drishyam")) postional argument mix-up

print("\nKeyword Arguments")
def customer_details(customer_name,customer_age,city):
    print(f"Customer Name: {customer_name}\nCustomer Age: {customer_age}\nCustomer City: {city}")


customer_details(customer_age=27,city="Ernakulam",customer_name="Tom")

print("\nDefault Arguments")
def booking_status(status="Confirmed",screen="Screen1",customer_name="Peter"):
    print(f"{customer_name}'s bookin status : {status}")
    print(f"Screen Allocated : {screen}")

booking_status(customer_name="James")
booking_status(customer_name="Amy","Pending")
booking_status(customer_name="Ben","Pending","Screen3")

print("Multiple Arguments")
def calculate_bill(*ticket_prices):
    print(f"Ticket Prices: {ticket_prices}")
    print("Total Bill:",sum(ticket_prices))

calculate_bill(90,450,90,765)#difference between kwargs and args
print("\nMultiple Keyword Arguments")
'''
def passenger_info(**details):
    print("Passenger Infomation")
    for key,value in details.items():
        print(f"{key} : {value}")
    
passenger_info(
    passenger_name="Kiran",
    seats=3,
    payment_status="Paid",
    destination="Kasargod"
)
'''
print("Built-in Fuctions")
print(len("Argentina"))
print(sum([45,35,800,986]))
print(max(45,35,800,986))
print(min(45,35,800,986))
print(sorted([45,35,800,986]))
print(sorted([45,35,800,986],reverse=True))

language=["Malayalam","Hindi","English","Japanese"]
print(sorted(language))
print(sorted(language,reverse=True))

print(sorted(language,key=len,reverse=True))

#check enumerate in a function

'''
'''
LEGB rule = LOCAL ENCLOSING GLOBAL BUILT-IN

def student_details():
    name="Abhinand"#local variable
    print("Student Name: ",name)


student_details()
college_name="John Cox Memorial CSI Institute of Technology"#global variable
def display():
    print("College Name: ",college_name)
display()

def department():
    department_name="Computer Science Enginnering" #enclosing variable
    def student():
        print("Department: ",department_name)
    student()

department()

# global variable =tax,fucntion=shopping, enclosing =disocunt, inner=amount, inner_function=bill

tax=50#global variable
def shopping():
    discount=100#enclosing variable
    def bill():
        amount=900#local variable
        total_amount=amount-discount+tax
        print("Total Bill: ",total_amount)
    bill()

shopping()

print("\n Recursive Fuctions")
def factorial(number):
    if number==1:
        return 1
    else:
        return number * factorial(number-1)

num=int(input("Enter a Number: "))
print(f"Factorial of {num} is {factorial(num)}")

5 *factorial(4)
4 *factorial(3)
3 *factorial(2)
2 *factorial(1)

2*1=2 factorial(1)
3*2=6 factorial(2)
4*6=24 factorial(3)
5*24=120 factorial(4)
factorial(5)
=5*Factorial(4)
=5 * 4 * factorial(3)
=5 * 4 *3 * factorial(2)
=5 * 4 * 3 * 2 *factorial(1)
=5 * 4 * 3 * 2 * 1 

#direct way for recursion using for
number=int(input("Enter a number: "))
factorial=1
for num in range(1,number+1):
    factorial*=num

print(f"Factorial of {number} is {factorial}")



def add(num1,num2):
    return num1+num2
print(add(3,4))

#syntax lambda argements:expression
add= lambda a,b:a+b
print(add(8,6))

square=lambda num:num*num
print(square(4))

largest= lambda a,b: a if a>b else b
print(largest(15,6))
'''