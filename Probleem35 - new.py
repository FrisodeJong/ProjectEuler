# tijdmodule om de uitvoeringstijd te berekenen met daarbij start tijd
import time
start_tijd = time.time()

# formule om alle priemgetallen te kunnen vinden
def priem_getallen(n):
    nummers = set(range(n, 1, -1))
    lijst = []
    while nummers:
        p = nummers.pop()
        lijst.append(p)
        nummers.difference_update(set(range(p * 2, n + 1, p)))
    return lijst

# maak een lijst met de priemgetallen onder de miljoen
lijst_priem = priem_getallen(1000000)

# een antwoord om mee te beginnen
antwoord = 0

# loop maken met de priemgetallen
for i in lijst_priem:

    # ervan uitgaand dat er geen 0,2,4,5,6,8 cijfers zijn
    vlag = True

    # beginnen met 10 cijfers
    nummer = i / 10

    # loop maken met de cijfers afgerond naar beneden
    while nummer:
        if (nummer % 10) % 2 == 0 or (nummer % 10) % 5 == 0:
            vlag = False
            break
        nummer //= 10

    # checken of de vlag true of false is
    if vlag:
        lengte = len(str(i))
        nummer = i

        # vanuit gaan de circulaire permutaties priemgetallen zijn
        antwoord += 1

        # loop maken met cirekelvormige permutaties
        for j in range(lengte):
            nummer = (nummer % 10) * 10 ** (lengte - 1) + nummer // 10

            # als een cirkelvormige permutaties geen priemgetal is
            if nummer not in lijst_priem:

                # haal er 1 af van het antwoord
                antwoord -= 1
                break

# print het aantal cirkelvormige priemgetallen
print(antwoord)

# eind tijd noteren
eind_tijd = time.time()

# print het totale tijd van de uitvoering
print(eind_tijd - start_tijd)