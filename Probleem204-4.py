import time 
start_tijd = time.time()

priem_lijst = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def functie(n,m):
    if n==0:
        return n!=0
    for p in [i for i in range(m) if i in priem_lijst]:
        while n % p == 0:
            n = n / p
    return n==1

som = 0
teller = 1
while teller < 10**8:
    if functie(teller,5):
        som += 1
    teller += 1
print(som)


eind_tijd = time.time()
print(eind_tijd-start_tijd)