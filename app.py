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


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    choice = input("Enter choice(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

    #ejercicio 22



print("=== MENÚ DE CONVERSIÓN DE UNIDADES ===")
print("1) Convertir de Celsius a Fahrenheit")
print("2) De kilómetros a millas")
print("3) De kilogramos a libras")

opcion = int(input("\nElige una opción (1-3): "))


if opcion < 1 or opcion > 3:
    print("❌ Error: Opción no válida. Debe ser 1, 2 o 3.")
else:
    
    match opcion:
        case 1:
        
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"✅ {celsius}°C = {fahrenheit:.2f}°F")
        
        case 2:
            
            km = float(input("Ingresa la distancia en kilómetros: "))
            if km < 0:
                print("❌ Error: La distancia no puede ser negativa.")
            else:
                millas = km * 0.621371
                print(f"✅ {km} km = {millas:.2f} millas")
        
        case 3:
            
            kg = float(input("Ingresa el peso en kilogramos: "))
            if kg < 0:
                print("❌ Error: El peso no puede ser negativo.")
            else:
                libras = kg * 2.20462
                print(f"✅ {kg} kg = {libras:.2f} lb")

#ejercicio 23                

import re

def es_valido(email):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    return re.match(patron, email) is not None


correos = ["hola@dominio.com", "usuario#dominio.com", "contacto@empresa.co.uk"]

for correo in correos:
    print(f"{correo}: {'Válido' if es_valido(correo) else 'Inválido'}")

    #ejercicio 24


import string
import random

length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')

characterList = ""

while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
        characterList += string.digits
    elif(choice == 2):
        characterList += string.ascii_letters
    elif(choice == 3):
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
  
    randomchar = random.choice(characterList)
    
    password.append(randomchar)

print("The random password is " + "".join(password))

#ejercicio 25

from datetime import date

def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad

try:
    año = int(input("Introduce tu año de nacimiento (AAAA): "))
    mes = int(input("Introduce tu mes de nacimiento (MM): "))
    dia = int(input("Introduce tu día de nacimiento (DD): "))
    
    fecha_nac = date(año, mes, dia)
    print(f"Tienes {calcular_edad(fecha_nac)} años.")
except ValueError:
    print("Fecha no válida. Por favor, asegúrate de usar números correctos.")


    #ejercicio 26

    usuarios_registrados = {
    "juan": "clave123",
    "maria": "secreta456"
}

def login():
    username = input("Usuario: ")
    password = input("Contraseña: ")
    
    if username in usuarios_registrados and usuarios_registrados[username] == password:
        print(f"¡Inicio de sesión exitoso! Bienvenido, {username}.")
    else:
        print("Error: Usuario o contraseña incorrectos.")

login()


#ejercicio 27

"""
JUEGO DE PIEDRA PAPEL O TIJERA
"""
namej1 = input("ingrese el nombre del primer jugador")
namej2 = input("ingrese el nombre del segundo jugador")

print("Elige una opción",
      "1. Piedra",
      "2. Papel",
      "3. Tijera")

opcj1 = int(input("ingresa tu opción jugador 1"))
opcj2 = int(input("ingresa tu opcion jugador 2"))


if opcj1 == 1 and opcj2 == 2:
    print("el ganador es ", namej2)
elif opcj1 == 1 and opcj2 == 3:
    print("el ganador es", namej1)
elif opcj1 == 2 and opcj2 == 1:
    print("El ganador es ", namej1 )
elif opcj1 == 2 and opcj2 == 3:
    print("el ganador es ", namej2)
elif opcj1 == 3 and opcj2 == 1:
    print("el ganador es ", namej1)
elif opcj1 == 3 and opcj2 == 2:
    print("el ganador es ", namej1)
elif opcj1 == opcj2:
    print("Es un empate")


#ejercicio 28

