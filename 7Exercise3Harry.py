n=18
g = "Wrong guess,"
h = "you have"
i = 5
j = "guesses"
k = "left"
l = "."
print("You have", i, j+l)
x = int(input("Guess your first no.\n"))

while(i>0):

    if x < 18:
        i = i - 1
        y = i
        if y == 0:
            print("Game Over")
        elif y== 1:
            print(g, h, i, "guess", k+l)
            x = int(input("Now guess a smaller no.\n"))
        else:
            print(g, h, i, j, k+l)
            x = int(input("Now guess a larger no.\n"))
    elif x > 18:
        i = i - 1
        y = i
        if y == 0:
            print("Game Over")
        elif y== 1:
            print(g, h, i, "Guess", k+l)
            x = int(input("Now guess a smaller no.\n"))
        else:
            print(g, h, i, j, k+l)
            x = int(input("Now guess a smaller no.\n"))
    else:
        print("Congratulations your guess is correct!!")
        break
