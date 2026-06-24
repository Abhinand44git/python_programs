'''
number=int(input("Enter a number: "))
if number <=1:
    print("Not a prime number")
else:
    is_prime=True
for num in range(2,number):
    if number%num==0:
        is_prime=False
        break
if is_prime:
    print("Is a Prime Number")
else:
    print("Not a Prime Number")
    #tryout this program using count and floor division

#Fibonacci Series
num=int(input("Enter the number of terms: "))
a=0
b=1
for i in range(num):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

#palindrome
num=int(input("Enter a Number: "))
initial=num
rev=0

while num>0:
    temp=num%10
    rev=rev*10+temp
    num=num//10
    
if initial==rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome number")


#count of a number
count=0
user_value=int(input("Enter the number: "))
temp=abs(user_value)
if temp==0:
    count=1
else:
    while temp>0:
        count+=1
        temp=temp//10

print("Number of digits",count)
#try to do reverse of a number

num=int(input("Enter a Number: "))
sum_digits=0
temp=abs(num)
while temp>0:
    digit=temp%10
    sum_digits+=digit
    temp=temp//10

print("Sum of digits",sum_digits)


num=int(input("Enter a Number: "))
prod_number=1
temp=abs(num)
while temp>0:
    digit=temp%10
    prod_number*=digit
    temp=temp//10
print("Product of digits: ",prod_number)

pin=4562
balance=75000
attempts=0
while attempts!=3:
    pin_num=int(input("Enter a Pin: "))
    if pin_num==pin:
        print("Pin Verfied")
        while True:
            print("\n1. Balance Check")
            print("2. Withdrawal")
            print("3. Deposit cash")
            print("4. exit")
            choice=int(input("Enter a Choice: "))
            if choice == 1:
                print("Balance is: ",balance)
            elif choice == 3:
                deposit_amount=int(input("Enter Amount to be Deposited: "))
                current_balance=balance+deposit_amount
                print("New Balance: ",current_balance)
            elif choice == 2:
                withdrwal_amount=int(input("Enter amount to be withdrawn: "))
                if withdrwal_amount>balance:
                    print("Insufficient Balance")
                else:
                    balance-=withdrwal_amount
                    print("Current Balance: ",balance)
            elif choice== 4:
                break
            else:
                print("Wrong Input! Try Again")
        break
    else:
        print("Incorrect Pin")
        attempts+=1
else:
    print("Account Blocked")

total_seats=10
available_seats=abs(total_seats)
while True:
    if available_seats==0:
        break
    else:
        print("1. Available seats")
        print("2. Book Tickets")
        print("3. Exit")
        choice=int(input("Enter your choice between 1 and 3: "))
        if choice==1:
            print(f"Seats Available: {available_seats}")
        elif choice == 2:
            booking_seats=int(input("Enter the number of seats user wants: "))
            available_seats-=booking_seats
            print("Booking Successful")
            print(f"Remaining Seats : {available_seats}")
        elif choice == 3:
            break
        else:
            print("Wrong Input")
print("Booking closed")

start_value=int(input("Enter Start Value: "))
end_value=int(input("Enter End Value:  "))
for item in range(start_value,end_value+1):
    if item%3==0 and item%5==0:
        print("FizBuzz")
    elif item%3==0:
        print("Fiz")
    elif item%5==0:
        print("Buzz")
    else:
        print(item)

#find the largest and smallest number in the list
numbers_list=[]
number_of_items=int(input("Enter number of elements to be inserted: "))
for items in range(number_of_items):
    num=int(input(f"Enter item {items+1}:"))
    numbers_list.append(num)
largest_num=numbers_list[0]
smallest_num=numbers_list[0]
for num in numbers_list:
    if num>largest_num:
        largest_num=num
    if num<smallest_num:
        smallest_num=num
print("Largest Number in the list is: ",largest_num)
print("Smallest Number in the list is: ",smallest_num)

# seperate positive and negative number from list

numbers_list=[]
number_of_items=int(input("Enter the number of elements to be inserted"))

count=0
numbers=tuple(map(int,input("Enter the numbers to be inserted: ").split()))
number=int(input("Enter the number to count: "))
for items in numbers:
    if items == number:
        count+=1
print("Tuple elements are: ",numbers)
print(f"Occurence of {number} in tuple is {count}")

combination=tuple(map(int,input("Enter the numbers to be inserted: ").split()))
number=int(input("Enter the Target sum: "))
for items in combination:
    for element in combination:
        if items+element==number:
            combines=(items,element)
    if items==number/2+1:
        break
    print(combines)


data={"a":1,"b":2,"c":3}
reversed_data={}
while data:
    key,value = data.popitem()
    reversed_data[key]= value
print(reversed_data)

data={"a":1,"b":2,"c":3}
reversed_data={}
keys=list(data.keys())
for key in keys[::-1]:
    reversed_data[key]=data[key]
print(reversed_data)
'''
print("Linear Search")
user_marks=list(map(int,input("Enter the Elements To be Inserted: ").split()))
search_element=int(input("Enter the Element of Search: "))
for i in range(len(user_marks)):
    if user_marks[i]==search_element:
        print(f"Element found at position {i+1}")
        break
else:
    print("Element not found")