from enum import Enum

class Veiksmas(Enum):
    ĮVESTI = 1
    ATSPAUSDINTI = 2
    IŠEITI = 3


def atlikti_veiksma(veiksmas: Veiksmas):
    print(f"Veiksmas įvykdytas: {veiksmas.name}")
    # print(f"Veiksmas {veiksmas.value{[0]}}")


# Įvedimas ir funkcijos kvietimas:
for veiksmas in Veiksmas:
    print(f"{veiksmas.value} - {veiksmas.name}")

ivesta = int(input("Pasirinkite veiksmą: "))
atlikti_veiksma(Veiksmas(ivesta))