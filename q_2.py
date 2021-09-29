def compute():
    res = 2
    f1 = 1
    f2 = 2
    f3 = 0

    while (f3 := f1 + f2) < 4000000:
        if f3 % 2 == 0:
            res += f3
        f1 = f2; f2 = f3
    return res
    

if __name__ == "__main__":
    print(compute())

#too big for recursion