def multiplicacion (v1,v2,*lista):
    multiplicacion = v1 * v2
    for x in range(len(lista)):
        multiplicacion = multiplicacion*lista[x]
    return multiplicacion


print("Si sabemos que las placas de los vehiculos de Guatemala estan formadas por 3 digitos segidos por 3 letras")
print("¿cuantas placas pueden emitirse e el pais?")
print("se pueden formar")
print(multiplicacion(27,26,25,10,9,8))
print("sin repetir letras ni codigos")
