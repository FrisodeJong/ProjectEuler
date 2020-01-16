import time 
start_tijd = time.time()


hamming_lijst = []
priemfactor_lijst = [2, 3, 5]

for i in range(1, 10**8):
    x = i
    for y in priemfactor_lijst:
        while x % y == 0:
            x = x / y
    if x == 1.0:
        hamming_lijst.append(i)     
    i = i + 1

print(len(hamming_lijst))

eind_tijd = time.time()
print(eind_tijd-start_tijd)