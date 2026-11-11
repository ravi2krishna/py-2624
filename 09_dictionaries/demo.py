# Empty Dictionary

empty_dict = {}
print(type(empty_dict))
print(empty_dict)

empty_dict = dict()
print(type(empty_dict))
print(empty_dict)

# Dictionary With Numeric Data 
data = {1:10,2:20,3:30}
print(data)

# Dictionary With Text Data 
data = {"c1":"python","c2":"django","c3":"react"}
print(data)


# Dictionary With Mixed Data 
data = {1:10,2:20,"c1":"python","c2":"django","gpa":9.5,"passed":True}
print(data)

# Access Data
data = {1:10,2:20,3:30}
# print(data[0]) # KeyError: 0
print(data[1])


# Access Data - 10k records 
data = {1:10,2:20,3:30,4:40,5:50,1000:10000}
print(data[1])
print(data[2])
print(data[3])
# ......
print(data[1000])

print(data)

# Access Individual Elements From Dict 
for num in data: # We Got Only Keys 
    print(num)

# We Need Values    
for key in data: # We Got Only Keys 
    print(data[key]) # dict[key]
    
# Apply Conditionals -> Requirements: Give Only Even Numbers
data = {1:10,2:20,3:35,4:40,5:55,1000:10000} 
for key in data: 
    if data[key] % 2 == 0:
        print(data[key])
        
# Duplicates 
data = {1:10,2:20,1:30,3:20}
print(data)

# keys should be immutable 
# data = {['ten']:10,['twenty']:20}
# print(data)

data = {('ten'):10,('twenty'):20}
print(data)

# Real World Dictionaries Looks like JSON Data 
# https://media.licdn.com/dms/image/v2/D4D12AQGwOUMYbhUu-A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1682148646113?e=2147483647&v=beta&t=qeCSY5Ktzx2jkeq7suYaSBV_-OS_18P-yuabrIhNWcU
# https://www.anbowell.com/_astro/guide_to_json.DimYsN86.webp
# https://www.goanywhere.com/sites/default/files/styles/max_2600x2600/public/2022-08/example_json_file_0.png.webp?itok=nS3qt8dd

# A Small Data Structure To Store Students Data 
students = {
    "101": {
        "name":"Ravi",
        "email":"ravi@gmail.com",
        "courses":["python","react","sql"],
        "courses_fee":(10000,10000,5000)
    },
    "102": {
            "name":"John",
            "email":"john@yahoo.com",
            "courses":["cloud","aws","azure"],
            "courses_fee":(25000,10000,10000)
    }
}

# Get Me The Courses Enrolled By John
print(students["102"])
print(students["102"]['courses'])

# Tell Me If John is Google Customer Or not 
print(students["102"]['email'])
print(type(students["102"]['email']))
if students["102"]['email'].endswith("@gmail.com"):
    print(f"User {students["102"]['name']} is Google Customer")
else:
    print(f"User {students["102"]['name']} is Not Google Customer")
    
list_data = [1,2,3]
tuple_data = (1,2,3)
dict_data = {1:10,2:20,1:30,3:20}

