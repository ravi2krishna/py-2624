# Inbuilt Modules

# def sqrt():
#     print("Give Square Root")
    
# sqrt() # NameError: name 'sqrt' is not defined

# print(math.sqrt(25)) # NameError: name 'math' is not defined. Did you forget to import 'math'?

# 1st Syntax
import math 
print(math.sqrt(25))
print(math.e)

# 2nd Syntax
# from module import specific_functionality (imports only what you need) # Recommended
from math import pi,e 
print(pi)
print(e)

