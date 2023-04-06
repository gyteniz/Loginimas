"""
3.

Perdaryti 2 užduoties programą, kad:

Būtų sukurtas savo logeris, kuris fiksuotų visus anksčiau aprašytus pranešimus
Sukurtas logeris ne tik išsaugotų pranešimus faile, bet ir atvaizduotų juos konsolėje

"""
import logging
import math

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('uzd3.log')
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def sk_suma(*args):
    suma = sum(args)
    logger.info(f"Skaiciu {args} suma lygi: {suma}")
    return suma


def kvad_saknis(skaicius):
    try:
        saknis = math.sqrt(skaicius)
        logger.info(f"Skaiciaus {skaicius} kvadratine saknis: {saknis}")
        return saknis
    except TypeError:
        logger.exception(f"Klaida: {TypeError.__name__} - bloga ivestis.")

def sak_simboliai(sakinys):
    logger.info(f"Sakinys turi {len(sakinys)} simboliu.")
    return len(sakinys)


def dalyba(x, y):
    try:
        rezultatas = x / y
        logger.info(f"Skaiciaus {x} padalinimas is {y} lygu {rezultatas}")
        return x / y
    except ZeroDivisionError:
        logger.exception(f"Klaida: {ZeroDivisionError.__name__} - dalyba is nulio negalima.")
    else:
        return rezultatas





sk_suma(12, 45, 9, 6, 7, 123)
kvad_saknis("asd")
sak_simboliai("Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:")
dalyba(81, 0)





# def dalyba(a, b):
#     try:
#         rezultatas = a / b
#
#     except ZeroDivisionError:
#         logger.exception("Dalyba is nulio")
#     else:
#         return rezultatas
#
#
#
# padalinom = dalyba(20, a)
# logger.info(f"Dalyba: {a} / {b} = {padalinom}")
