#ejemplo del commit
# APARTADO 1:
# 1. Establece una profundidad inicial de 0 metros y una profundidad máxima de la
# fosa de 1500 metros.
# 2. Simula el descenso del submarino en incrementos de 150 metros por turno.
# 3. Usa un bucle while para continuar el descenso mientras la profundidad actual
# sea menor que la profundidad máxima.
# 4. En cada paso, muestra la profundidad actual.
# 5. Al salir del bucle (llegar o superar los $1500~m$), muestra el mensaje:
# "¡Llegada a la Fosa Abisal! Iniciando escaneo."

p_inicial = 0
p_final = 1500
incremento = 150
while p_inicial <= p_final:
    print(f"profundidad actual {p_inicial}")
    p_inicial += incremento
print("¡Llegada a la Fosa Abisal! Iniciando escaneo.")


# APARTADO 2:
# 1. La presión segura máxima de los tanques de lastre es de $8.5~ATM$.
# 2. El programa debe solicitar al operador que introduzca la lectura de presión
# actual.
# 3. Usa un bucle while para validar la entrada. Si la presión introducida es mayor
# que la segura:
# o Muestra el mensaje: "⚠️ ¡ALERTA DE PRESIÓN! Valor crítico de
# $P > 8.5~ATM$. Introduzca una lectura más baja."# o Solicita una nueva lectura hasta que se introduzca un valor seguro.
# 4. Una vez que se ingresa una presión segura $(\le 8.5~ATM)$, muestra: "Presión
# estabilizada. Misión continúa."
p_segura = 8.5
p_actual = float(input("Ingrese la presión actual: "))
while p_actual > p_segura:
    if p_actual <= 10:
        print("⚠️ ¡ALERTA DE PRESIÓN! Valor crítico de P > 8.5 ATM. Introduzca una lectura más baja.")
    elif p_actual > 10:
        print("🚨 ¡ALERTA CRÍTICA! Presión extremadamente alta. ¡Reduzca inmediatamente!")
    p_actual = float(input("Ingrese una presión segura (ATM): "))

print("Presión estabilizada. Misión continúa.")


# APARTADO 3:
# 1. El submarino comienza con 150 unidades de Energía (E).
# 2. El bucle debe ejecutarse mientras la Energía sea mayor a 0.
# 3. En cada ciclo, el operador elige una actividad:
# o 1. Escáner Sonar (Costo: 30 E)
# o 2. Recolección de Muestras (Costo: 55 E)
# o 3. Fotografía Térmica (Costo: 15 E)
# 4. El programa debe verificar si la Energía restante es suficiente para la actividad
# elegida.
# o Si no hay suficiente Energía, muestra: "🔋 Energía insuficiente para
# esta acción. Elija otra." (Y el bucle continúa sin restar energía).
# o Si hay suficiente Energía, resta el costo y muestra la Energía restante.
# 5. Al agotarse la Energía, muestra: "Energía agotada. Retorno de emergencia a
# la superficie."

energia = 150

while energia > 0:
    print("\nEnergía actual:", energia)
    print("1. Escáner Sonar (30 E)")
    print("2. Recolección de Muestras (55 E)")
    print("3. Fotografía Térmica (15 E)")

    opcion = int(input("Elija una actividad: "))

    if opcion == 1:
        costo = 30
    elif opcion == 2:
        costo = 55
    elif opcion == 3:
        costo = 15
    else:
        print("Opción no válida.")
        continue  # vuelve al inicio del bucle
    if energia < costo:
        print("🔋 Energía insuficiente para esta acción. Elija otra.")
    else:
        energia -= costo
        print(f"Acción realizada. Energía restante: {energia}")

print("\nEnergía agotada. Retorno de emergencia a la superficie.")

# CÓDIGO PROBLEMÁTICO
combustible = 10
while combustible > 0:
    print(f"Tanques: {combustible}%. Continuar.")
    combustible -= 1
# Tarea: Corregir el código para que cuente del 10 al 1.





