def outer():
    def inner():
        global g
        nonlocal n
        l = 0
        m = int(input())
        for _ in range(m):
            scope, x = input().split()
            x = int(x)
            if scope == "global":
                g += x
            elif scope == "nonlocal":
                n += x
            elif scope == "local":
                l += x
        print(g, n)
    n = 0
    inner()
g = 0
outer()