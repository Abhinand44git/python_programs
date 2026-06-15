'''
if condition:
    code to be executed
elif condition:
    code to be executed
else:
    code to be executed
'''
'''
number1=int(input("Enter a number: "))
if number1>0:
    print("Positive number")
else:
    print("Negative number")
'''
'''
vowel_check=input("Enter a character: ")
if vowel_check=='a' or vowel_check=='A':
    print("Character is a vowel")
elif vowel_check=='e' or vowel_check=='E':
    print("Character is a vowel")
elif vowel_check=='i' or vowel_check=='I':
    print("Character is a vowel")
elif vowel_check=='o' or vowel_check=='O':
    print("Character is a vowel")
elif vowel_check=='u' or vowel_check=='U':
    print("Character is a vowel")
else:
    print("Character is a consonant")ineffcient


vowel_checker=input("Enter a Character: ")
if vowel_checker in 'aeiouAEIOU':
    print("Character is a vowel.")
else:
    print("Character is a consonant.")


odd_even=int(input("Enter a number: "))
if odd_even%2 ==0:
    print("Number is Even.")
else:
    print("Number is Odd.")

age=int(input("Enter An Age: "))
if age<=13:
    print("Individual is a Child")
elif age<18:
    print("Individual is a Teenager")
elif age<60:
    print("Individual is a Adult")
else:
    print("Individual is a Senior Citizen")

hetero_number=int(input("Enter a Number: "))
if hetero_number>0:
    if hetero_number%2==0:
        print("The Number is a Positive and Even")
    else:
        print("The Number is a Positive and Odd")
else:
    print("Number is Negative")

three_digit_number=int(input("Enter a Number: "))
if three_digit_number<1000 and three_digit_number>99:#99>three_digit_number<1000
    print("It is a 3 Digit Number")
elif three_digit_number<100:
    print("It is a 2 Digit Number")
else:
    print("It is a 4 digit or Higher Digit Number")

#A Simple ATM Program

balance_amount=50000
withdrawal_amount=int(input("Enter an Amount for Withdrawal: "))
if withdrawal_amount<=balance_amount:
    print("Transaction Status:Successful")
else:
    print("Transaction Status:Failed \nInsufficient Balance")
'''
