import time
start_tijd = time.time()

# functie die checked of getal x een priemgetal is
def is_priem(x):
    if x == 1:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

# lijst met priemgetallen
priem_lijst = (is_priem(x) for x in range(2, 100000000))

# functie die de divisors van x geeft
def divisors(x):
    for d in range(1,x):
        if x % d == 0:
            yield d

# functie die voor een gegeven n kijkt of de formule een priemgetal geeft
def priem_divisor(n):
    for divisor in divisors(n):
        check = divisor + (n // divisor)
        if is_priem(check) == False:
            return False

def optellen():
    for n in range(2, 1000000):
        if priem_divisor(n) == None:
            yield True

print(sum(optellen()))

eind_tijd = time.time()
print(eind_tijd-start_tijd)