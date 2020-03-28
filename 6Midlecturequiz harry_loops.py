x = int(input("Type a no.: "))
if x > 100:
    print("Congratulations your guess is greater than 100.")
else:
    while(x < 101):
        x = int(input("Type another no.: "))
        if x > 100:
            print("Congratulations your no. is greater than 100.")
            break
