import os

original_file="crud_operation.txt"

with open(original_file,"w") as file:
    for i in range(1,201):
        file.write(f"Entry {i}: This is line{i}\n")
    print("File created with 200 entries")

with open(original_file,"r") as file:
    print("Reading file contents: ")
    #print(file.readline)
    #print(file.readline)
    lines=file.realines()
    for i in lines[:60]:
        print(i.strip())

print(lines[3])
lines[3]="Entry 4: This line is updated.\n"
print(f"After updation: {lines[3]}")

lines=[line for line in lines if "Entry 10" not in line]
for i in range(70,120):
    print(lines[i].strip())

updated_file="crud_operation_updated.txt"
with open (updated_file,"w") as file:
    file.writelines(lines)
    for i in range(201,301):
        file.write(f"Entry {i}: THis is line{i}\n")
    print(f"Updated file saced as {updated_file}")
with open(updated_file,"r") as file:
    print(file.read())

with open(original_file,"r") as file:
    print(file.read())