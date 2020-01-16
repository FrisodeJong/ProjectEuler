import time
import itertools
start_tijd = time.time()

# functie die kijkt of een getal priem is
def check_priemgetal(getal):
    for i in range(2,getal):
        if getal % i == 0:
            return False

permutaties = list(itertools.permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9']))
# permutaties = list(itertools.permutations(['2', '3', '4', '5', '6', '7', '8', '9']))
pandigital_number = 0
for x in permutaties:
    getal = int(''.join(x))
    if getal > pandigital_number:
        if check_priemgetal(getal) == None:
            pandigital_number = getal

print(pandigital_number)

eind_tijd = time.time()
print(eind_tijd - start_tijd)