def analizar_texto():
    texto = input("Ingresa un texto: ").lower()
    letras_input = input("Ingresa 3 letras separadas por espacio: ").lower()
    letras = letras_input.split()

    palabras = texto.split()
    total_palabras = len(palabras)
    total_caracteres = len(texto)

    contador_letras = {letra: texto.count(letra) for letra in letras}

    primera_palabra = palabras[0] if palabras else ""
    ultima_palabra = palabras[-1] if palabras else ""
    palabra_python = "python" in texto

    print("\n--- REPORTE DE ANÁLISIS ---")
    print(f"Total de palabras: {total_palabras}")
    print(f"Total de caracteres: {total_caracteres}")
    print(f"Frecuencia de las letras: {contador_letras}")
    print(f"Primera palabra: '{primera_palabra}' | Última palabra: '{ultima_palabra}'")
    print(f"¿Contiene la palabra 'python'?: {palabra_python}")

analizar_texto()

#ejercicio 29

def menu():
    """Muestra las opciones del menú."""
    print("\n" + "="*30)
    print("      LISTA DE COMPRAS")
    print("="*30)
    print("1. Ver lista")
    print("2. Agregar artículo")
    print("3. Eliminar artículo")
    print("4. Salir")
    print("="*30)

def gestionar_lista():
    """Lógica principal de la lista de compras."""
    lista = []
    
    while True:
        menu()
        opcion = input("\nSelecciona una opción (1-4): ")

        if opcion == '1':
            if not lista:
                print("\nTu lista está vacía.")
            else:
                print("\n--- TUS ARTÍCULOS ---")
                for index, item in enumerate(lista, start=1):
                    print(f"{index}. {item.capitalize()}")

        elif opcion == '2':
            articulo = input("\n¿Qué deseas agregar?: ").strip()
            if articulo:
                lista.append(articulo)
                print(f"'{articulo}' ha sido agregado.")
            else:
                print("No ingresaste un nombre válido.")

        elif opcion == '3':
            if not lista:
                print("\nNo hay artículos para eliminar.")
            else:
                print("\n--- TUS ARTÍCULOS ---")
                for index, item in enumerate(lista, start=1):
                    print(f"{index}. {item.capitalize()}")
                
                try:
                    num_eliminar = int(input("\nNúmero del artículo a eliminar: "))
                    if 1 <= num_eliminar <= len(lista):
                        eliminado = lista.pop(num_eliminar - 1)
                        print(f"'{eliminado.capitalize()}' ha sido eliminado.")
                    else:
                        print("Número fuera de rango.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")

        elif opcion == '4':
            print("\n¡Gracias por usar la lista de compras! ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo (1-4).")

if __name__ == "__main__":
    gestionar_lista()


#ejercicio 30

def menu():
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

