# arguments.variable.positional.py
def minimum(*n):
    # print(type(n))
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

minimum(1, 3, -7, 9)
minimum()