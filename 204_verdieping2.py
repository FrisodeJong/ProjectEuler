import time
import itertools

print("Voer het gewenste type hamming nummer in:")
n = int(input())
type_hamming = n

limiet = type_hamming * type_hamming
# print("Voer het gewenste limiet in:")
# limiet = int(input())

def grootste_priem_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
        if i > type_hamming:
            break
    return n

start_tijd = time.time()

teller = 0
for iterator in itertools.count(1,1):
    if iterator > limiet:
        break
    priem_factor = grootste_priem_factor(iterator)
    if priem_factor <= type_hamming:
        teller += 1

# print("Gegeven type is", type_hamming)
# print("Het gegeven limiet is", limiet)
print("Er zijn", teller, "hamming nummers van type", n, "onder de", limiet)

eind_tijd = time.time()
print(eind_tijd - start_tijd, "sec")