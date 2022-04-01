def menuCalculadora():
    print("=========CALCULADORA=================")
    print("Seleccione una operacion: \n 1-Suma  \n 2-Resta \n 3-Mutiplicacion \n 4- Division \n 5- Salir")
    operacion = int(input("Digite su opcion: "))
    if operacion == 5: quit()
    num1 = float(input('Ingresa el primer numero: '))
    num2 = float(input('Ingresa el segundo numero: '))
    calculadora(operacion,num1,num2)
    return menuCalculadora()

def calculadora(operacion, num1, num2):
    def suma(num1, num2):
        return num1 + num2

    suma2= lambda num1,num2: num1+num2

    def resta(num1, num2):
        return num1 - num2

    def multiplicacion(num1, num2):
        return num1 * num2

    def division(num1, num2):
        return num1 / num2

    switch_operacion = {
        1: suma2(num1, num2),
        2: lambda num1, num2 : num1 - num2,
        3: multiplicacion(num1, num2),
        4: division(num1, num2),

    }

    return print("el resultado es: " + str(switch_operacion.get(operacion, "invalido")) + '\n')