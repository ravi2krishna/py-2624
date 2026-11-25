# Customer wants arithmetic operations and profile related information

# print(add(2,5)) # NameError: name 'add' is not defined

# import mathprofile
# print("Sample Value Is: ",mathprofile.sample_value)

from mathprofile import sample_value,mul,profile
print("Sample Value Is: ",sample_value)
print("Product Of Numbers: ",mul(2,5))
print(profile())

