import math

while True:
    print("------------------------------------------------------------------------------------------------------------------")
    d = int(input("Chcesz policzyć miejsca zerowe dla funkcji liniowej (wpisz 1) czy kwadratowej?(wpisz 2): "))
    if d == 1:
        a = float(input("Wpisz współczynnik 'a' = "))
        while True:
            if a == 0:
                print("'a' nie może być równe 0")
                a = float(input("Wpisz współczynnik 'a' = "))
            else:
                break
        b = float(input("Wpisz współczynnik 'b' = "))
        x0 = -b/a
        print(f"Miejce zerowe tej funkcji to: {x0}")
    elif d == 2:
        print("Wypisz współczynniki do funkcji kwadratowej a*x^2 + b*x + c\n")
        a = float(input("Wpisz współczynnik 'a' = "))
        while True:
            if a == 0:
                print("'a' nie może być równe 0")
                a = float(input("Wpisz współczynnik 'a' = "))
            else:
                break
        b = float(input("Wpisz współczynnik 'b' = "))
        c = float(input("Wpisz współczynnik 'c' = "))
        delta = b**2 - 4*a*c
        if delta < 0:
            print("\nDelta jest mniejsza od zera.\nBrak miejsc zerowych")
        elif delta == 0:
            x0 = (-b + math.sqrt(delta)) / (2*a)
            print(f"\nDelta jest równa 0.\nMiejsce zerowe tej funkcji to: {x0}")
        else:
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            print(f"\nDelta jest większa od 0.\nMiejsca zerowe tej funkcji to: {x1}, {x2}")
    else:
        print("Proszę wpisać 1 lub 2")
