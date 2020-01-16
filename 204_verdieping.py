# tijdmodule om de uitvoeringstijd te berekenen met daarbij start tijd
import time
start_tijd = time.time()

# Lijst maken alle hamming nummers met de priemgetallen t/m 100
hamming_lijst = []
priemfactor_lijst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for i in range(1, 10**9):
    x = i
    for y in priemfactor_lijst:
        while x % y == 0:
            x = x / y
    if x == 1.0:
        hamming_lijst.append(i)
    i = i + 1

# getal '1' hoort er ook bij, dus bij de lengte van hamming_lijst voegen we er nog 1 toe
print(len(hamming_lijst)+ 1)

# eind tijd noteren
eind_tijd = time.time()

# print het totale tijd van de uitvoering
print(eind_tijd - start_tijd, "sec")