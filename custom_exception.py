'''
class CustomException(Exception):
    pass
def check_number(num):
    if num<0:
        raise CustomException("Not allowed negative numbers")
    return num
try:
    result=check_number(7)
except CustomException as e:
    print(e)
else:
    print(result)
'''
class NameTooShortError(Exception):
    pass
name=input("Enter User Name: ")
try:
    if len(name)<8:
        raise NameTooShortError("Name must be grater than 8 letters")
except NameTooShortError as n:
    print(n)
else:
    print(name)