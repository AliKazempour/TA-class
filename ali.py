def fact(n):
    if n == 1 or n ==0 :
        return 1
    return n * fact(n-1)


def hello(name):
    print(f"Hello {name}")

print(fact(5))
