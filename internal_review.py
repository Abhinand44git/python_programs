# Exam Result Processing System
def grade(total):
    if total/5>90:
        return "S"
    elif total/5>80:
        return "A"
    elif total/5>80:
        return "B"
    elif total/5>80:
        return "C"
    elif total/5>80:
        return "D"
    else:
        return "Fail"

def search_student(name):
    if name in student_names:
        print("Student present")
    else:
        print("not found")
        


subject_list=("English","Maths","HIndi","Science","Social Science")
student_names=["Anand","Grishma","Mayeen","Tania","Umesh"]
grades={"S","A","B","C","D","F"}
total_marks_list=[]
total_marks=0
for student in student_names:
    for subject_marks in range(1,6):
        student_marks=int(input(f"Enter Student marks in 5 subjects out of 100: "))
        total_marks+=student_marks
    print("Total marks: ",total_marks)
    print("Average_marks: ",total_marks/5)
    print("Grade:",grade(total_marks))
    total_marks_list.append(total_marks)
    
print(total_marks_list>sorted)
results={
    "Anand's marks": "Pass",
    "Grishma's marks": "Pass",
    "Mayeen's marks": "Fail",
    "Tania's marks": "Pass",
    "Umesh's marks": "Pass",
    }
