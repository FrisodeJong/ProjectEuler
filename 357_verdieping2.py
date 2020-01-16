import time
import itertools

# functie die checked of getal x een priemgetal is
def is_priem(x):
    if x == 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

# # lijst met priemgetallen
# priem_lijst = (is_priem(x) for x in range(2, n))

# functie die de delers van x geeft
def delers(x):
    for d in range(1,x):
        if x % d == 0:
            yield d

# functie die voor een gegeven n kijkt of de formule een priemgetal geeft
def priem_deler(n):
    for deler in delers(n):
        check = deler + (n // deler)
        if is_priem(check) == False:
            return False

print("Voer een getal in:")
n = int(input())

start_tijd = time.time()

for iterator in itertools.count(n+1,1):
    if priem_deler(iterator) == None:
        getal = iterator
        break

print("Het eerstvolgende getal met die bepaalde eigenschap is", getal)

eind_tijd = time.time()
print(eind_tijd - start_tijd, "sec")