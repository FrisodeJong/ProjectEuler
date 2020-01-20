import time
import itertools

# functie die checked of getal x een priemgetal is
# In jouw geval is deze functie gegeven door is_prime(). Dus deze hieronder kan weg
def is_priem(x):
    if x == 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

# Dit is een functie die de delers van input x geven. 
def delers(x):
    for d in range(1,x):
        if x % d == 0:
            yield d

# Deze functie checked voor alle delers van n (gevonden door de functie delers(x)), 
# of de deler + (n // deler) een priemgetal is.
def priem_deler(n):
    for deler in delers(n):
        check = deler + (n // deler)
        if is_priem(check) == False:
            return False

# Vraag de gebruiker voor het invoeren van een willekeurig integer getal.
print("Voer een getal in:")
n = int(input())

# Zet de starttijd van de timer.
start_tijd = time.time()

# Start met tellen vanaf het gegeven getal en kijken voor elk getal of we 
# de eigenschap hebben die bij de functie priem_deler(n) wordt gecheckt.
for iterator in itertools.count(n+1,1):
    if priem_deler(iterator) == None:
        getal = iterator
        break

# Print het resultaat.
print("Het eerstvolgende getal met die bepaalde eigenschap is", getal)

# Stop de timer.
eind_tijd = time.time()
# Print de tijd die het algoritme erover gedaan heeft.
print(eind_tijd - start_tijd, "sec")