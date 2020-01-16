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

lijst_priem = priem_getallen(1000000)


def is_circular(x):
    string = str(x)
    rotaties = []
    vlag = True
    for i in range(0, len(string)):
        rotaties.append(string[i : ] + string[ : i])
    for j in rotaties:
        x = int(j)
        if x not in lijst_priem:
            vlag = False
            break
    if vlag == True:
        return True

antwoord = 0
for i in lijst_priem:
    if is_circular(i):
        antwoord +=1

print(antwoord)


eind_tijd = time.time()
print(eind_tijd - start_tijd)