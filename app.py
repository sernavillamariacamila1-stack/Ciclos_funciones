#ejercicio 1

def sumar_hasta_cero():
    total = 0 

    while True:
        try:
            numero = float(input("Ingrese un número (0 para terminar): "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
            continue 

        if numero == 0:
            break  
        total += numero 

    print(f"La suma total de los números ingresados es: {total}")

 #ejercicio 2
if __name__ == "__main__":
    sumar_hasta_cero()


    numero_secreto = 9
    numero_usuario = 0
    while numero_secreto != numero_usuario:
        try:
            numero_usuario = int(input("Adivina el número secreto (entre 1 y 10): "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
            continue  # Volver a pedir el número

        if numero_usuario < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        elif numero_usuario > numero_secreto:
            print("El número secreto es menor. Intenta de nuevo.")

    print("¡Felicidades! Has adivinado el número secreto.") 


#ejercicio 3
def contador_regresivo(inicio=10):
    """
    Realiza un conteo regresivo desde 'inicio' hasta 1
    y luego imprime '¡DESPEGUE!'.
    """
    if not isinstance(inicio, int) or inicio < 1:
        raise ValueError("El valor inicial debe ser un entero mayor o igual a 1.")
    for numero in range(inicio, 0, -1):
        print(numero)

    
    print("¡DESPEGUE!") 


if __name__ == "__main__":
    try:
        contador_regresivo(10)
    except ValueError as e:
        print(f"Error: {e}")    

#ejercicio 4    
numero = int(input("Please enter a number: "))

i = 1

print(f"\nla multiplicacion de {numero} es:")
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1

#ejercicio 5
def imprimir_pares(inicio: int, fin: int):
    """
    Imprime los números pares en el rango [inicio, fin].
    """
    if not isinstance(inicio, int) or not isinstance(fin, int):
        raise ValueError("Los valores de inicio y fin deben ser enteros.")
    if inicio > fin:
        raise ValueError("El valor de inicio no puede ser mayor que el de fin.")
#ejercicio 6
    print(f"Números pares del {inicio} al {fin}:")
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            print(numero, end=" ")
    print()
if __name__ == "__main__":
    try:
        imprimir_pares(1, 20)
    except ValueError as e:
        print(f"Error: {e}")

numeros = [4, 7, 2, 9, 1, 5]
suma_total = sum(numeros)
print("La suma total usando sum() es:", suma_total)
suma_total_bucle = 0
for numero in numeros:
    suma_total_bucle += numero      
#EJercicio  7       


niveles = 5

for i in range(1, niveles + 1): 
    espacios = " " * (niveles - i)
    asteriscos = "*" * (2 * i - 1)  
    print(espacios + asteriscos)
   
#ejercicio 8

texto = "Programando en Python"
vocales = "aeiouáéíóú"

cantidad = sum(1 for letra in texto.lower() if letra in vocales)
print(f"Total de vocales: {cantidad}")

#ejercicio 9
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo multiplicando base por altura."""
    return base * altura
try:
    medida_base = float(input("Ingresa la base del rectángulo: "))
    medida_altura = float(input("Ingresa la altura del rectángulo: "))
    
   
    area = calcular_area_rectangulo(medida_base, medida_altura)
    

    print(f"El área del rectángulo es: {area}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa números válidos para la base y la altura.")     


#ejercicio 10

def es_par(numero):
     if numero % 2 == 0:
        return True  
     else:
        return False 
numero_a_probar = 7 

if es_par(numero_a_probar):
    print(f"{numero_a_probar} es par")
else:
    print(f"{numero_a_probar} es impar")

    #ejercicio 11

    def celsius_a_fahrenheit(celsius):
      return (celsius * 1.8) + 32

grados_c = 25
grados_f = celsius_a_fahrenheit (grados_c)
print(f"{grados_c}°C son {grados_f}°F") 

#ejercicio 12
def crear_tarjeta(nombre, rol="Estudiante", activo=True):
    estado = "Activo" if activo else "Inactivo"
    return f"--- Tarjeta ---\nNombre: {nombre}\nRol: {rol}\nEstado: {estado}\n-------------"
print(crear_tarjeta("Juan_pablo", "Estudiante"))    
print(crear_tarjeta("camila", "Profesor")) 
print(crear_tarjeta("maria", "directora"))  
print(crear_tarjeta("rua", "deportista" ))
 
#ejercicio 13

print("--- Calculadora de Propinas ---")
cuenta = float(input("¿Cuál es el total de la cuenta? $"))
porcentaje = int(input("¿Qué porcentaje de propina deseas dejar? (ej. 10, 15, 20): "))
personas = int(input("¿Entre cuántas personas se dividirá la cuenta? "))

total_propina = cuenta * (porcentaje / 100)
total_cuenta = cuenta + total_propina
pago_por_persona = total_cuenta / personas

print(f"\n--- Resumen ---")
print(f"Propina total: ${total_propina:.2f}")
print(f"Total a pagar: ${total_cuenta:.2f}")
print(f"Cada persona debe pagar: ${pago_por_persona:.2f}") 

#ejercicio 14
 
def analizar_numeros(lista):
    if not lista:
        return "La lista está vacía."

    total_elementos = len(lista)
    suma = sum(lista)
    promedio = suma / total_elementos
    numero_mayor = max(lista)
    numero_menor = min(lista)
    
    pares = sum(1 for n in lista if n % 2 == 0)
    impares = total_elementos - pares

    resultado = f"""
    --- Análisis de la Lista ---
    Elementos totales: {total_elementos}
    Suma total: {suma}
    Promedio: {promedio}
    Número mayor: {numero_mayor}
    Número menor: {numero_menor}
    Cantidad de pares: {pares}
    Cantidad de impares: {impares}
    --------------------------
    """
    return resultado

    mis_numeros = [45, 12, 89, 34, 7, 22, 100]
print(analizar_numeros(numeros))

#ejercicio 15
import random
import re
def main():
    passwd = "xpabloxP@ssw0rd"
    reg = r"^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$#%])[A-Za-z\d@$#%]{6,20}$"


    pat = re.compile(reg)

    mat = re.search(pat, passwd)

    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")

        if __name__ == '_main_':
          main() 

#ejercicio 16


def juego_adivinanzas():
    """
    Juego de adivinanzas mejorado:
    - El sistema elige un número aleatorio.
    - El jugador tiene un número limitado de intentos.
    - Se dan pistas progresivas.
    """
    print("🎯 Bienvenido al Juego de Adivinanzas Mejorado 🎯")
    
    
    numero_secreto =  random.randint(1, 100)
    intentos_maximos = 7
    intentos_realizados = 0

    while intentos_realizados < intentos_maximos:
        try:
            # Solicitar número al usuario
            intento = int(input(f"Intento {intentos_realizados + 1}/{intentos_maximos} - Ingresa un número entre 1 y 100: "))
            
            # Validar rango
            if intento < 1 or intento > 100:
                print("⚠️ Por favor, ingresa un número dentro del rango 1-100.")
                continue

            intentos_realizados += 1

            
            if intento == numero_secreto:
                print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos_realizados} intentos.")
                break
            else:
                
                if intento < numero_secreto:
                    print("🔼 El número secreto es mayor.")
                else:
                    print("🔽 El número secreto es menor.")

            
                if intentos_maximos - intentos_realizados == 2:
                    if numero_secreto % 2 == 0:
                        print("💡 Pista: El número es par.")
                    else:
                        print("💡 Pista: El número es impar.")

        except ValueError:
            print("⚠️ Entrada inválida. Debes ingresar un número entero.")

    else:
        print(f"❌ Se acabaron los intentos. El número secreto era {numero_secreto}.")


if __name__ == "__main__":
    juego_adivinanzas()
    
    #ejercicio 17
tareas = []


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 40)
    print("GESTOR DE TAREAS".center(40))
    print("=" * 40)
    print("1. Agregar tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar como completada")
    print("4. Eliminar tarea")
    print("5. Buscar tarea")
    print("6. Estadísticas")
    print("7. Salir")
    print("=" * 40)


def agregar_tarea(lista_tareas):
    """
    Agrega una nueva tarea a la lista.
    Una tarea es un diccionario con:
    - descripcion: str
    - completada: bool
    - prioridad: str ("alta", "media", "baja")
    """
    descripcion = input("\nDescripción de la tarea: ")

    print("Prioridad:")
    print("1. Alta")
    print("2. Media")
    print("3. Baja")

    opcion = input("Elige (1-3): ")

    prioridades = {
        "1": "alta",
        "2": "media",
        "3": "baja"
    }

    prioridad = prioridades.get(opcion, "media")

    tarea = {
        "descripcion": descripcion,
        "completada": False,
        "prioridad": prioridad
    }

    lista_tareas.append(tarea)
    print(f"Tarea agregada con prioridad {prioridad}")


def mostrar_tareas(lista_tareas):
    """Muestra todas las tareas numeradas"""

    if len(lista_tareas) == 0:
        print("\nNo hay tareas registradas")
        return

    print("\n" + "=" * 60)
    print("LISTA DE TAREAS".center(60))
    print("=" * 60)

    for i, tarea in enumerate(lista_tareas, 1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        prioridad = tarea["prioridad"].upper()

        print(f"{i}. {estado} [{prioridad}] {tarea['descripcion']}")

    print("=" * 60)


def marcar_completada(lista_tareas):
    """Marca una tarea como completada"""

    mostrar_tareas(lista_tareas)

    if len(lista_tareas) == 0:
        return

    try:
        num = int(input("\n¿Qué tarea completaste? (número): "))

        if 1 <= num <= len(lista_tareas):
            lista_tareas[num - 1]["completada"] = True
            print("¡Tarea marcada como completada!")
        else:
            print("Número inválido")

    except ValueError:
        print("Debes ingresar un número")


def eliminar_tarea(lista_tareas):
    """Elimina una tarea de la lista"""

    mostrar_tareas(lista_tareas)

    if len(lista_tareas) == 0:
        return
    try:
        num = int(input("\n¿Qué tarea quieres eliminar? (número): "))

        if 1 <= num <= len(lista_tareas):
            lista_tareas.pop(num - 1)
            print("¡Tarea eliminada!")
        else:
            print("Número inválido")

    except ValueError:
        print("Debes ingresar un número")
 
 #ejercicio 18

    print ("programa que calcule el factorial")
    numero = int(input("intrduzca el numero"))

    factorial = 1
    i=1
    while (i <= numero ):
        factorial  = factorial * i
        i = i +1 
        print ("el factorial de ",numero, "es" , factorial)

#ejercicio 19

n = 10
a, b = 0, 1

fibonacci_numbers = []

for _ in range(n):  
    fibonacci_numbers.append(str(a)) 
    a, b = b, a + b

print(' '.join(fibonacci_numbers))
 
 #ejercicio 20


numero = 12345
numero_invertido = int(str(numero)[::-1])
print(numero_invertido)

#ejercicio 20

import math

def es_primo(numero):
    
    if numero <= 1:
        return False
    
    
    limite = int(math.isqrt(numero))
    
    for i in range(2, limite + 1):
        if numero % i == 0:
            return False
            
    return True

#ejercicio 21

