def dec_to_bin(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        iloraz = n // 2
        reszta = n % 2
        return dec_to_bin(iloraz) + str(reszta)
print(dec_to_bin(112))