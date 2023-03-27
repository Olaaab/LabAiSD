#Implementacja algorytmu NWD w formie iteracyjnej:
def nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
print(nwd(12, 18))
print(nwd(28, 24))

#Implementacja algorytmu NWD w formie rekurencyjnej:
def nwd2(a, b):
    if a == b:
        return a
    elif a > b:
        return nwd2(a - b, b)
    else:
        return nwd2(a, b - a)
print(nwd2(12, 18))
print(nwd2(28, 24))

