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

# Without return 
def add(a,b):
    a + b 

add(10,5)
print(add(10,5))
print("=" * 50)

# # Problem 
# def add(a,b):
#     print(a+b)
    
# # Function Composition
# def sub(c,d,e): # add c and d then minus e --> c + d - e (None - 5)
#     print(add(c,d) - e) # TypeError: unsupported operand type(s) for -: 'NoneType' and 'int' --> 

# sub(3,4,5) # 3 + 4 - 5 = 2
    
# print("=" * 50)

# Solution
def add(a,b):
    return a + b 

# Function Composition
def sub(c,d,e): # add c and d then minus e --> c + d - e 
    print(add(c,d) - e)
    
sub(3,4,5) # 3 + 4 - 5 = 2

print("=" * 50)

# return, make sure it's the last part of statement to be executed
def add(a,b):
    print("Calculation Started......")
    return a + b 
    print("Calculation Completed......") # Code is structurally unreachable

print(add(10,10))

print("=" * 50)

a = 50
a = 60
a = 70
print(a) # 70 

print("=" * 50)
     
# If you have multiple return statements, first return will be considered
def math_ops(a,b):
    return a + b 
    return a * b # Code is structurally unreachable
    return a / b # Code is structurally unreachable

print(math_ops(2,3))

print("=" * 50)

# multiple returns are present, and used with conditionals, you can control the flow 
def math_ops(a,b,operator):
    if operator == "+":
        return a + b 
    elif operator == "*":
        return a * b 
    elif operator == "/":
        return a / b
    else:
        return "Invalid Operator"
    
print(math_ops(20,5,"+"))
print(math_ops(20,5,"$"))
print(math_ops(20,5,"*"))

print("=" * 50)

# Local Scope 
def add():
    la = 10 # local variable declared "inside the function" 
    lb = 20 # local variable declared "inside the function" 
    print(la)
    print(lb)
    
add()    

print("=" * 50)
 
# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?

def add(la,lb): # local variable la and lb 
    print(la)
    print(lb)
    
add(30,40) 

# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?

print("=" * 50)

# Global Scope
ga = 70

def add(la,lb):
    print(la)
    print(lb)
    print(ga) # accessing global inside the function
    
add(50,60)
# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?
print(ga)

print("=" * 50)

ga = 100 # ga is global 

def add(la,lb,ga): # ga is local 
    print(la)
    print(lb)
    print(ga) # 90 preference is local
    # print(ga) # 100 want to access  
    print(globals()['ga']) # 100 want to access  
    
add(70,80,90) 

print("=" * 50)

# global variables outside the function
count = 0
print(count)
count += 1 
print(count)

print("=" * 50)


# global variables inside the function
count = 0
print(count)

def increment():
    global count # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    count += 1   # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    return count
print("=" * 50)

print(increment())

print("=" * 50)

# Lambda Functions 

# Without lambda, standard functions
def add(a,b):
    return a + b 
print(add(200,300))

print("=" * 50)

# With lambda function
# lambda arguments:expression
lambda a,b:a + b 
# IILE -> print((lambda_function)(arguments))
print((lambda a,b:a + b)(20,30))
print("=" * 50)

# Without lambda, standard functions check the number is even or not
def is_even_num(num):
    if num % 2 == 0:
        return True 
    else:
        return False
    
print(is_even_num(13))
print("=" * 50)
print(is_even_num(12))
print("=" * 50)

# With lambda functions check the number is even or not
# lambda arguments:expression
lambda num:num % 2 == 0
# IILE -> print((lambda_function)(arguments))
print((lambda num:num % 2 == 0)(5))
print("=" * 50)
print((lambda num:num % 2 == 0)(6))
print("=" * 50)

# Without Higher Order Functions - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]     ==>     [1,4,9,16,25]
def square_list(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num * num)
    return squared_list
print(square_list([1,2,3,4,5]))

print("=" * 50)

# With Higher Order Functions - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]     ==>     [1,4,9,16,25]
# map(function,Iterable) 
# map(function,[1,2,3,4,5]) 
map((lambda num:num * num),[1,2,3,4,5]) # Higher Order Function
print(map((lambda num:num * num),[1,2,3,4,5]))
print(list(map((lambda num:num * num),[1,2,3,4,5])))

print("=" * 50)

products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},

    {"name": "Tablet", "price": 25000, "discount": 10},
    {"name": "Monitor", "price": 12000, "discount": 8},
    {"name": "Keyboard", "price": 2000, "discount": 5},
    {"name": "Mouse", "price": 1000, "discount": 0},
    {"name": "Printer", "price": 15000, "discount": 12},

    {"name": "Smartwatch", "price": 7000, "discount": 18},
    {"name": "Speaker", "price": 3500, "discount": 10},
    {"name": "PowerBank", "price": 1800, "discount": 7},
    {"name": "Router", "price": 2500, "discount": 5},
    {"name": "HardDisk", "price": 6000, "discount": 15},

    {"name": "SSD", "price": 5500, "discount": 20},
    {"name": "Webcam", "price": 2200, "discount": 10},
    {"name": "Microphone", "price": 3000, "discount": 12},
    {"name": "Projector", "price": 40000, "discount": 25},
    {"name": "Drone", "price": 75000, "discount": 30},

    {"name": "TV", "price": 45000, "discount": 18},
    {"name": "GamingConsole", "price": 38000, "discount": 15},
    {"name": "VRHeadset", "price": 20000, "discount": 22},
    {"name": "GraphicsCard", "price": 65000, "discount": 10},
    {"name": "Motherboard", "price": 12000, "discount": 8}
]

