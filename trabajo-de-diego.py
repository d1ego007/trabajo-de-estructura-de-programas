# Caso 8. Voltaje residencial/industrial y estabilidad

contador_mediciones = 0
contador_criticos = 0

while True:
    print("\n--- Menú Estabilidad de Voltaje ---")
    print("1. Registrar voltaje")
    print("2. Salir y mostrar reporte")
    opcion = input("Elige una opción (1 o 2): ")

    if opcion == "1":
        # Registro y validación de la medición
        voltaje = float(input("Ingresa el voltaje medido (V): "))
        while voltaje < 0 or voltaje > 300:
            print("Error: El voltaje debe estar entre 0 y 300.")
            voltaje = float(input("Ingresa nuevamente el voltaje (V): "))

        contador_mediciones += 1

        # Generar gráfico textual proporcional (una barra por cada 10V)
        barra = "*" * int(voltaje // 10)
        print("Voltaje:", voltaje, "V | Gráfico:", barra)

        # Validar si el voltaje está fuera del rango aceptable (110-130V)
        if voltaje < 110 or voltaje > 130:
            contador_criticos += 1
            print("Voltaje crítico: fuera del rango aceptable.")
        else:
            print("Voltaje dentro del rango aceptable.")

    elif opcion == "2":
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

# Salida esperada final
print("\n----- REPORTE DE ESTABILIDAD -----")
print("Cantidad de voltajes medidos:", contador_mediciones)
print("Cantidad de voltajes críticos (fuera de rango):", contador_criticos)

# Clasificación de la estabilidad
if contador_criticos > 0:
    estabilidad = "Sistema con variaciones peligrosas"
else:
    estabilidad = "Sistema estable"

print("Mensaje:", estabilidad)