#to make game more interesting use random module
import random
random = random.randint(0,1000)
x = int(input("Type a no.: "))
if x > random:
    print("Congratulations your guess is greater than 100.")
else:
    while(x < random):
        x = int(input("Type another no.: "))
        if x > random:
            print("Congratulations your no. is greater than 100.")
            break
