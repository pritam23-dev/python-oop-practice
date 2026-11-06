a = 30   # Global scope
b = 20
c = 60
def hablu():
    x = 100   # Local scope
    global c
    c = 70
    print(x)
    print(a)
    print(c)

hablu()



