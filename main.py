from random import choice
from time import sleep
from almafuerte import almafuerte_01, almafuerte_02
from aznar import aznar_01, aznar_02
from drexler import drexler_01, drexler_02, drexler_03
from zitarrosa import zitarrosa_01, zitarrosa_02, zitarrosa_03


# Lista de estrofas
estrofa = [
    almafuerte_01,
    almafuerte_02,
    aznar_01,
    aznar_02,
    drexler_01,
    drexler_02,
    drexler_03,
    zitarrosa_01,
    zitarrosa_02,
    zitarrosa_03
]

# Función que imprime una linea aleatoria de una estrofa aleatoria
def maquina_de_decimas():
    for i in range(10):
        e = choice(estrofa)
        print(f"{i+1} {e[i]}")
        sleep(1)

maquina_de_decimas()
