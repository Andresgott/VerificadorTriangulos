def triangulo():
    
    print("Bienvenido al verificador de triangulos, dependiendo de la longitud de los lados, te dire que tipo de triangulo es!!")
    ladoA=int(input("Porfavor ingrese la longitud del primer lado del triangulo: "))
    ladoB=int(input("Porfavor ingrese la longitud del segundo lado del triangulo: "))
    ladoC=int(input("Porfavor ingrese la longitud del tercer lado del triangulo: "))

    if ladoA==ladoB and ladoB==ladoC:
        print("Es un triangulo equilatero!!")
    else:
        if (ladoA!=ladoB and ladoB==ladoC) or (ladoA==ladoB and ladoB!=ladoC) :
            print("Es un triangulo Isosceles!!")
        else:
            print("Es un triangulo escaleno!!")    



triangulo()        
    