def cajero():
    saldo = 1000.0  
    
    while True:
        menu()
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            print(f"\nSu saldo actual es: ${saldo:.2f}")
            
        elif opcion == "2":
            try:
                monto = float(input("\nIngrese la cantidad a depositar: $"))
                if monto > 0:
                    saldo += monto
                    print(f"¡Depósito exitoso! Su nuevo saldo es: ${saldo:.2f}")
                else:
                    print("Error: El monto debe ser mayor a cero.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                
        elif opcion == "3":
            try:
                monto = float(input("\nIngrese la cantidad a retirar: $"))
                if monto <= 0:
                    print("Error: El monto debe ser mayor a cero.")
                elif monto > saldo:
                    print("Error: Fondos insuficientes.")
                else:
                    saldo -= monto
                    print(f"¡Retiro exitoso! Su nuevo saldo es: ${saldo:.2f}")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                
        elif opcion == "4":
            print("\nGracias por utilizar nuestros servicios. ¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")



#ejercicio 31

class SistemaCalificaciones:
    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, nombre):
        """Agrega un nuevo estudiante al sistema."""
        if nombre in self.estudiantes:
            print("El estudiante ya existe.")
        else:
            self.estudiantes[nombre] = []
            print(f"Estudiante '{nombre}' agregado exitosamente.")

    def agregar_calificacion(self, nombre, nota):
        """Agrega una nota validando que esté entre 0 y 100."""
        if nombre not in self.estudiantes:
            print("Estudiante no encontrado.")
            return

        if 0 <= nota <= 100:
            self.estudiantes[nombre].append(nota)
            print(f"Nota {nota} agregada a {nombre}.")
        else:
            print("Error: La calificación debe estar entre 0 y 100.")

    def calcular_promedio(self, nombre):
        """Calcula el promedio de un estudiante específico."""
        notas = self.estudiantes.get(nombre, [])
        if not notas:
            return 0.0
        return sum(notas) / len(notas)

    def obtener_letra(self, promedio):
        """Asigna una letra basada en el promedio."""
        if promedio >= 90: return 'A'
        elif promedio >= 80: return 'B'
        elif promedio >= 70: return 'C'
        elif promedio >= 60: return 'D'
        else: return 'F'

    def generar_reporte_individual(self, nombre):
        """Muestra las notas y el promedio de un estudiante."""
        if nombre not in self.estudiantes or not self.estudiantes[nombre]:
            print("No hay información suficiente de este estudiante.")
            return

        notas = self.estudiantes[nombre]
        promedio = self.calcular_promedio(nombre)
        letra = self.obtener_letra(promedio)

        print(f"\n--- Reporte de {nombre} ---")
        print(f"Notas: {notas}")
        print(f"Promedio: {promedio:.2f}")
        print(f"Calificación: {letra}")

    def generar_reporte_general(self):
        """Muestra el promedio de todos los estudiantes."""
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
            return

        print("\n--- Reporte General de la Clase ---")
        total_clase = 0
        num_estudiantes = len(self.estudiantes)

        for nombre, notas in self.estudiantes.items():
            prom = self.calcular_promedio(nombre)
            total_clase += prom
            print(f"{nombre}: Promedio {prom:.2f} ({self.obtener_letra(prom)})")

        promedio_clase = total_clase / num_estudiantes
        print(f"\nPromedio general del grupo: {promedio_clase:.2f}")

if __name__ == "__main__":
    sistema = SistemaCalificaciones()

    sistema.agregar_estudiante("camila serna")
    sistema.agregar_estudiante("juan rua")

    sistema.agregar_calificacion("camila serna", 95)
    sistema.agregar_calificacion("camila serna", 88)
    sistema.agregar_calificacion("camila serna", 92)

    sistema.agregar_calificacion("juan rua", 75)
    sistema.agregar_calificacion("juan rua", 80)
    sistema.agregar_calificacion("juan rua", 68)

    
    sistema.generar_reporte_individual("camila serna")
    sistema.generar_reporte_general()


#ejercicio 32


import random

def obtener_palabra_secreta():
    palabras = ['python', 'programacion', 'desarrollo', 'computadora', 'codigo', 'ia']
    return random.choice(palabras).upper()

def jugar():
    palabra = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 6
    juego_terminado = False

    print("¡Bienvenido al juego del Ahorcado!")
    print(f"La palabra tiene {len(palabra)} letras.")

    while not juego_terminado:
        adivinanza = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                adivinanza += letra
            else:
                adivinanza += "_"
        
        print(f"\nPalabra: {adivinanza}")
        print(f"Intentos restantes: {intentos}")
        
        intento = input("Ingresa una letra: ").upper()

        if len(intento) != 1 or not intento.isalpha():
            print("Por favor, ingresa solo una letra válida.")
            continue
        if intento in letras_adivinadas:
            print("Ya habías ingresado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(intento)

        if intento in palabra:
            print(f"¡Bien! La letra '{intento}' está en la palabra.")
        else:
            intentos -= 1
            print(f"¡Oh no! La letra '{intento}' no está en la palabra.")

        if "_" not in adivinanza:
            juego_terminado = True
            print(f"\n¡Felicidades! Has adivinado la palabra secreta: {palabra}")

        if intentos == 0:
            juego_terminado = True
            print(f"\n¡Game Over! Te has quedado sin intentos. La palabra era: {palabra}")

if __name__ == "__main__":
    jugar()


#ejercicio 33


class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) [{estado}]"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        self.libros_prestados.append(libro)

    def devolver(self, libro):
        self.libros_prestados.remove(libro)


