#---------  Importaciones --------
from src.errores import main as mostrarErrores
from time import sleep
from src.extras import limpiar,pausar
import src.menus as menus


#---------  Funciones --------
def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    mostrar_menu = True
    valor_real = 0
    valor_obtenido = 0
    while mostrar_menu:
        limpiar()
        opc = menus.principal()
        if opc != 4:
            if opc == 1:
                valor_real = menus.numero()
            elif opc == 2:
                valor_obtenido = menus.numero()
            elif opc == 3:
                limpiar()
                mostrarErrores(valor_real,valor_obtenido)
                pausar()
        else:
            print('Adios')
            sleep(.5)
            mostrar_menu = False

if __name__ == "__main__":
    main()
