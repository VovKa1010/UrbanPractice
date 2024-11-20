numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for item in numbers:
    if item not in [0, 1]:
        is_prime = True
        for i in range(2, item):
            if i != item and item % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(item)
        else:
            not_primes.append(item)

print(primes)
print(not_primes)
