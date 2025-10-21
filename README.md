# 📐 Kalkulator Miejsc Zerowych (Liniowa i Kwadratowa)

Prosty i interaktywny skrypt konsolowy napisany w Pythonie, służący do obliczania miejsc zerowych dla funkcji liniowych ($y=ax+b$) i kwadratowych ($y=ax^2+bx+c$).

## Kluczowe Funkcjonalności

* **Obsługa Dwóch Typów Funkcji:** Użytkownik wybiera, czy chce policzyć miejsca zerowe funkcji **liniowej** (wymaga współczynników $a$ i $b$) czy **kwadratowej** (wymaga współczynników $a$, $b$ i $c$).
* **Wysoka Odporność na Błędy Wejścia (Input Validation):** Zastosowano mechanizmy `try-except`, które **zapobiegają awarii programu** w przypadku podania tekstu zamiast liczby (np. wpisanie "lol" dla współczynnika $a$).
* **Powtarzanie Zapytania:** Po wykryciu niepoprawnych danych wejściowych lub podaniu $a=0$, program **automatycznie ponawia zapytanie** o dany współczynnik, aż do momentu podania poprawnej wartości.
* **Walidacja $a \neq 0$:** Program rygorystycznie sprawdza, czy współczynnik $a$ nie jest równy $0$ dla obu typów funkcji, wymuszając poprawne dane.
* **Kompleksowa Obsługa $\Delta$:** Poprawnie rozpoznaje i oblicza pierwiastki dla $\Delta < 0$ (brak), $\Delta = 0$ (jeden pierwiastek) i $\Delta > 0$ (dwa pierwiastki).
* **Historia Wyników:** Wszystkie obliczone miejsca zerowe są przechowywane i wyświetlane w liście **`lista_liniowa`** oraz **`lista_kwadratowa`** w trakcie działania programu, oddzielnie dla każdego typu funkcji.
