liczba = int(input("Podaj liczbe: "))
potega = int(input("Podaj potęge: "))
def pot(x,y):
    return x ** y
print(pot(liczba,potega))

#2 Sposób wersja zooptymalizowana, sprawdzająca błędy
try:
    liczba = int(input("Podaj liczbe: "))
    potega = int(input("Podaj potęge: "))
    wynik = pow(liczba,potega)
except ValueError:
    print("Nie podano liczb")
except:
    print("Inny błąd")
