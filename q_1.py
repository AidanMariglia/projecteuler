from functools import reduce

def compute():
    multiples = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
    s = reduce(lambda a, b: a + b, multiples)
    return s

if __name__ == "__main__":
    print(compute())