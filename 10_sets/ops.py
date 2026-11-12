# Set Methods Operations 


# add(): Add Element To Set 
data = {10,20,30,40,50}
print(data)
data.add(60)
print(data)

# update(): Add Multiple Elements To Set 
data = {10,20,30,40,50}
print(data)
data.update([60,70,80,80])
print(data)

# pop(): Remove Random Element 
data = {10,20,30,40,50}
print(data)
data.pop()
print(data)

# remove(): Remove Element By Value
data = {10,20,30,40,50}
print(data)
data.remove(30)
# data.remove(300) # KeyError: 300
print(data)


# discard(): Remove Element By Value, if value not present, then don't give exception
data = {10,20,30,40,50}
print(data)
data.discard(30)
data.discard(300) 
print(data)

# clear(): Empties Set
data = {10,20,30,40,50}
print(data)
data.clear()
print(data)

# copy(): Create A Copy
data = {10,20,30,40,50}
print(data)
backup = data.copy()
print(backup)

# print(dir(data))

# Special Methods Specific To Sets Only 
s1 = {10,20,30,40,50}
print(s1)

s2 = {40,50,60,70,80}
print(s2)

# union(): Combine Sets 
print(s1.union(s2))
print(s1 | s2) # | this is called pipe 

# intersection(): Get Common Elements 
print(s1.intersection(s2))
print(s1 & s2) 

print(s1)
print(s2)

# intersection_update(): get common elements from sets, updates calling sets 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.intersection_update(s2))

print(s1)
print(s2)

# difference(): Removes Common elements from the set and gives unique elements 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.difference(s2))

print(s2 - s1) # 60,70,80

print(s1)
print(s2)

# difference_update(): Removes Common elements from the set and gives unique elements, updates calling sets  
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.difference_update(s2))

print(s1)
print(s2)

# symmetric_difference(): Removes Common elements from the set and takes combined elements from both sets

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.symmetric_difference(s2))

print(s1)
print(s2)

# symmetric_difference_update(): Removes Common elements from the set and takes combined elements from both sets, updates calling sets  

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.symmetric_difference_update(s2))

print(s1)
print(s2)

# issubset(): Checks if given set is a subset of another set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s2.issubset(s1))
print(s3.issubset(s1))
print(s1.issubset(s3))

# issuperset(): Checks if given set is a superset of another set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s1.issuperset(s3))

# isdisjoint(): Check if sets have no common elements 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s1.isdisjoint(s3))
print(s2.isdisjoint(s3))


