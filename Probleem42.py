# alle woorden van het alphabet met een waarde in een dictionary. Deze zijn makkelijk aan te roepen als key-value pair
Alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
            'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
            'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
            'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
            'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 
            'Z': 26, '"': 0 }

# check woorden lijst en maak er losse strings van (elke string bestaat uit 1 woord)
Tekst = open("p042_words.txt","r")
for lijn in Tekst:
    woorden = lijn.split(",")

# vind alle triangle nummers. Deze kunnen niet groter zijn dan het langste woord * 26
Triangle_nummers = []
for n in range(1, (len(max(woorden, key = len))-2) * 26):
    triangle_nummer = 1/2 * n * (n + 1)
    Triangle_nummers.append(int(triangle_nummer))

# functie voor het vinden van de woordwaarde   
def check_waarde(woord):
    woord_waarde = 0
    for letter in woord:
        woord_waarde = woord_waarde + Alphabet[letter]
    return woord_waarde

# for loop over alle woorden in de lijst 'woorden'. Bij elke iteratie kijken of het woord een triangle waarde heeft
resultaat = 0
for huidig_woord in woorden:
    waarde = check_waarde(huidig_woord)
    for nummer in Triangle_nummers:
        if nummer == waarde:
            resultaat += 1
            break

print(resultaat)