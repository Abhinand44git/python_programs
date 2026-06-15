'''
pin_number=int(input("Enter the PIN Number: "))
pin_value=1234
if pin_number==pin_value:
    withdrawal_amount=float(input("Withdrawal Amount: "))
    account_balance=65000
    if withdrawal_amount<=account_balance:
        print("Withdrwal Successful")
        remaining_balance=account_balance
        remaining_balance-=withdrawal_amount
        print("Remaining Balance: ",remaining_balance)
    else:
        print("Insufficient Balance")

purchase_amount=float(input("Enter Purchase amount: "))
premium_member=input("Premium Member(yes/no): ")
if purchase_amount>10000:
    purchase_amount-=500
    if premium_member=="yes":
        discount_applied=25/100
        print("Discount Applied: ",discount_applied*100,"%")
        final_bill_amount=purchase_amount
        discount_amount=final_bill_amount*25/100
        print("Final Bill Amount: ",final_bill_amount-discount_amount)

higher_secondary_percentage=int(input("Enter Higher Secodary Pecentage: "))
mathematics_percentage=int(input("Enter Mathematics Pecentage: "))
enterance_exam_score=int(input("Enter Enterance Exam Score: "))

if higher_secondary_percentage>60 and mathematics_percentage>60 and enterance_exam_score>60:
    print("Admission Status: Eligible")
    print("Suggested Course: Computer Science")

age=int(input("Enter Age: "))
salary=float(input("Enter Salary: "))
credit_Score=int(input("Enter Credit Score: "))
loan_status=input("Existing Loan(yes/no): ")

if age>18 and salary>35000 and credit_Score>600 and loan_status =="no":
    print("Loan Status: Approved")
else:
    print("Loan Status: Disapproved")

patient_age=int(input("Enter Age: "))
condition_status=input("Enter Condition(critical/severe/mild): ")
if patient_age>0 and condition_status=="critical":
    print("Priority Category: High Priority")
elif patient_age>0 and condition_status=="severe":
    print("Priority Category: High Priority")
else:
    print("Priority Category: Low Priority")

years_of_service=int(input("Enter Years of Service: "))
performance_rating=input("Enter Performance Rating: ")
attendance_percentage=int(input("Enter Attendance Percentage: "))
base_salary=60000
if years_of_service>5 and performance_rating=="Excellent" and attendance_percentage>=95:
    bonus_percentage=20
    print("Bonus Percentage:",bonus_percentage,"%")
elif years_of_service<=5 and performance_rating=="Excellent" or performance_rating=="Good" and attendance_percentage<95:
    bonus_percentage=10
    print("Bonus Percentage:",bonus_percentage,"%")
elif years_of_service<=5 and performance_rating=="Average" and attendance_percentage<85:
    bonus_percentage=5
    print("Bonus Percentage:",bonus_percentage,"%")
else:
    print("Employee Is Not Eligible For Bonus")

bonus_amount=base_salary*(bonus_percentage/100)
print("Bonus Amount: ", bonus_amount)

helmet_Worn=input("Helmet Worn(yes/no): ")
seatbelt_used=input("Seatbely Used(yes/no): ")
speed_limit_violated=input("Speed Limit Violated(yes/no): ")
valid_license=input("Valid License(yes/no): ")
total_fine=0
if helmet_Worn=="no":
    total_fine+=500
if seatbelt_used=="no":
    total_fine+=1500
if speed_limit_violated=="yes":
    total_fine+=1000
if valid_license=="no":
    total_fine+=5000
print("Total Fine: ",total_fine)

age_for_movie_ticket=int(input("Enter Age: "))
seat_type=input("Seat Type(Normal/Premium): ")
day_type=input("Day Type(Weekday/Weekend): ")
student=input("Student(yes/no): ")
final_price=0
if seat_type=="Premium":
    final_price=400
    if day_type=="Weekend":
        final_price+=200
else:
    final_price=250
    if day_type=="Weekend":
        final_price+=100
if age_for_movie_ticket<=12 or age_for_movie_ticket>=65:
    final_price=final_price*0.80
if student=="yes":
    final_price=final_price*0.66
print("Final Ticket Cost: ",final_price)

family_income=float(input("Enter Family Income: "))
academic_percentage=int(input("Enter Academic Percentage: "))
attendance_percentage=int(input("Enter Attendance Percentage: "))
if family_income<=200000 and academic_percentage>=90 and attendance_percentage>=95:
    print("Scholarship Status: Full Scholarship")
elif family_income<=400000 and academic_percentage>=80 and attendance_percentage>=90:
    print("Scholarship Status: Partial Scholarship")
elif family_income<=200000 and academic_percentage>=70:
    print("Scholarship Status: Basic Scholarship")
else:
    print("Scholarship Status: Not Eligible")
'''
print("Enter Marks In 5 Subjects: ")
subject1=int(input())
subject2=int(input())
subject3=int(input())
subject4=int(input())
subject5=int(input())
total_marks=subject1+subject2+subject3+subject4+subject5
mark_percentage= total_marks/5
print("Total Marks: ",total_marks)
print("Percentage: ",mark_percentage)
if mark_percentage>=90:
    print("Grade: S")
elif mark_percentage>=80:
    print("Grade: A")
elif mark_percentage>=70:
    print("Grade: B")
elif mark_percentage>=60:
    print("Grade: C")
elif mark_percentage>=50:
    print("Grade: D")
elif mark_percentage>40:
    print("Grade: P")
else:
    print("Grade: F")

if subject1>=40 and subject2>=40 and subject3>=40 and subject4>=40 and subject5>=40:
    print("Result:Pass")
    print("Promotion Status: Eligible")
else:
    print("Result:Fail")
    print("Promotion Status: Not Eligible")
