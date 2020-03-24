n = int(input("Please Enter a no.:\n"))
while True:
    b = input("Enter a boolean:\n") #it'll work for 0,1,True,False or even without capital t and f i.e. true or false
    i = 1
    try:
        b = int(b)
        if b == 1:
            while i < n+1:
                print("*"*i)
                i += 1
            break
        elif b == 0:
            while n > 0:
                print("*"*n)
                n -= 1
            break
    except Exception as q:
        print("Trying True or False type boolean....!!")
        b = b.capitalize()

    try:
        if b == "True":
            while i < n+1:
                print("*"*i)
                i += 1
            break
        elif b == "False":
            while n > 0:
                print("*"*n)
                n -= 1
            break
    except Exception as e:
        print("Error:",e,"\nTry using True with Capital 'T' or use '1' instead")
    print("Error, Try again!")
    continue