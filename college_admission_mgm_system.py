student_names=[]
available_courses=("CSE","CE","EEE","ME","AIML")
unique_cities=set()
student_details={}

def collect_student_info():
    total_marks=0
    number_of_students=10
    for student in range(1,number_of_students+1):
        name=input("Enter Student Name: ")
        age=int(input("Enter Student Age: "))
        course=input("Enter the Course Name: ")
        if course not in available_courses:
            print("Invalid course.")
            course="Unassigned"
        marks=int(input("Enter Student Marks: "))
        city_name=input("Enter City Name: ")

        student_details[student]={
            "Name": name,
            "Age" : age,
            "Course" : course,
            "Marks": marks
        }
        student_names.append(name)
        unique_cities.add(city_name)
        total_marks+=marks
    
    average_marks=total_marks/number_of_students
    return average_marks

def display_metrics(average_marks):
    print(f"Averge mark of admitted students are: {average_marks}")

    def get_marks(student):
        return student_details[student]["Marks"]

    topper=max(student_details, key=get_marks)
    lowest_scorer=min(student_details, key=get_marks)

    print(f"Topper={student_details[topper]['Name']}({student_details[topper]['Marks']} Marks)")
    print(f"Lowest Scorer={student_details[lowest_scorer]['Name']}({student_details[lowest_scorer]['Marks']} Marks)")
    print("\nStudents marked by Marks")
    sort_students= sorted(student_details.items(), key=lambda student_mark: student_mark[1]["Marks"], reverse=True)
    rank=1
    for student, data in sort_students:
        print(f"{rank}. {data['Name']}: {data['Marks']} Marks")
        rank+=1
    
    print("\nEligible Students(Mark>=75)")
    for student, data in student_details.items():
        if data["Marks"]>=75:
            print(f"{data['Name']}: Eligible")
        else: 
            print(f"{data['Name']}: Ineligible")

def search_student(name):
    if name in student_names:
        print(f"Student {name} is found in records")
    else:
        print(f"Student {name} record not found")

def show_admission():
    average=collect_student_info()

    display_metrics(average)

    search_query=input("\nEnter Student Name to Search: ")
    search_student(search_query)

show_admission()
