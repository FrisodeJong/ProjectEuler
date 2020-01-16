import time
start_tijd = time.time()

# lijst = [int(i) for i in range(3,20)]

# for x in range
#     for i in lijst:
#         if i % 2 == 0:
#             lijst.remove(i)
#     for i in lijst:
#         if i % 3 == 0:
#             lijst.remove(i)
#     lijst.append(3)


# lijst.sort()
# print(lijst)


lijst = [2]
x = 3
sum = 0
while x < 2000000:
    if x % 2 != 0:
        vlaggetje = True
        for i in lijst:
            if x % i == 0:
                vlaggetje = False
                break
        if vlaggetje == True:
            lijst.append(x)
            sum = sum + x
    x = x + 1
print(sum+2)


eind_tijd = time.time()
print(eind_tijd-start_tijd)
