#Aplikacja do nauki angielskiego
import random
from translate import Translator
import datetime
import os
import pickle
# Ustawienie języka wejściowego i wyjściowego
jezyk_wejsciowy = 'pl'
jezyk_wyjsciowy = 'en'
translator = Translator(to_lang=jezyk_wyjsciowy, from_lang=jezyk_wejsciowy)
#Tworzenie funkcji z pętlą while True do obsługi programu
def main():
    while True:
        try:
            print("Chcesz wpisać czy wylosować słówko?")
            print("1.Wpisz ręcznie")
            print("2.Wylosuj słówko")
            print("3.3 słowa dnia")
            print("4.Nauka")
            print("5.Wyjśćie")
            wybor = int(input("Wpisz numer: "))
            if wybor == 1:
                slowko = input("Wpisz słówko: ")
                if len(slowko) < 2:
                    print('-----------------')
                    print("Nie wpisano żadnego słowa lub jest ono za krótkie ")
                    print('-----------------')
                else:
                    translation = translator.translate(slowko)
                    print('-----------------')
                    print('Tłumaczenie: ')
                    print(slowko + ' - ' + translation)
                    print('-----------------')
            elif wybor == 2:
                losowe_slowa = ['Narazie', 'Dobranoc', 'Kocham', 'Programowanie', 'Kopanie']
                losowe_slowo = random.choice(losowe_slowa)
                translation = translator.translate(losowe_slowo)
                print('-----------------')
                print('Tłumaczenie: ')
                print(losowe_slowo + ' - ' + translation)
                print('-----------------')
            elif wybor == 3:
                slowa_dnia = ['Mróz', 'Pies', 'Krowa', 'Kogut', 'Marchewka']
                slowo_dnia = []

                # Sprawdź, czy minęło co najmniej 24 godziny od ostatniego losowania słowa dnia
                if os.path.exists('last_day_word.pickle'):
                    with open('last_day_word.pickle', 'rb') as f:
                        last_day_word = pickle.load(f)
                    if (datetime.datetime.now() - last_day_word).days < 1:
                        print('Słowo dnia zostało już wylosowane dzisiaj. Spróbuj ponownie jutro.')
                        return
                last_day_word = datetime.datetime.now()
                with open('last_day_word.pickle', 'wb') as f:
                    pickle.dump(last_day_word, f)

                for i in range(3):
                    losowe = random.choice(slowa_dnia)
                    slowo_dnia.append(losowe)
                    slowa_dnia.remove(losowe)

                print('-----------------')
                print(slowo_dnia[0] + ' - ' + translator.translate(slowo_dnia[0]))
                print(slowo_dnia[1] + ' - ' + translator.translate(slowo_dnia[1]))
                print(slowo_dnia[2] + ' - ' + translator.translate(slowo_dnia[2]))
                print('-----------------')
            elif wybor == 4:
                print("Kategoria: ")
                print("1.Dom")
                print("2.Zwierzęta")
                print("3.Jedzenie")
                wybor_kategorii = int(input("Wybierz numer: "))
                if wybor_kategorii == 1:
                    Dom = ['Łóżko', 'Poduszka', 'Lodówka', 'Pralka', 'Kuchnia', 'Salon', 'Łazienka', 'Kanapa']
                    for i, slowo in enumerate(Dom, 1):
                        print(str(i) + '.' + slowo + ' - ' + translator.translate(slowo))
                elif wybor_kategorii == 2:
                    Zwierzeta = ['Krowa', 'Pies', 'Kogut', 'Kura', 'Ryba', 'Kot', 'Sroka', 'Żółw', 'Mors']
                    for i, slowo in enumerate(Zwierzeta, 1):
                        print(str(i) + '.' + slowo + ' - ' + translator.translate(slowo))
                elif wybor_kategorii == 3:
                    Jedzenie = ['Chleb', 'Bułka', 'Szynka', 'Banan', 'Jabłko', 'Mandarynka', 'Jajko']
                    for i, slowo in enumerate(Jedzenie, 1):
                        print(str(i) + '.' + slowo + ' - ' + translator.translate(slowo))
            elif wybor == 5:
                exit()
            else:
                print('-----------------')
                print("Podano liczbę spoza zakresu")
                print('-----------------')
        except ValueError:
            print("Błąd: Proszę podać liczbę z podanego zakresu")
        except:
            print("Wystąpił błąd proszę się upewnić, że wszystko zostało wprowadzone poprawnie")
            
if __name__ == "__main__":
    main()
