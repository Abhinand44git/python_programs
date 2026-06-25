'''
print("First statement")
print("Second Year")
print("Third Month")
print("Fourth Week")
try:
    value_1=10
    value_2=0
    value_3=value_1/value_2
    print(value_3)
except ZeroDivisionError:
    print("Denominator cannot be Zero")
print("Fifth Day")
print("Sixth hour of the day")

numerator=int(input("Enter the numerator: "))
denominator=int(input("Enter the denominator: "))
try:
    quotient=numerator/denominator
except ZeroDivisionError:
    print("Denominator Cannot be Zero")
else:
    print(quotient)

print("Type Error")
try:
    num1=15
    num2="25"
    add=num1+num2
    print(add)
except TypeError:
    print("String cannot be added with integer value")

print("Index Error")
appointment_id=[101,102,103,104]
try:
    print(appointment_id[8])
except IndexError:
    print("Index out of range")

print("Key error")
book_details={
    "book_id": 21,
    "book_name": "Chronicles of Narnia",
    "book_author": "Joseph Claude"
    }
try:
    print(book_details["ISBN no"])
except KeyError:
    print("Key not found")

try:
    with open("sample_file.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found in directory")

try:
    from math import square
except ImportError as e:
    print(e)

try:
    greet=int("hello")
except ValueError:
    print("Invalid Literal")

user_value="Welcome"
try:
    print(user_value.add())
except AttributeError as e:
    print(e)

try:
    print(person)
except NameError as r:
    print(r)

print("Multiple Exception")
try:
    greet=int("hello")
    from math import square   
except ValueError as f:
    print(f)
except ImportError as e:
    print(e)
#multiple Exception Another method

try:
    greet=int("hello")
    from math import square
except (ValueError, ImportError) as e:
    print(e)

numerator=int(input("Enter the numerator: "))
denominator=int(input("Enter the denominator: "))
try:
    quotient=numerator/denominator
    print(quotient)
except ZeroDivisionError as z:
    print(z)
finally:
    print("Executed Normally")
'''
