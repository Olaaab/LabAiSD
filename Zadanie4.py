#Zaprojektuj algorytm wyszukiwania w tablicy jednowymiarowej minimalnej wartości.

def znajdz_minimum(tablica):
    minimum = tablica[0]
    for i in range(1, len(tablica)):
        if tablica[i] < minimum:
            minimum = tablica[i]
    return minimum
tablica = [11, 4, 8, 1, 8, 2]
print(znajdz_minimum(tablica))