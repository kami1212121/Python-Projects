from random import randint
odp = -1
razy = 0
while odp != razy:
    razy += 1
    Liczba = input("Podaj liczbe: ")
    Losowa = randint(1, 10)
    if razy > 0 and int(Liczba) != Losowa:
        print("Nie udało się")
        print(Losowa)
    elif int(Liczba) == Losowa:
        print("GRATULACJE ODGADŁEŚ LICZBE")
        print("Losowa liczba to: " + str(Losowa))
        print("Zgadłeś za: " + str(razy))
        break
