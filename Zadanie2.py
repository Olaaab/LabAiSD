count = 0
n = int(input("Podaj ilość liczb w ciągu: "))
if n <= 0:
    print("Ilość liczb w ciągu musi być większa od 0.")
else:
    numbers = []
    i = 0
    while i < n:
        num = int(input(f"Podaj {i+1}. liczbę: "))
        numbers.append(num)
        i += 1
    for num in numbers:
        if num < 0:
            count += 1
    print(f"Ilość liczb ujemnych w ciągu: {count}")