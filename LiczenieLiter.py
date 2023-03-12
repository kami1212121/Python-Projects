plik = open("test.txt", "r")
tekst = plik.read()
plik.close()
def policz(txt,znak):
    licznik = 0
    for z in txt:
        if z == znak:
            licznik += 1
    return licznik
print(policz(tekst,"l") + policz(tekst,"L")) #Zwraca uwage na wielkość liter
print(policz(tekst.lower(), "l")) #2 Sposób aby policzyć nie zwracająć uwagi na wielkość liter

for znak in "abcdefghijklmnoprstuwyz":
    ile = policz(tekst.lower(), znak)
    procent = 100 * ile / len(tekst)
    print("{0}, {1}, {2}%".format(znak, ile, round(procent, 2)))
