def hanoi(n, jeden='A', dwa='B', trzy='C'):
    if n == 1:
        print(f"Przenieś krązek z {jeden} do {dwa}")
        return

    hanoi(n - 1, jeden, trzy, dwa)
    print(f"Przenieś krążek {n} z {jeden} do {dwa}")
    hanoi(n - 1, trzy, dwa, jeden)

hanoi(3)
