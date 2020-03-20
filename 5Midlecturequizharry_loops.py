list =["a","b",9,3,0,14,"i",16,78,"c","f"]
for items in list:
    if str(items).isnumeric() and items>6:
        print(items)