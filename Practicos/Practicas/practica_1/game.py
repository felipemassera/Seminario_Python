from random import choice, randrange
from datetime import datetime

# variable contadora de aciertos
aciertos = 0
print(f"aciertos {aciertos}")
# Operadores posibles
operators = ["+", "-", "/", "*"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    if (operator != "/") or (number_2 != 0):
        result = int(input("resultado: "))
        match operator:
            case "+":
                if (number_1 + number_2) == result:
                    print("Respuesta correcta")
                    aciertos += 1
                else:
                    print("respuesta incorrecta")
            case "-":
                if result == (number_1 - number_2):
                    print("Respuesta correcta")
                    aciertos += 1
                else:
                    print("respuesta incorrecta")
            case "/":
                if result == round(number_1 // number_2):
                    print("Respuesta correcta")
                    aciertos += 1
                else:
                    print("respuesta incorrecta")
            case "*":
                if result == number_1 * number_2:
                    print("Respuesta correcta")
                    aciertos += 1
                else:
                    print("respuesta incorrecta")
    else:
        print("no se puede dividir por 0")
        aciertos += 1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(
    f"\n Tardaste {total_time.seconds} segundos. tuviste {aciertos} respuestas correctas."
)
