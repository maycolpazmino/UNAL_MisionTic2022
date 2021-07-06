def conversion_lista_str():
    lista = input().split(' ')
    return lista

def elementos_repetidos(lista):
    for i in range(len(lista)-1):
        if lista[i] == (lista[i+1]):
            pass
        if lista[i] != lista[i+1]:
            print(lista[i], end=' ')
    print(lista[-1], end='')
    
def cantidad_repetidos(lista):
    from itertools import groupby
    lista = [len(list(group)) for key, group in groupby(lista)]
    for i in range(len(lista)):
        print(lista[i], end= ' ')
        
def main():
    lista = conversion_lista_str()
    elementos_repetidos(lista)
    print('')
    cantidad_repetidos(lista)
    
main()
