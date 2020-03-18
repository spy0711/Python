x = int(input("your age please:"))
if x > 18 and x < 101:
    print("you can drive")
elif x == 18:
    print("we cannot tell if you can drive, you have to come and take a test for it")
elif x < 18 and x < 4:
    print("sorry you cannot drive")
else:
    print("Illogical Input!!!")