import time
start_tijd = time.time()

a = 0

for a in range(0,333):
    b = float((500000 - (1000*float(a)))/(1000 - float(a)))
    if (b).is_integer():
        if a < b:
            c = 1000 - a - b
            if b < c:
                break

    
print(a, int(b), int(c))
print(int(a*b*c))


eind_tijd = time.time()
print(eind_tijd-start_tijd)