class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        print(f"Libro '{libro.titulo}' agregado.")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado.")

    def prestar_libro(self, isbn, id_usuario):
        libro = next((l for l in self.catalogo if l.isbn == isbn), None)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario:
            if libro.disponible:
                libro.disponible = False
                usuario. tomar_prestado(libro)
                print(f"¡Éxito! '{libro.titulo}' prestado a {usuario.nombre}.")
            else:
                print("El libro ya está prestado.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        libro = next((l for l in self.catalogo if l.isbn == isbn), None)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario and libro in usuario.libros_prestados:
            libro.disponible = True
            usuario.devolver(libro)
            print(f"¡Éxito! '{libro.titulo}' devuelto a la biblioteca.")
        else:
            print("Registro de préstamo incorrecto.")

    def mostrar_catalogo(self):
        print("\n--- Catálogo de la Biblioteca ---")
        for libro in self.catalogo:
            print(libro)

if __name__ == "__main__":
    biblioteca = Biblioteca()

    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-8437604947")
    libro2 = Libro("1984", "George Orwell", "978-8499890944")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    usuario1 = Usuario("Ana Gómez", "U001")
    biblioteca.registrar_usuario(usuario1)

    biblioteca.prestar_libro("978-8437604947", "U001")

    biblioteca.mostrar_catalogo()

    biblioteca.devolver_libro("978-8437604947", "U001")


#ejercicio 34


import statistics

datos = [10, 12, 23, 23, 16, 23, 21, 16, 30]

media = statistics.mean(datos)
mediana = statistics.median(datos)
moda = statistics.mode(datos)
desviacion_estandar = statistics.stdev(datos)
varianza = statistics.variance(datos)

# Mostrar resultados
print("--- Estadísticas Básicas ---")
print(f"Datos: {datos}")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Desviación Estándar: {desviacion_estandar:.2f}")
print(f"Varianza: {varianza:.2f}")


#ejercicio 35


FILAS = 6
COLUMNAS = 8

sala = [['0' for _ in range(COLUMNAS)] for _ in range(FILAS)]

def mostrar_sala():
    print("\n--- PANTALLA ---")
    print("  " + " ".join([str(i+1) for i in range(COLUMNAS)]))
    for r in range(FILAS):
        fila_str = " ".join(sala[r])
        print(f"{r+1} {fila_str}")
    print("-----------------\n")

def reservar_asientos():
    mostrar_sala()
    try:
        cantidad = int(input("¿Cuántos boletos deseas reservar? "))
        total_pagar = cantidad * 12.00 
        
        for i in range(cantidad):
            print(f"\nBoleto {i + 1}:")
            fila = int(input(f"Selecciona la fila (1 al {FILAS}): ")) - 1
            columna = int(input(f"Selecciona la butaca (1 al {COLUMNAS}): ")) - 1
            
            if 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
                if sala[fila][columna] == '0':
                    sala[fila][columna] = 'X'
                    print("¡Asiento reservado con éxito!")
                else:
                    print("Error: Este asiento ya está reservado. Intenta de nuevo.")
                    return
            else:
                print("Error: Asiento fuera de rango. Intenta de nuevo.")
                return
                
        print(f"\n¡Reserva completada! Total a pagar: ${total_pagar:.2f}")
    
    except ValueError:
        print("Entrada inválida. Por favor, ingresa solo números.")

while True:
    print("=== CINE VIRTUAL ===")
    print("1. Ver asientos disponibles")
    print("2. Reservar boletos")
    print("3. Salir")
    opcion = input("Selecciona una opción (1-3): ")
    
    if opcion == '1':
        mostrar_sala()
    elif opcion == '2':
        reservar_asientos()
    elif opcion == '3':
        print("Gracias por usar el sistema de reservas. ¡Hasta pronto!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")






