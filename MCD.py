def euclides(num1,num2,iteracciones=1):
 
    if num1<num2:
        num1,num2=num2,num1
 

    resto=num1%num2
 
    if resto==0:
        return (num2,iteracciones)
 
    return euclides(num2,resto,iteracciones+1)
 
num1=24
num2=62
 
comunDivisor,iteracciones=euclides(num1,num2)
 
print("El comun divisor de {} y {} es {}".format(num1,num2,comunDivisor))
print("Se ha encontrado en {} iteracciones".format(iteracciones))