# Assume In Real World You Have 50k Product Records 
# Requirement: Give Prices After Applying discounts
# {"name": "Laptop", "price": 80000, "discount": 10} -> 80000 - 8000 = 72000 
# How To Do Style 

prices_after_discount = []

for product in products:
    print(product)
    
    price = product['price']
    print("Price Of Product: ",price)
    
    discount = product['discount']
    print("Discount On Product: ",discount)
    
    price_after_discount = price - price * discount / 100
    print("Price Of Product After Discount: ",price_after_discount)
    
    # Store Discounted Prices
    prices_after_discount.append(price_after_discount)
    
print("Prices Of Products After Discount: ",prices_after_discount)
    
print("=" * 50)    
    
# Assume In Real World You Have 50k Product Records 
# Requirement: Give Prices After Applying discounts
# {"name": "Laptop", "price": 80000, "discount": 10} -> 80000 - 8000 = 72000 
# What To Do Style - With Higher Order Functions - map()
# print(list(map((lambda num:num * num),[1,2,3,4,5])))
print(list(map((lambda product:product['price'] - product['price'] * product['discount']/100),products)))
print("=" * 50)  
prices_after_discount = list(map((lambda product:product['price'] - product['price'] * product['discount']/100),products))
print("Prices Of Products After Discount: ",prices_after_discount)
print("=" * 50)  

# Without Higher Order Functions - filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10]    ==>     [2,4,6,8,10]

def even_list(numbers):
    evened_list = []
    for num in numbers:
        if num % 2 == 0:
            evened_list.append(num)
    return evened_list
print(even_list([1,2,3,4,5,6,7,8,9,10]))

print("=" * 50)  

# With Higher Order Functions - filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10]    ==>     [2,4,6,8,10]
# filter(function,Iterable) 
# filter(function,[1,2,3,4,5,6,7,8,9,10]) 
filter((lambda num:num % 2 ==0),[1,2,3,4,5,6,7,8,9,10]) # Higher Order Function
print(filter((lambda num:num % 2 == 0),[1,2,3,4,5,6,7,8,9,10]))
print(list(filter((lambda num:num % 2 == 0),[1,2,3,4,5,6,7,8,9,10])))

print("=" * 50)

products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},

    {"name": "Tablet", "price": 25000, "discount": 10},
    {"name": "Monitor", "price": 12000, "discount": 8},
    {"name": "Keyboard", "price": 2000, "discount": 5},
    {"name": "Mouse", "price": 1000, "discount": 0},
    {"name": "Printer", "price": 15000, "discount": 12},

    {"name": "Smartwatch", "price": 7000, "discount": 18},
    {"name": "Speaker", "price": 3500, "discount": 10},
    {"name": "PowerBank", "price": 1800, "discount": 7},
    {"name": "Router", "price": 2500, "discount": 5},
    {"name": "HardDisk", "price": 6000, "discount": 15},

    {"name": "SSD", "price": 5500, "discount": 20},
    {"name": "Webcam", "price": 2200, "discount": 10},
    {"name": "Microphone", "price": 3000, "discount": 12},
    {"name": "Projector", "price": 40000, "discount": 25},
    {"name": "Drone", "price": 75000, "discount": 30},

    {"name": "TV", "price": 45000, "discount": 18},
    {"name": "GamingConsole", "price": 38000, "discount": 15},
    {"name": "VRHeadset", "price": 20000, "discount": 22},
    {"name": "GraphicsCard", "price": 65000, "discount": 10},
    {"name": "Motherboard", "price": 12000, "discount": 8}
]

# Assume In Real World You Have 50k Product Records 
# Requirement: Find The Premium Products i.e Product With Price Above 25000
# {"name": "Laptop", "price": 80000, "discount": 10} -> price > 25000 then premium
# How To Do Style 
premium_products = []

for product in products:
    # print(product)
    price = product['price']
    if price > 25000:
        print(product)
        premium_products.append(product)
        
print("All Products: ",products)
print("=" * 50)
print("Premium Products: ",premium_products)
print("=" * 50)

# Assume In Real World You Have 50k Product Records 
# Requirement: Find The Premium Products i.e Product With Price Above 25000
# {"name": "Laptop", "price": 80000, "discount": 10} -> price > 25000 then premium
# What To Do Style - With Higher Order Functions - filter()
# print(list(filter((lambda num:num % 2 == 0),[1,2,3,4,5,6,7,8,9,10])))
print(list(filter((lambda product:product['price'] > 25000),products)))
premium_products = list(filter((lambda product:product['price'] > 25000),products))
print("=" * 50)
print("Premium Products: ",premium_products)
print("=" * 50)

for product in premium_products:
    print(product['name'],product['price'])
    
# Real World Data Looks and Comes like this in the form of a "file" (csv & xls files) 
# https://e.nodegoat.net/CMS/upload/guide-import_person_spreadsheet_excel.png    