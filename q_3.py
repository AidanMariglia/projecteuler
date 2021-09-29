def prime_factors(n):
    res = []
    d = 2

    while n > 1:
        while n % d == 0:
            res.append(d)
            n /= d
        d += 1

    return res

def compute():
    N = 600851475143
    return max(prime_factors(N))

if __name__=="__main__":
    print(compute())