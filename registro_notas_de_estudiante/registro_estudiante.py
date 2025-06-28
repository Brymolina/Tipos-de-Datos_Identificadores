# Creación de programa que registra los datos de un estudiante y calcula el promedio de sus calificaciones.
# Aqui vamos a monstrar el uso de tipos de datos, identificadores y documentación en Python.

# Definimos una función para calcular el promedio de tres notas
def calcular_promedio(nota1: float, nota2: float, nota3: float) -> float:
    """Calcula el promedio de tres calificaciones."""
    return (nota1 + nota2 + nota3) / 3

# Datos otorgados del estudiante, en este caso hice con mi nombre
nombre = "Bryan Molina"                             # Tipo string
edad = 30                                           # Tipo int
materia = "Programación Orientada a Objetos"        # Tipo string

# Notas de ejemplo
nota_1 = 8.5                                        # Tipo float
nota_2 = 9.0
nota_3 = 7.5

# Llamamos a la función para calcular el promedio
promedio = calcular_promedio(nota_1, nota_2, nota_3)

# Evaluamos si el estudiante ha aprobado (nota mayor o igual a 7)
aprobado = promedio >= 7.0                          # Tipo boolean

# Mostramos los resultados obtenidos
print("REGISTRO DE ESTUDIANTE Y CÁLCULO DE PROMEDIO")
print("\nRESULTADOS")
print(f"Estudiante: {nombre}")
print(f"Edad: {edad} años")
print(f"Materia: {materia}")
print(f"Nota 1: {nota_1}")
print(f"Nota 2: {nota_2}")
print(f"Nota 3: {nota_3}")
print(f"Promedio: {promedio:.2f}")
print("¿Aprobado?:", aprobado)