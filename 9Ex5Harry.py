def getdate():
    import datetime
    return datetime.datetime.now()
def  we(a):
    if a == 1:
        h1 = open("99Harry" + b + ".txt")
        h1o = h1.read()
        h1.close()
        return h1o
    elif a == 2:
        h2 = open("99Rohan" + b + ".txt")
        h2o = h2.read()
        h2.close()
        return h2o
    elif a == 3:
        h3 = open("99Hammad" + b + ".txt")
        h3o = h3.read()
        h3.close()
        return h3o
c = int(input("1 to Read, 2 for writing\n"))
b = input("Input Exercise or Diet\n")
a = int(input("1 for Harry, 2 for Rohan, 3 for Hammad\n"))
if c == 1:
    print(we(a))
elif c == 2:
    print(wer(a))
