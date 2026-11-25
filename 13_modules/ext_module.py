# Fetch API Data 
# https://dummyjson.com/products

# import requests # ModuleNotFoundError: No module named 'requests'
# r = requests.get('https://dummyjson.com/products')
# status_code = r.status_code
# print(status_code)

# pip install requests
import requests # ModuleNotFoundError: No module named 'requests'
r = requests.get('https://dummyjson.com/products')
status_code = r.status_code
print(status_code)

print("=" * 50)

r = requests.get('https://dummyjson.com/countries')
status_code = r.status_code
print(status_code)

print("=" * 50)

# Get API Data Based On status_code 
url = input("Enter API Endpoint: ")
response = requests.get(url)
# r = requests.get('https://dummyjson.com/countries')
status_code = response.status_code

if status_code == 200:
    print("=" * 50)
    print("Processing API Data")
    print("=" * 50)
    
    print(response.text) # Fetch Data From API

    
else:
    print("=" * 50)
    print("Processing API Failed")
    print("=" * 50)  

print("=" * 50)