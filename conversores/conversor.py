def convertendoPorBase (value, base):
    binaryArr = []
    while True:
        resto = value % base
        quociente = value // base
        value = quociente
        binaryArr.append(str(resto))
        if (quociente < base):
            binaryArr.append(str(quociente))
            break
    binaryArr = list(reversed(binaryArr))
    return "".join(binaryArr)