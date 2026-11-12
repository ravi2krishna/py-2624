# Dictionary Methods / Operations 

data = {"a":"apple","b":"banana"}
print(data)

# update(): Add / Update Item In Dictionary
data.update({"c":"cherry"}) # If Key is not present, then add the item
print(data)

data.update({"a":"apricot"}) # If Key is present, then update the item
print(data)

# pop(): Remove an Item By key 
data = {"a":"apple","b":"banana"}
print(data)
data.pop("a")
print(data)

# popitem(): Remove Last Item
data = {"a":"apple","b":"banana"}
print(data)
data.popitem()
print(data)

# clear(): Empties Dictionary
data = {"a":"apple","b":"banana"}
print(data)
data.clear()
print(data)

# keys(): Used To Get Keys 
data = {"a":"apple","b":"banana"}
print(data)
output = data.keys()
print(output)
for key in data.keys():
    print(key)
    
# values(): Used To Get Values 
data = {"a":"apple","b":"banana"}
print(data)
output = data.values()
print(output)
for value in data.values():
    print(value)
    
# items(): Used To Get Both Keys & Values
data = {"a":"apple","b":"banana"}
print(data)
output = data.items()
print(output)
for item in data.items():
    print(item)
    
# setdefault(): returns a value of key, if the key is already present
# if key doesn't exist, then adds the item and returns the value
data = {"a":"apple","b":"banana"}
print(data)
print(data.setdefault("b","blueberry"))
print(data.setdefault("c","cheery"))
print(data)

# copy(): Creates A Copy
data = {"a":"apple","b":"banana"}
print(data)
backup = data.copy()
print(backup)