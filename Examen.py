"""
Simular un sistema de cajero automático que permita al usuario realizar operaciones básicas como consultar saldo, retirar dinero, depositar dinero y salir. Todo debe hacerse mediante el uso de funciones, condicionales y repetitivas.

El programa inicia con un saldo inicial de $1000.
Mostrar un menú con las siguientes opciones:
Consultar saldo
Depositar dinero
Retirar dinero
Salir
"""

saldo = 1000

def consultar_saldo(saldo):
    print("\n-------------------")
    print("su saldo actual es: $", (saldo))

def depositar(saldo):
    print("\n--- DEPOSITAR DINERO ---")
    monto = float(input("ingrese cantidad que quieras depositar: $"))

    if monto > 0:
        saldo = saldo + monto
        print("¡Depósito exitoso!")
        print("Su nuevo saldo es: $", saldo)
    else:
        print("Error: El monto a depositar debe ser mayor a cero.")
        
    return saldo

def retirar(saldo):
    print("\n--- RETIRAR DINERO ---")
    monto = float(input("ingrese la cantidad de retiro: $"))

    if monto > 0:
        if monto <= saldo:
            saldo <= saldo - monto
            print("¡Retiro exitoso!")
            print("Su nuevo saldo es: $", saldo)
        else:
            print("Error: No tiene suficiente saldo para retirar esa cantidad.")
    else:
        print("Error: El monto a retirar debe ser mayor a cero.")
                    
        return saldo

def cajero_automatico():
    saldo = 1000
    opcion = ()

    while opcion != "4":
        print("\n==============================")
        print("     CAJERO AUTOMÁTICO     ")
        print("==============================")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            consultar_saldo(saldo)
        elif opcion == "2":
            saldo = depositar(saldo)
        elif opcion == "3":
            saldo = retirar(saldo)
        elif opcion == "4":
            print("\nGracias por usar el cajero. ¡Hasta luego!")
        else:
            print("Opción inválida. Por favor, elija un número entre 1 y 4.")

cajero_automatico()