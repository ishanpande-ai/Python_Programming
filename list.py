list=['x','x','y','y','z','z','w','w','u','u']
if x is str in list and y is str in list and z is str in list and r is str in list and x and y and z is not repeated in list:
    print("list is unique")
i=0
while i!=len(list):
    if list[i] == list[i+1]:
        list.pop(i)
        list.pop(i)
    i+=1

else:
    print('')