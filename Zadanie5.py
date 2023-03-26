#Zaprojektuj algorytm wyszukiwania w tablicy dwuwymiarowej minimalnej wartości w każdym
#wierszu. Po znalezieniu minimalnej wartości wstaw ją na początek danego wiersza (poprzez
#zamianę miejsc).

def min_values(tablica):
    for row in tablica:
        min_val = min(row)
        min_idx = row.index(min_val)
        row[0], row[min_idx] = row[min_idx], row[0]
    return tablica

tablica = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(min_values(tablica))