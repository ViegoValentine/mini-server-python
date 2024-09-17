#-*- coding: utf-8 -*-

import cmath

def czytaj_dane_z_pliku(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            linie = plik.readlines()
            return [linia.strip() for linia in linie]
    except FileNotFoundError:
        print(f"Nie mozna odnalezc pliku o nazwie '{nazwa_pliku}'")
        return None

def oblicz_funkcje_kwadratowa(a, b, c, x):
    return a * x**2 + b * x + c

def zapisz_do_txt(wyniki, nazwa_pliku, a, b, c):
    with open(nazwa_pliku, 'w') as plik_txt:
        plik_txt.write(f"Funkcja kwadratowa: f(x) = {a}x^2 + {b}x + {c}\n")
        for argument, wynik in wyniki:
            plik_txt.write(f"{argument}: {wynik}\n")

def main_obliczenia():

    # Wczytaj wspó³czynniki i argumenty z pliku
    dane = czytaj_dane_z_pliku("wejsciowe.txt")

    if dane is not None and len(dane) >= 4:
        try:
            # Konwertuj wspó³czynniki na liczby zmiennoprzecinkowe
            a = float(dane[0])
            b = float(dane[1])
            c = float(dane[2])
            
            print(f"Funkcja kwadratowa: f(x) = {a}x^2 + {b}x + {c}")

            # Wczytaj argumenty
            argumenty = [complex(arg) for arg in dane[3:]]

            wyniki = []

            # Oblicz wartoœci funkcji dla argumentów
            for argument in argumenty:
                wynik = oblicz_funkcje_kwadratowa(a, b, c, argument)
                print(f"Wartosc funkcji dla {argument}: {wynik}")

                wyniki.append((argument, wynik))

            zapisz_do_txt(wyniki, "wyjsciowe.txt", a, b, c)
            print(f"Wyniki zostaly zapisane do pliku wyjsciowe.txt")

        except ValueError:
            print("Blad konwersji wspolczynnikow na liczby")

if __name__ == "__main__":
    main_obliczenia()
