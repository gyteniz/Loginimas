"""
2.
Perdaryti 1 užduoties programą, kad:

Į šaknies funkciją padavus string tipo argumetrą, į log failą būtų išsaugoma
išimties klaida su norimu tekstu
Į dalybos funkciją antrą argumentą padavus 0, į log failą būtų išsaugoma
išimties klaida su norimu tekstu

Patarimas: panaudoti try/except/else, logging.exception()
    """

import math
import logging

logging.basicConfig(filename="uzd2.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def sk_suma(*args):
    suma = sum(args)
    logging.info(f"Skaiciu {args} suma lygi: {suma}")
    return suma


def kvad_saknis(skaicius):
    try:
        logging.info(f"Skaiciaus {skaicius} kvadratine saknis: {math.sqrt(skaicius)}")
        return math.sqrt(skaicius)
    except TypeError:
        logging.exception(f"Klaida: {TypeError.__name__} - bloga ivestis.")


def sak_simboliai(sakinys):
    logging.info(f"Sakinys turi {len(sakinys)} simboliu.")
    return len(sakinys)


def dalyba(x, y):
    try:
        rezultatas = x / y
        logging.info(f"Skaiciaus {x} padalinimas is {y} lygu {rezultatas}")
        return x / y
    except ZeroDivisionError:
        logging.exception(f"Klaida: {ZeroDivisionError.__name__} - dalyba is nulio negalima.")
    else:
        return rezultatas


sk_suma(12, 45, 9, 6, 7, 123)
kvad_saknis("asd")
sak_simboliai("Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:")
dalyba(81, 0)
