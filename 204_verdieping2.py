import time
import itertools

# laat de gebruiker zijn gewenste type hamming nummer invoeren (input moet integer zijn)
print("Voer het gewenste type hamming nummer in:")
n = int(input())
type_hamming = n

# Het limiet is gelijk aan het kwadraat van het type
limiet = type_hamming * type_hamming

# Deze functie geeft de grootste priemfactor terug
def grootste_priem_factor(n):
    i = 2
    # Begin met 2 en start delen zolang het kan. 
    # Zodra de priemfactor groter wordt dan gegeven type hamming nummer, 
    # dan is het handig om meteen te stoppen (voor snelheid)
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
        if i > type_hamming:
            break
    return n

# Zet de starttijd om te kijken hoe lang het algoritme erover doet
start_tijd = time.time()

# Begin met 0 hamming nummers en tel er 1 bij op zodra er een nieuwe is gevonden
teller = 0
# Zet een counter aan die pas stopt op het moment als het limiet wordt overschreden
for iterator in itertools.count(1,1):
    if iterator > limiet:
        break
    priem_factor = grootste_priem_factor(iterator)
    if priem_factor <= type_hamming:
        teller += 1

# Print de uitkomst samen met de gegevens
print("Er zijn", teller, "hamming nummers van type", n, "onder de", limiet)

# Stop de timer
eind_tijd = time.time()
# Print de tijd die het algoritme nodig had om het resultaat te vinden
print(eind_tijd - start_tijd, "sec")