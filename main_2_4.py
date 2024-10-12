from itertools import count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_Primes = []
for i in numbers:
    if i == 1:
        continue
    for j in range(1, i):
        if j + 1 == i:
            Primes.append(i)
        else:
            if i%(j + 1) == 0:
                Not_Primes.append(i)
                break
print(Primes)
print(Not_Primes)
