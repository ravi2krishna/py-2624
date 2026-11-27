# File Management With Python

# Syntax - 1
# file = open("file_path","mode")

# file_data = open("file.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
# print(file_data)

file_data = open("14_file_manage/file.txt","r") 
print(file_data)
print(file_data.read())

print(file_data.closed) # False --> Still Open 
file_data.close() # Flush and close the IO object.
print(file_data.closed) # True --> File Closed 

print("=" * 50)

# Syntax - 2 (Recommended)

# with open("file_path","mode") as alias_name:
#     statement 

with open("14_file_manage/file.txt","r") as file_data:
    print(file_data)
    print(file_data.read())
print(file_data.closed) # True --> File Closed Automatically 
    
print("=" * 50)

# Create File & Write Data 
with open("14_file_manage/write.txt","w") as file_data:
    print("File Created")
    file_data.write("This File Has Been Created Using Python")

print("=" * 50)
    
# Read Data From File 
with open("14_file_manage/write.txt","r") as file_data:
    print("Reading Data From File")
    print(file_data.read())

print("=" * 50)

# Update Data To File 
with open("14_file_manage/write.txt","w") as file_data:
    print("File Updated")
    file_data.write("This File Has Been Created Using Python - Updated")
    
print("=" * 50)

# # Delete File 
# file_path = "14_file_manage/write.txt"
# os.remove(file_path) # NameError: name 'os' is not defined. Did you forget to import 'os'?

# Delete File 
import os 
file_path = "14_file_manage/write.txt"
print("Removing File")
os.remove(file_path)


# # Create Folder
# folder_path = "14_file_manage/students_data"
# print("Creating Folder")
# os.mkdir(folder_path) # FileExistsError: [Errno 17] File exists: '14_file_manage/students_data'

# Create Folder
folder_path = "14_file_manage/students_data"
print("Creating Folder")
if not os.path.exists(folder_path):
    os.mkdir(folder_path) 

# Delete Folder
folder_path = "14_file_manage/students_data"
print("Deleting Folder")
os.rmdir(folder_path)