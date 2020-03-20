h = "Wrong guess, you have"
i = 5
j = "guesses"
k = "left"
l = "."
print("Welcome to the game 'Guess the No.', a game created by Harry Bhai.\nThe value you choose should be an integer\nYou have a total of", i, j+l)
x = int(input("Guess your first no.:\n"))

while(i>0):

    if x < 18:
        i = i - 1
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
        print("Congratulations your guess is correct!!")
        break