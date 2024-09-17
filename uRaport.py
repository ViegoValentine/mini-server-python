#-*- coding: utf-8 -*-
import datetime
import sys

def czytaj_dane_z_pliku(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            linie = plik.readlines()
            return [linia.strip() for linia in linie]
    except FileNotFoundError:
        print(f"Nie mozna odnalezc pliku o nazwie '{nazwa_pliku}'")
        return None

def zapisz_do_html(funkcja_kwadratowa, wyniki, nazwa_pliku):
    with open(nazwa_pliku, 'w') as plik_html:
        plik_html.write("<html>\n")
        plik_html.write("<head><title>"+nazwa_pliku+"</title></head>\n")
        plik_html.write("<body>\n")
        plik_html.write("<h1>"+nazwa_pliku+"</h1>\n")

        # Dodaj funkcjê kwadratow¹ do raportu
        plik_html.write(f"<p>{funkcja_kwadratowa}</p>\n")

        plik_html.write("<table border='1'>\n")
        plik_html.write("<tr><th>Argument</th><th>Wynik</th></tr>\n")

        for wynik in wyniki:
            argument, wartosc = wynik.split(": ")
            plik_html.write(f"<tr><td>{argument}</td><td>{wartosc}</td></tr>\n")

        plik_html.write("</table>\n")
        plik_html.write("</body>\n")
        plik_html.write("</html>\n")

if __name__ == "__main__":
    # Wczytaj funkcjê kwadratow¹ i wartoœci z pliku wyjœciowego
    if len(sys.argv) != 2:
        sys.exit(1)

    nazwa_raportu = sys.argv[1]
    dane_obliczen = czytaj_dane_z_pliku("wyjsciowe.txt")

    if dane_obliczen is not None and len(dane_obliczen) >= 2:
        try:
            funkcja_kwadratowa = dane_obliczen[0]
            wyniki_obliczen = dane_obliczen[1:]

            zapisz_do_html(funkcja_kwadratowa, wyniki_obliczen, nazwa_raportu+".html")
            print(f"Raport zostal zapisany do pliku {nazwa_raportu}.html")

        except ValueError:
            print("Blad konwersji danych na odpowiedni format")
