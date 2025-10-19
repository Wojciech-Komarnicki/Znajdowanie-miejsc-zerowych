Jasne, oto krótki opis Twojego projektu w formacie, który idealnie nadaje się do pliku **`README.md`** na GitHubie.

-----

# 📐 Kalkulator Miejsc Zerowych (Liniowa i Kwadratowa)

Prosty i interaktywny skrypt konsolowy napisany w Pythonie, służący do obliczania miejsc zerowych dla funkcji liniowych ($y=ax+b$) i kwadratowych ($y=ax^2+bx+c$).

## Kluczowe Funkcjonalności

  * **Obsługa Dwóch Typów Funkcji:** Użytkownik wybiera, czy chce policzyć miejsca zerowe funkcji **liniowej** (wymaga współczynników $a$ i $b$) czy **kwadratowej** (wymaga współczynników $a$, $b$ i $c$).
  * **Walidacja:** Program sprawdza, czy współczynnik $a$ nie jest równy $0$ dla obu typów funkcji.
  * **Kompleksowa Obsługa $\Delta$:** Poprawnie rozpoznaje i oblicza pierwiastki dla $\Delta < 0$ (brak), $\Delta = 0$ (jeden pierwiastek) i $\Delta > 0$ (dwa pierwiastki).
  * **Historia Wyników:** Wszystkie obliczone miejsca zerowe są przechowywane i wyświetlane w liście **`lista`** w trakcie działania programu.

## Jak Uruchomić?

1.  Upewnij się, że masz zainstalowanego Pythona 3.x.

2.  Uruchom plik z terminala:

    ```bash
    python nazwa_pliku.py 
    # np. python miejsca_zerowe.py
    ```

3.  Postępuj zgodnie z instrukcjami wyświetlanymi w konsoli.
