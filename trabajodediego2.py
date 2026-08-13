# Caso 5. Potencia eléctrica y sobrecarga

voltaje = 0.0
corriente = 0.0
potencia = 0.0
umbral_potencia = 1000
contador_mediciones = 0
contador_sobrecargas = 0
suma_potencia = 0.0

print("--- Menú Potencia Eléctrica ---")
print("1. Registrar voltaje y corriente")
print("2. Salir y mostrar resultados")
opcion = input("Elige una opción (1 o 2): ")

# Utilizamos un ciclo while sencillo evaluando la opción como en los ejemplos
while opcion != "2":
	if opcion == "1":
		# Registro y validación del voltaje
		voltaje = float(input("Ingresa el voltaje (V): "))
		while voltaje < 0 or voltaje > 300:
			print("Error: El voltaje debe ser numérico y estar entre 0 y 300.")
			voltaje = float(input("Ingresa nuevamente el voltaje (V): "))

		# Registro y validación de la corriente
		corriente = float(input("Ingresa la corriente (A): "))
		while corriente < 0 or corriente > 100:
			print("Error: La corriente debe estar entre 0 y 100.")
			corriente = float(input("Ingresa nuevamente la corriente (A): "))

		# Cálculo de potencia y actualización de acumuladores
		potencia = voltaje * corriente
		suma_potencia += potencia
		contador_mediciones += 1

		print("Voltaje:", voltaje, "V | Corriente:", corriente, "A | Potencia:", potencia, "W")

		# Detección de sobrecarga
		if potencia > umbral_potencia:
			contador_sobrecargas += 1
	else:
		print("Opción no válida. Intenta de nuevo.")

	print("\n--- Menú Potencia Eléctrica ---")
	print("1. Registrar voltaje y corriente")
	print("2. Salir y mostrar resultados")
	opcion = input("Elige una opción (1 o 2): ")

# Salida esperada final
print("\n----- RESULTADOS FINALES -----")
print("Sobrecargas detectadas:", contador_sobrecargas)

if contador_mediciones > 0:
	promedio = suma_potencia / contador_mediciones
	print("Promedio de potencia:", promedio, "W")

if contador_sobrecargas > 0:
	print("Mensaje: Se detectaron sobrecargas, revisar dimensionamiento del sistema")
else:
	print("Mensaje: Sistema operando dentro de límites seguros de potencia")