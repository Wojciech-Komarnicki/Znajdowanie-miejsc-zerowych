import math

lista_liniowa = []
lista_kwadratowa = []

while True:
    print(
        "------------------------------------------------------------------------------------------------------------------")

    while True:
        try:
            d = int(input("Chcesz policzyć miejsca zerowe dla funkcji liniowej (wpisz 1) czy kwadratowej?(wpisz 2): "))
            break
        except ValueError:
            print("Błąd: Proszę wpisać cyfrę (1 lub 2). Spróbuj ponownie.")

    if d == 1:
        while True:
            try:
                a = float(input("Wpisz współczynnik 'a' = "))
                if a == 0:
                    print("'a' nie może być równe 0")
                else:
                    break
            except ValueError:
                print("Błąd: Proszę wpisać poprawną liczbę dla 'a'.")

        while True:
            try:
                b = float(input("Wpisz współczynnik 'b' = "))
                break
            except ValueError:
                print("Błąd: Proszę wpisać poprawną liczbę dla 'b'.")

        x0 = -b / a
        print(f"Miejce zerowe tej funkcji to: {x0}\n")
        lista_liniowa.append([x0])
        print(f"Nasza lista zawiera teraz elemnty: {lista_liniowa}")

    elif d == 2:
        print("Wypisz współczynniki do funkcji kwadratowej a*x^2 + b*x + c\n")

        while True:
            try:
                a = float(input("Wpisz współczynnik 'a' = "))
                if a == 0:
                    print("'a' nie może być równe 0. Spróbuj ponownie.")
                else:
                    break
            except ValueError:
                print("Błąd: Proszę wpisać poprawną liczbę dla 'a'.")

        while True:
            try:
                b = float(input("Wpisz współczynnik 'b' = "))
                break
            except ValueError:
                print("Błąd: Proszę wpisać poprawną liczbę dla 'b'.")

        while True:
            try:
                c = float(input("Wpisz współczynnik 'c' = "))
                break
            except ValueError:
                print("Błąd: Proszę wpisać poprawną liczbę dla 'c'.")

        delta = b ** 2 - 4 * a * c

        if delta < 0:
            print("\nDelta jest mniejsza od zera.\nBrak miejsc zerowych")

        elif delta == 0:
            x0 = (-b) / (2 * a)
            print(f"\nDelta jest równa 0.\nMiejsce zerowe tej funkcji to: {x0}\n")
            lista_kwadratowa.append([x0])
            print(f"Nasza lista zawiera teraz elemnty: {lista_kwadratowa}")
        else:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            print(f"\nDelta jest większa od 0.\nMiejsca zerowe tej funkcji to: {x1}, {x2}\n")
            lista_kwadratowa.append([x1, x2])
            print(f"Nasza lista zawiera teraz elemnty: {lista_kwadratowa}")

    else:
        print("Błąd: Wpisz 1 lub 2!")
