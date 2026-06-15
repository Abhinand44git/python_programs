'''
for variable in sequence:
    code to be executed

using Range function
for variable in range(start,stop,skip):
    code to be executed

while condition:
    code to be executed
    updation
'''
'''
word=input("Enter a Word: ")
for letter in word:
    print(letter,end=" ")

for element in [1,2,3,4]:
    print(element)

for element in range(11):
    print(element)

for element in range(5,16):
    print(element)

for item in range(10,26,5):
    print(item)

for item in range(1,10,-1):#will not work 
    print(item)

for item in range(10,0,-1):
    print(item)

for item in range(17,3,-3):
    print(item)

number_from_user=int(input("Enter a Number: "))
for integer in range(1,11):
    #print(number_from_user,"*",integer,"=",number_from_user*integer)
    print(f"{integer} * {number_from_user} = {number_from_user*integer}")#printing using formating string

value=1
while value<=10:
    print(value)
    value+=1

value=1
iterations=(int(input("Enter the number of iterations:")))
sum=0
while value<=iterations:
    sum+=value
    value+=1
print(sum)
'''
'''
step 1: getting the last digit (ex:165%10=5)
step 2: remove the last digit(ex:165/10=16)
step 3: build the reversed number(reversed=0)
reverse*10+5

number= int(input("Enter the number to got reversed: "))
reverse=0
while number>0:
    remainder=number%10
    reverse=reverse*10+remainder
    number//=10
print(reverse)

number =165
165>0 is True
remainder = 165%10 is 5
reverse = 0*10+5 = 5
number = 165//10 = 16
still number 16 is greater than 0

number = 16
16>0 is true
remainder = 16%10 is 6
reverse = 5*10+6 = 56
number = 16//10 = 1

number=1
1>0 is true
remainder = 1%10 = 1
reverse = 56*10+1 = 561
number = 1//10 = 0
exit while
'''

'''
number of 9's from 1 to 100
count = 0
for number in range(1,101)
remainder = number%10
if remainder == 9
count+=1
'''
'''
count=0
for number in range(1,101):# 1,19,99
    temp=number
    while temp>0:
        digit= temp%10
        if digit == 9:
            count+=1
        temp//=10 # the number is changed to zero
print("Total Number of 9's: ",count)
'''
'''
number = 1
temp = 1
digit = 1%10 = 1
temp = 1//10=0

number = 19
temp = 19
digit = 19%10 = 9
count = 1
temp = 19//10 = 1
temp>0
digit = 1%10 = 1
temp = 1//10=0

number = 99
temp = 99
digit = 99%10 = 9
count =19
temp = 99//10= 9
temp>0
digit = 9%10 = 9
count = 20
temp = 9//10 = 0
'''