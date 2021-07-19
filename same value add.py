dic1={1:10, 2:20}
dic2={1:40,2:40}
dic3={5:50,6:60}
# {1: 10, 2: 60, 3: 30,  5: 50, 6: 60} 
dict4={} 

dict4.update(dic1)
dict4.update(dic2)
dict4.update(dic3)
dic4 ={}
for i in dic1:
    for j in dic2:
         for k in dic3:
            if i == j:#key i and j is giving key.
                a =dic1[i]+dic2[j]# dictionary name[variable ] is give value
                dic4[i]= a # dictionary append value
dict4={}
dict4.update(dic1)
dict4.update(dic2)
dict4.update(dic3)
for c in dic4:
    for d in dict4:
        if c == d:# key 
            dict4[c]= dic4[d] # dict4 is our dictinory in that dic4[d] value.
            break
print(dict4)
