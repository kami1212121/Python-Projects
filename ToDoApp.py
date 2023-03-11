def dodaj_zadanie(lista_zadan):
    tytul = input("Podaj tytuł zadania: ")
    opis = input("Podaj opis zadania: ")
    data = input("Podaj datę wykonania (RRRR-MM-DD): ")
    godzina = input("Podaj godzinę wykonania (GG:MM): ")
    zadanie = {"tytul": tytul, "opis": opis, "data": data, "godzina": godzina}
    lista_zadan.append(zadanie)
    print("Dodano zadanie: ", zadanie)

def usun_zadanie(lista_zadan):
    numer = int(input("Podaj numer zadania do usunięcia: "))
    if numer > 0 and numer <= len(lista_zadan):
        usuniete = lista_zadan.pop(numer-1)
        print("Usunięto zadanie: ", usuniete)
    else:
        print("Nieprawidłowy numer zadania.")

def wyswietl_zadania(lista_zadan):
    print("Lista zadań do wykonania:")
    if len(lista_zadan) == 0:
        print("Brak zadań.")
    else:
        for i, zadanie in enumerate(lista_zadan):
            print(i+1, ")", "Tytuł:", zadanie["tytul"], "| Opis:", zadanie["opis"], "| Data:", zadanie["data"], "| Godzina:", zadanie["godzina"])
            
def main():
    lista_zadan = []
    while True:
        print("Co chcesz zrobić?")
        print("1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Wyświetl zadania")
        print("4. Wyjdź")
        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            dodaj_zadanie(lista_zadan)
        elif wybor == "2":
            usun_zadanie(lista_zadan)
        elif wybor == "3":
            wyswietl_zadania(lista_zadan)
        elif wybor == "4":
            break
        else:
            print("Nieprawidłowa opcja.")

if __name__ == "__main__":
    main()
