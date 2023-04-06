"""
1.
Sukurti funkcijas, kurios:

Gražintų visų paduotų skaičių sumą (su *args argumentu)
Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
Gražintų paduoto sakinio simbolių kiekį (su len())
Gražintų rezultatą, skaičių x padalinus iš y

Nustatyti standartinį logerį (logging) taip, kad jis:

Saugotų pranešimus į norimą failą
Saugotų INFO lygio žinutes
Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė
Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:

logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
Paleisti kiekvieną funkciją su norimais argumentais"""
import math
import logging

logging.basicConfig(filename="uzd1.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def sk_suma(*args):
    suma = sum(args)
    logging.info(f"Skaiciu {args} suma lygi: {suma}")
    return suma


def kvad_saknis(skaicius):
    logging.info(f"Skaiciaus {skaicius} kvadratine saknis: {math.sqrt(skaicius)}")
    return math.sqrt(skaicius)


def sak_simboliai(sakinys):
    logging.info(f"Sakinys turi {len(sakinys)} simboliu.")
    return len(sakinys)


def dalyba(x, y):
    logging.info(f"Skaiciaus {x} padalinimas is {y} lygu {x/y}")
    return x / y


sk_suma(12, 45, 9, 6, 7, 123)
kvad_saknis(169)
sak_simboliai("Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:")
dalyba(81, 9)