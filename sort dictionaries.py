my_dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
dict1={}
for i in my_dict:
    s=my_dict[i]
    for i in my_dict:
        a=my_dict[i]
        if s>a:
            dict1[i]=a
for i in my_dict:
    s=my_dict[i]
    for i in my_dict:
        a=my_dict[i]
        if s<a:
            dict1[i]=a
print(dict1)
