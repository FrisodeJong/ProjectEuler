from itertools import permutations 
lijst = [int(i) for i in "12351"]

def converteren(lijst): 
	resultaat = int("".join(map(str, lijst))) 
	return resultaat

def permuteren(string):
    getallen = []
    permutatie_lijst = [int(i) for i in string]
    alle_permutaties = permutations(permutatie_lijst)
    for i in alle_permutaties:
        getallen.append(converteren(i))
    return getallen

x = permuteren(str(453))
print(x)

# x = 3
# lijst = [2]
# while x < 100:
#     lijst_permutaties = permuteren(str(x))
#     for i in lijst_permutaties:
#         if x % 2 != 0:
#             vlaggetje = True
#             for i in lijst:
#                 if x % i == 0:
#                     vlaggetje = False
#                     break
#                 if vlaggetje == True:
#                     x = str(x)

#                     lijst.append(x)
#     x = x + 1


