import json

def adivinanza(dicc, iniciales):
    costo_total = 0
    elemento_seleccionado = ""
    for i in iniciales:
        if i in dicc:
            costo_total += dicc[i]
            elemento_seleccionado += i
    print(costo_total)
    print(" ".join(elemento_seleccionado))
    
def main():
    dicc = json.loads(input())
    iniciales = input().split(" ")
    adivinanza(dicc, iniciales)
    
if __name__ == '__main__':
    main()
