# Functional Programming 

# Without Functions 

# User One Wants To Calculate For Below Values 
num1 = 10
num2 = 5

# Math Arithmetic Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 50)

# User Two Wants To Calculate For Below Values 
num1 = 20
num2 = 5

# Math Arithmetic Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 50)

# User Three Wants To Calculate For Below Values 
num1 = 200
num2 = 50

# Math Arithmetic Operations 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 50)

# With Functions 
def math_ops():
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

# User One Wants To Calculate For Below Values 
num1 = 10
num2 = 5
math_ops()    
print("=" * 50)
# User Two Wants To Calculate For Below Values 
num1 = 20
num2 = 5
math_ops()    
print("=" * 50)
# User Three Wants To Calculate For Below Values 
num1 = 200
num2 = 50
math_ops()    
print("=" * 50)

# Functions With Parameters 
def math_ops(num1, num2): # num1 and num2 are Parameters
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    
# math_ops()  # TypeError: math_ops() missing 2 required positional arguments: 'num1' and 'num2'  
print("=" * 50)
# num = int(input("Enter Number: "))
math_ops(10,5) # User One Wants To Calculate For Below Values 
print("=" * 50)
math_ops(20,5) # User Two Wants To Calculate For Below Values 
print("=" * 50)
math_ops(200,50) # User Three Wants To Calculate For Below Values 
print("=" * 50)

# Process Data like gmail functionality 
# RAvi2KRIshNA --> ravi2krishna@gmail.com
def process_email_id(email_id):
    print('Processing Email.......')
    print(email_id.lower()+"@gmail.com")

process_email_id("RAvi2KRIshNA")

print("=" * 50)

# Positional Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")

employee_info("Hyderabad","Ravi","ravi@gmail.com")

print("=" * 50)

employee_info("Ravi","ravi@gmail.com","Hyderabad")

print("=" * 50)

# Keyword Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")
    
employee_info("Hyderabad","Ravi","ravi@gmail.com")

print("=" * 50)

employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")

print("=" * 50)

# Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    

employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com",org_name="IBM")

print("=" * 50)

employee_info(emp_location="Pune",emp_name="Krishna",emp_email="krishna@gmail.com",org_name="IBM")

print("=" * 50)

employee_info(emp_location="Bangalore",emp_name="John",emp_email="john@gmail.com",org_name="IBM")

print("=" * 50)

# Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name="IBM"):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    

employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi@gmail.com")

print("=" * 50)

employee_info(emp_location="Pune",emp_name="Krishna",emp_email="krishna@gmail.com")

print("=" * 50)

employee_info(emp_location="Bangalore",emp_name="John",emp_email="john@gmail.com",org_name="TCS")

print("=" * 50)

# Default Arguments
# def employee_info(emp_name,emp_email,emp_location,org_name="IBM",emp_mobile):
#     print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")


def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="IBM",):
    print(f"Hi {emp_name} your email is {emp_email}, and mobile is {emp_mobile} and working for {org_name} at location {emp_location}")

employee_info(emp_location="Pune",emp_name="Krishna",emp_email="krishna@gmail.com",emp_mobile=898080)

print("=" * 50)

employee_info(emp_location="Bangalore",emp_name="John",emp_email="john@gmail.com",org_name="TCS",emp_mobile=9090900)

print("=" * 50)

# Without Arbitrary Positional Arguments
def add_numbers_one(n1):
    print(n1)
    
def add_numbers_two(n1,n2):
    print(n1 + n2)
    
def add_numbers_six(n1,n2,n3,n4,n5,n6):
    print(n1 + n2 + n3 + n4 + n5 + n6)
    

add_numbers_one(5)
print("=" * 50)
add_numbers_two(5,10)
print("=" * 50)
# add_numbers_two(5,10,30)
# print("=" * 50)

# With Arbitrary Positional Arguments
def add_numbers(*numbers):
    print(numbers)
    
add_numbers(5)
print("=" * 50)
add_numbers(5,10)
print("=" * 50)
add_numbers(5,10,20,30)
print("=" * 50)

# With Arbitrary Positional Arguments
def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num 
    print(f"Total Sum is {total}")
    
add_numbers(5)
print("=" * 50)
add_numbers(5,10)
print("=" * 50)
add_numbers(5,10,20,30)
print("=" * 50)

# Arbitrary Keyword Arguments
def profile(**info):
    print(info)

profile(fname="Ravi")    
print("=" * 50)

profile(fname="John",lname="Doe",mobile=909080800)    
print("=" * 50)
