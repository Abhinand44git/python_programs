'''
username="Abhinand"
# 0  1  2  3  4  5  6  7
# A  b  h  i  n  a  n  d(positive indexing)
#-8 -7 -6 -5 -4 -3 -2 -1(negative indexing)
print(f"Username: {username}")
print(username[2])
print(username[-4])
print(username[8])

data="Python is a Programming Language"
print(data[1:8])
print(data[0:14])
print(data[-33:-6])
print(data[-33:-8:2])
print(data[:-6])
print(data[6:])
print(data[::3])
print(data[::-2])

scooty="Scooty model is Grazia and Company is Honda."
print(scooty.upper())
print(scooty.lower())
print(scooty.capitalize())
print(scooty.title())
print(scooty.startswith("Sco"))
print(scooty.endswith("da."))
#scooty[3]= "a"
#print(scooty)
#print(scooty.replace("model is Grazia and Company is Honda","name is Honda Grazia"))
print(id(scooty))
uppercase=scooty.upper()
print(id(uppercase))

user_data=["Abhinand",22,"Pottayil"]

user_data.insert(2,"JIT")
user_data.append(2026)
user_data.extend("python")

user_data.append(["English","Malayalam","Hindi"])
user_data.extend(["C","HTML","SQL"])

user_data.remove("Abhinand")
user_data.pop(2)
user_data.reverse()
user_data.sort()

print(user_data)#if 
#print(user_data[11])
#print(user_data[12][0])

tuple1=(10,20,30,40)
print(tuple1)
nested_tuple=((1,2,3,4,5),"Aalvin","Abhinand","Abhiram","Abhishek","Adhishlal")
print(nested_tuple) #tryout indexing and slicing
# tryout immutability

person=("Krishna",26,"Kattakada")
name,age,place=person
print(name)
print(age)
print(place)

number=(10,20,30,40,50)
a,b,*c=number
print(a)
print(b)
print(c)
d,*e,f=number
print(d)
print(e)
print(f)

numb_repeated=(2,4,2,5,6,7,2,9,7,9,4,3,2)
print(len(numb_repeated))
print(numb_repeated.count(2))
print(numb_repeated.index(3))
print(numb_repeated[3])

user_data=input("Enter a String: ")
count=0
for char in user_data:
    count+=1

print(count)

user_input=input("Enter a word: ")
count=0
for char in user_input:
    if user_input.count(char)==1:
        print("First least repeating character is: ",char)
        break
    else:
        print("There is no non_repeating character")# find second non repeating character then third non repeating and index of these non repeating character 

student1={"English","Hindi","Malayalam"}
student2={"English","Hindi","Python"}
student3={"Python","Urdu",}
student1.add("C")
#student1.add("Kannada","Marathi")

#student1.update(["C++","Java","Malayalam"])
#student1.pop()
#student1.discard("English")
#student1.remove("Javascript")
#student1.discard("Javascript")
print(student1.union(student2))
print(student1|student2)
print(student1.intersection(student2))
print(student1&student2)
print(student1.difference(student2))
print(student3-student2)
print(student1.isdisjoint(student3))#check subset or superset 

fs1 = frozenset("Abhinand")
fs2 = frozenset([22,33,44,55])
fs3 = frozenset(("Andhra","Mughlai","Travancore"))
print(fs1)
print(fs2)
print(fs3)

student = {
    "Name" : "Abhinand",
    "Age" : 22,
    "Place" : "Pottayil"
    }

print(student["Name"])
info1 = dict(city = "Trivandum",state ="Kerala")
print(info1.keys())
print(info1.values())
print(info1)
print(student.get("Marks"))
student["Marks"] = 47#tryout update for multiple insertions
student.pop("Age")
del student["Place"]
print(student)
'''
employee={
    "emp1": {
        "name" : "Abhinand",
        "age": 22
    },
    "emp2" :{
        "name":"Ram",
        "age":25
    },
    "emp3" :{
        "name":"Krishna",
        "age":28
    },
    "emp4" :{
        "name":"Vidhya",
        "age":32
    }
}
print(employee["emp3"]["age"])