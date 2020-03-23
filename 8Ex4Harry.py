n = int(input("Enter a no.:\n"))
b = input("Enter a boolean:\n")
i=1
try:
    if b == "True" or "1" :
        while i<n:
            print("*"*i)
            i += 1
except Exception as e:
    print("Error:",e,"\nTry using True with Capital 'T' or use '1' instead")

