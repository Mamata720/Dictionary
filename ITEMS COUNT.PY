dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']
   }
count= 0
for i in dict1:
    value_count = (len(dict1[i]))
    count +=value_count
print(count)

