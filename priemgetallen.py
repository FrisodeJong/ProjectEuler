def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	is_prime[2] = True
	#even numbers except 2 have been eliminated
	for i in range(3,int(n**0.5+1),2):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = [2]
	for i in range(3,n,2):
		if is_prime[i]:
			prime.append(i)
	return prime

#sieving prime numbers upto 1 million
primes = sieve(100)

priemgetallen = set()
def maak_set():
	return(priemgetallen.add(i) for i in primes)

print(next(maak_set()))
print(next(maak_set()))
print(next(maak_set()))
print(next(maak_set()))



