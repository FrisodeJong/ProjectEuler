# from itertools import permutations
# perms = [''.join(p) for p in permutations ('0123')]
# print(perms)
# sort = sorted (perms)
# print(sort)
# print(sort[3])

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n

print(largest_prime_factor(20))