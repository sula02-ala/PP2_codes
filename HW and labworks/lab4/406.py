n = int(input())

def fibonacci(n):
    a, b = 0, 1   

    for i in range(n):
        yield a
        a, b = b, a + b   

gen = fibonacci(n)

print(",".join(str(x) for x in gen))