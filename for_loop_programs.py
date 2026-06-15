'''
employee1_salary=int(input("Enter Salary of Employee 1: "))
employee2_salary=int(input("Enter Salary of Employee 2: "))
employee3_salary=int(input("Enter Salary of Employee 3: "))
employee4_salary=int(input("Enter Salary of Employee 4: "))
employee5_salary=int(input("Enter Salary of Employee 5: "))
total_salary=0
employees_salary_list=[employee1_salary,employee2_salary,employee3_salary,employee4_salary,employee5_salary]
for employee_salary in employees_salary_list:
    total_salary+=employee_salary
print("Total Salary Expenditure: ",total_salary)

count_present=0
count_absent=0
for number_of_students in range(1,11):
    status=input(f"Student {number_of_students} Attendance: ")
    if status =="P":
        count_present+=1
    elif status=="A":
        count_absent+=1
    else:
        print("Wrong Input!! Retry Again.")
print("Total Present Students: ",count_present)
print("Total Absent Students: ",count_absent)

total_bill_Amount=0
for items in range(1,6):
    item_price=int(input(f"Item {items} Price: "))
    total_bill_Amount+=item_price

print("Total Bill Amount: ",total_bill_Amount)

total_runs_scored=0
for runs in range(1,7):
    runs_ball=int(input(f"Ball {runs} Runs: "))
    total_runs_scored+=runs_ball

print("Total Runs Scored: ",total_runs_scored)

total_books_in_library=0
for books in range(1,8):
    section_books_count=int(input(f"Section {books} Books: "))
    total_books_in_library+=section_books_count

print("Total Books In Library: ",total_books_in_library)

total_marks=0
for mark in range(1,6):
    subject_marks=int(input(f"Subject {mark} Marks: "))
    total_marks+=subject_marks

print("Total Marks: ",total_marks)
print("Average Marks: ",total_marks/5)

highest_temperature=0
for temperature in range(1,8):
    day_temperature=int(input(f"Day {temperature} Temperature: "))
    if day_temperature>highest_temperature:
        highest_temperature=day_temperature

print(f"Highest Temperature {highest_temperature} Degree Celsius",)

total_collection=0
for recharge_amount in range(1,11):
    customer_recharge=int(input(f"Customer {recharge_amount} Rehcarge: "))
    total_collection+=customer_recharge

print("Total Collection: ",total_collection)

total_water_consumed=0
for day_number in range(1,8):
    day_consumption=int(input(f"Day {day_number} onsumption: "))
    total_water_consumed+=day_consumption

print("Total Water Consumption: ",total_water_consumed)
'''
total_annual_production=0
for month_production in range(1,13):
    monthly_production=int(input(f"Month {month_production} Production: "))
    total_annual_production+=monthly_production

print(f"Total Annual Amount: {total_annual_production} units",)