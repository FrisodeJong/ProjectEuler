import time
start_tijd = time.time()

# functie die kijkt of een getal priem is
def check_priemgetal(getal):
    for i in range(2,getal):
        if getal % i == 0:
            return False

# functie die kijkt of het getal pandigital is
def check_pandigital(getal):
    getal_string = str(getal)
    lijst = ['0']
    for i in getal_string:
        if i in lijst:
            return (False)
        lijst.append(i)

digital_prime = 0
vlag = True
# getal = 1000000000 # doet er 74 seconden over
getal = 987654320
while vlag == True:
    if check_pandigital(getal) == None:
        if check_priemgetal(getal) == None:
            break
    getal = getal - 1

print(getal)


eind_tijd = time.time()
print(eind_tijd - start_tijd)