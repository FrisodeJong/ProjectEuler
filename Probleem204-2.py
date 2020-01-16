import time 
start_tijd = time.time()

priemfactor_lijst = [2,3,5]
# priemfactor_lijst = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def in_priemfactor_lijst(x):
    for y in priemfactor_lijst:
        while x % y == 0:
            x = x / y
    return x

teller = 0
for i in range(6, 10**8):
    x = i
    y = in_priemfactor_lijst(x)
    if y == 1.0:
        teller += 1    
    i = i + 1
    
print(teller)

eind_tijd = time.time()
print(eind_tijd-start_tijd)