from itertools import permutations 
import time
start_tijd = time.time()

def priem_getallen(n):
    nummers = set(range(n, 1, -1))
    lijst = []
    while nummers:
        p = nummers.pop()
        lijst.append(p)
        nummers.difference_update(set(range(p*2, n+1, p)))
    return lijst

lijst_priem = priem_getallen(100)

def converteren(lijst): 
	resultaat = int("".join(map(str, lijst))) 
	return resultaat

def permuteren(string):
    getallen = []
    permutatie_lijst = [int(i) for i in string]
    alle_permutaties = permutations(permutatie_lijst)
    for i in alle_permutaties:
        getallen.append(converteren(i))
    return getallen

resultaat = 0
# circular_primes = []
for x in lijst_priem:
    lijst_permutaties = permuteren(str(x))
    vlag = True
    for y in lijst_permutaties:
        if y not in lijst_priem:
            vlag = False
            break
    if vlag:
        # circular_primes.append(x)
        resultaat += 1

print(resultaat)

eind_tijd = time.time()
print(eind_tijd - start_tijd)