#-----------  IMPORTACIONES ----------------
from src.extras import pausar,limpiar, convertir, convertirFloat
#-----------  FUNCIONES ----------------
def principal():
    incorrecto = True
    while incorrecto:
        limpiar()
        print('https://github.com/Ojitos369/tabla-de-errores.git')
        opc = input('''1.- Ingresar valor Real
2.- Ingresar valor medido
3.- Mostrar tablas de errores
4.- Salir
Elige una opción: ''')
        opc = convertir(opc)
        if opc < 5 or opc > 0:
            incorrecto = False
        else:
            print('Opcion no valida. Intenta nuevamente. ')
            pausar()
    return opc

def numero():
    incorrecto = True
    while incorrecto:
        limpiar()
        opc = input('Ingresa un numero: ')
        opc = convertirFloat(opc)
        if opc:
            incorrecto = False
        else:
            print('Por favor ingresa un numero valido')
            pausar()
    return opc


