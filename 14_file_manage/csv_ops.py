# Work With CSV Files / Data 

# Read Data From CSV File 
with open("14_file_manage/students.csv","r") as file_data:
    print("Reading File")
    print(file_data.read())
    
print("=" * 50)

# Customer Requirement: Fetch Me All Students From Hyderabad 