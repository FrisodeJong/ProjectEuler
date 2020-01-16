import time
start_tijd = time.time()

MOD = 10**10
ans = (28433 * pow(2, 7830457, MOD) + 1) % MOD
print(str(ans))

eind_tijd = time.time()
print(eind_tijd - start_tijd)