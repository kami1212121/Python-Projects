#1 Sposób
def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x-1)
print(silnia(5))
#2 Sposób
def silnia(x):
    if x <= 1:
        return 1
    else:
        wynik = 1
        for i in range(1, x + 1):
            wynik *= i
        return wynik
print(silnia(5))
