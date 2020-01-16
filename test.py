import time
start_tijd = time.time()

# priem_lijst = []
# for i in range(1, 10):
#     for x in range(2, i):
#         if i % x == 0:
#             break
#     else:
#         priem_lijst.append(i)

# print(priem_lijst)

def is_priem(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return 0
        i += 1
    return x

priem_lijst = (is_priem(x) for x in range(2, 10))


eind_tijd = time.time()
print(eind_tijd - start_tijd)