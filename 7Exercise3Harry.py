h = "Wrong guess, you have"
i = 5
j = "guesses"
k = "left"
l = "."
print("Welcome to the game 'Guess the No.', a game created by Harry Bhai.\nThe value you choose should be an integer\nYou have a total of", i, j+l)
x = int(input("Guess your first no.:\n"))
u = 1
while(i>0):

    if x < 18:
        i = i - 1
        u = 6 - i
        y = i
        if y == 0:
            print("Game Over!")
        elif y == 1:
            print(h, i, "guess", k+l)
            x = int(input("Now guess a larger no.!\n"))
        else:
            print(h, i, j, k+l)
            x = int(input("Now guess a larger no.!\n"))
    elif x > 18:
        i = i - 1
        u = 6 - i
        y = i
        if y == 0:
            print("Game Over!")
        elif y == 1:
            print(h, i, "Guess", k+l)
            x = int(input("Now guess a smaller no.!\n"))
        else:
            print(h, i, j, k+l)
            x = int(input("Now guess a smaller no.!\n"))
    else:
        if u == 1:
            print("Congratulations your",str(u)+"st guess is correct!!")
        elif u == 2:
            print("Congratulations your", str(u) + "nd guess is correct!!")
        elif u == 3:
            print("Congratulations your", str(u) + "rd guess is correct!!")
        elif u == 5:
            print("Congratulations your", str(u) + "th i.e. last guess is correct!!")
        else:
            print("Congratulations your",str(u)+"th guess is correct!!")
        break