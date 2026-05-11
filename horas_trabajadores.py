# Matriz con nombre y horas trabajadas de lunes a viernes

trabajadores = [
    ["Carlos", 8, 8, 9, 8, 10],
    ["Mariana", 7, 8, 8, 7, 8],
    ["Andrés", 9, 9, 8, 9, 9],
    ["Luisa", 6, 7, 8, 7, 6]
]

# Función para calcular total de horas y clasificación
def calcular_horas(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion


# Mostrar resultados
print("REPORTE DE HORAS TRABAJADAS\n")

for trabajador in trabajadores:
    nombre = trabajador[0]
    horas = trabajador[1:]

    total, clasificacion = calcular_horas(horas)

    print("Nombre:", nombre)
    print("Total horas:", total)
    print("Clasificación:", clasificacion)
    print("-----------------------------")
