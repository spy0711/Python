n = int(input("Enter a no.:\n"))
b = input("Enter a boolean:\n")


print(b)
 if b == "True" or "1":
     b = True
     print("its true")
 elif b == "False" or "0":
     b = False
     print("its false")
i = 1
try:
    if b == True:
        while i < n+1:
            print("f*"*i)
            i += 1
    elif b == False:
        while n > 0:
            print("s*"*n)
            n -= 1
except Exception as e:
    print("Error:",e,"\nTry using True with Capital 'T' or use '1' instead")

