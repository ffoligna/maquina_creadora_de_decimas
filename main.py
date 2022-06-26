from random import choice
from time import sleep
from almafuerte import almafuerte_01, almafuerte_02
from aznar import aznar_01, aznar_02
from drexler import drexler_01, drexler_02, drexler_03
from zitarrosa import zitarrosa_01, zitarrosa_02, zitarrosa_03
from menus import menu_principal, acerca_del_proyecto
from os import system

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
    print("""### Décima Aleatoria ###
    """)
    for i in range(10):
        e = choice(estrofa)
        print(f"{i+1} {e[i]}")
        sleep(0.5)
    print("""
### Volverá al menú principal en 15 segundos ###""")

# Función limpiar pantalla
def limpiar_pantalla():
    system("clear")

# Programa principal
while True:
    limpiar_pantalla()
    menu = input(menu_principal)

    while menu not in ["1", "2", "3"]:
        print(f"""
########## Error!!! ##########
Sólo se puede elegir 1, 2 o 3.
##############################
""")
        menu = input(menu_principal)

    if menu == "1":
        limpiar_pantalla()
        maquina_de_decimas()
        sleep(15)
    elif menu == "2":
        limpiar_pantalla()
        for x in acerca_del_proyecto:
            print(x, end='', flush=True)
            sleep(0.05)
        sleep(10)
    elif menu == "3":
        break
    