list=['apple','banana','cherry','apple','banana','cherry']
uniquelist=[]
for item in list:
    if item not in uniquelist:
        uniquelist.append(item)
print(uniquelist)
