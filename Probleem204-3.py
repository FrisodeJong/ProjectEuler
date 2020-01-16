import time 
start_tijd = time.time()

LIMIT = 10**8
primes = [2, 3, 5]

def count(primeindex, product):
	if primeindex == len(primes):
		return 1 if product <= LIMIT else 0
	else:
		result = 0
		while product <= LIMIT:
			result += count(primeindex + 1, product)
			product *= primes[primeindex]
		return result


print(str(count(0,1)))

eind_tijd = time.time()
print(eind_tijd-start_tijd)
