name='MISSISSIPPI'
dict1={}
for char in name:
    if char not in dict1:
        dict1[char]=1
    else:
        dict1[char]=dict1[char]+1
print(dict1)