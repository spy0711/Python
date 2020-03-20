list =["a","b",9,3,0,14,"i",16,78,"c","f"]
for item in list:
    if str(item).isnumeric() and item>6:
        print(item)