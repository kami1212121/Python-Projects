import random
def generuj_haslo(dlugosc):
    znaki = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="
    haslo = ""
    for i in range(dlugosc):
        haslo += random.choice(znaki)
    return haslo
def main():
    while True:
        dlugosc = int(input("Podaj długość hasła 4-20: "))
        if dlugosc < 4 or dlugosc > 20:
            print("Niepoprawna długośc hasła")
        else:
            print("Generowanie hasła")
            print("------------------")
            haslo = generuj_haslo(dlugosc)
            print("Twoje nowe hasło to:", haslo)
        tn = input("Czy chcesz wygenerować kolejne hasło?t/n : ")
        if tn == "n":
            break
if __name__ == "__main__":
    main()
