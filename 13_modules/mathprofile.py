# Requirement: Customer needs arithmetic operations and profile related information

# arithmetic operations 

sample_value = 2.364666

def add(a,b):
    return a + b 

def mul(a,b):
    return a * b 

# profile related information
def profile():
    first_name = input("Enter Your First Name: ")
    last_name = input("Enter Your Last Name: ")
    email = input("Enter Your Email Address: ")
    return f"Welcome {first_name} {last_name} - You Can Login With {email}"

