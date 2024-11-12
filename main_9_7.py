def is_prime(func):
    def wrapper(*args):
        __result = func(*args)
        is_pr = 'Простое'
        if __result < 2:
            pass
        else:
            for i in range(2, int(__result ** 0.5) + 1):
                if __result % i == 0:
                    is_pr = 'Составное'
        print(is_pr)
        return __result
    return wrapper

@is_prime
def sum_three(a, b ,c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
