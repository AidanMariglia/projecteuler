def isPrime(n):
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False

    return True

def compute():
    N = 600851475143
    is_prime = [True for i in range(2, int(N/2))]

    if isPrime(N):
        return N

    for p in v:
        if is_prime

if __name__=="__main__":
    print(compute())