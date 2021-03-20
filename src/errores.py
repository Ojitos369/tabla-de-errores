from src.extras import limpiar, pausar

def mostrar(real,preob,n):
    obtenidostr = str(preob)
    obtenido = ''
    j=0
    decimales = 0
    avanzar = False
    while decimales <= n+1:
        try:
            obtenido = f'{obtenido}{obtenidostr[j]}'
            if obtenidostr[j] == '.':
                avanzar = True
            if avanzar:
                decimales += 1
        except:
            break
        j += 1
    obtenido = float(obtenido)
    absoluto = obtenido-real
    if absoluto < 0:
        absoluto *= -1
    relativo = absoluto/real
    porcentaje =  relativo * 100
    #obtenido = '{:.8f}'.format(obtenido)
    absoluto = '{:.8f}'.format(absoluto)
    relativo = '{:.8f}'.format(relativo)
    porcentaje = '{:.8f}'.format(porcentaje)
    print(f'{obtenido}\t\t{absoluto}\t\t{relativo}\t\t{porcentaje}%')

def main(real,obtenido):
    if real != 0:
        print(f'valor real: {real}\nvalor obtenido: {obtenido}')
        print(f'Tomado\t\tAbsoluto\t\tRelativo\t\tPorcentaje')
        for i in range(5):
            mostrar(real,obtenido,i)
