def factorRiesgo2(FD1):
    FD2 = int((FD1*2)+4)
    FD3 = int((FD1+FD2)/5)
    if FD3 >=0 and FD3 <=20:
        numeral = "uno"
    elif FD3 >=21 and FD3 <=30:
        numeral = "dos"
    elif FD3 >=30 and FD3 <=50:
        numeral = "tres"
    elif FD3 >=51:
        numeral = "cuatro"
    print(str(FD1) + ", " + str(FD2) + ", " + str(FD3))
    print(numeral)
    return
factorRiesgo2(FD1=int(input()))
