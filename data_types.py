#student_name=input("Enter the student name: ")
#student_id=int(input("Enter the student id: "))
#student_mark=float(input("Enter the student mark: "))
#is_present=bool(input("Is present or not?(T/F): "))
#languages_known=input("Enter the languages known: ").split(",")

#print("The student name is ",student_name)
#print("The student id is ",student_id)
#print("The student mark is ",student_mark)
#print("The student is present or not ",is_present)
#print("Language known by the student are: ",languages_known)

#print(type(student_name))
#print(type(student_id))
#print(type(student_mark))
#print(type(is_present))
#print(type(languages_known))

num1=10
num2=10

print(id(num1))
print(id(num2))

list1=[5,8,9,0]
list2=[5]
print(id(list1))
print(id(list2))

print(isinstance(list1[2],int))
print(isinstance(num1,int))
print(isinstance([100,1000],list))