'''
store_data=open("newfile.txt","w")
store_data.write("Welcome to python programming")
print(store_data)
store_data.close()

append_data=open("newfile.txt","a")
append_data.write("\nPython is an interpreted language")
print(append_data)
append_data.close()

read_data=open("newfile.txt","r")
print(read_data.read())
read_data.close()


#using Context Manager
with open("newfile.txt","r") as f:
    print("Current Position: ",f.tell())
    f.read(6)
    print("After Read Position: ",f.tell())
    f.seek(4)
    print("After Seek: ",f.tell())
    print(f.read())


with open("car.jpg","rb") as data:
    image_read=data.read()
    print(image_read)
#tryout pip install Pillow and use its functions,use pillow to import image

tech=open("delete_file.txt","x")
print(tech)
tech.close()

file_path="delete_file.txt"
import os
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} deleted successfully")
else:
    print("File does not exist.")
'''
#serialization and deserialization
import pickle

data={
    "students" : ["Aria","Rajesh","Vimal"],
    "marks" : (78,83,92),
    "subject" : {"Maths","English","Science"}
    }
'''
#serialzation- Saving Data to File
with open("user_details.pkl","wb") as f:
    pickle.dump(data,f)
    print("Data is serialized into user details: ",data)

with open("user_details.pkl","rb") as file:
    loaded_data=pickle.load(file)
    print("Data read from the pickle: ",loaded_data)

'''
#serialization: saving data in memory
dump_data=pickle.dumps(data)
print("Data is Serialized to Bytes: ",dump_data)

load_data=pickle.loads(dump_data)
print("Data is Deserialized to objects: ",load_data)
#try out json module
