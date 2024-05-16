import random
from datetime import datetime

class Estacionamiento:
    def __init__(self, num_lugares):
        self.num_lugares = num_lugares
        self.lugares_disponibles = list(range(1, num_lugares + 1))
        self.registros = {}

    def ingresar_vehiculo(self, placa):
        if not self.lugares_disponibles:
            print("Lo siento, no hay lugares disponibles en este momento.")
            return

        lugar = random.choice(self.lugares_disponibles)
        hora_entrada = datetime.now().strftime("%H:%M")
        fecha = datetime.now().strftime("%Y-%m-%d")
        self.registros[placa] = {'lugar': lugar, 'hora_entrada': hora_entrada, 'fecha': fecha}
        self.lugares_disponibles.remove(lugar)
        print("\n==============================")
        print(f"Fecha de entrada: {fecha}\nVehículo con placa: {placa}\nHora de entrada: {hora_entrada}\nNumero de parqueo: {lugar}")
        print("\n==============================")
        
    def salir_vehiculo(self, placa):
        if placa not in self.registros:
            print("Este vehículo no está registrado en el estacionamiento.")
            return

        registro = self.registros[placa]
        hora_salida = datetime.now().strftime("%H:%M")
        duracion_minutos = (datetime.strptime(hora_salida, "%H:%M") - datetime.strptime(registro['hora_entrada'], "%H:%M")).seconds / 60
        costo = duracion_minutos * 0.05
        print("\n=========== Recibo ===========")
        print(f"\nFecha de entrada: {registro['fecha']}\nVehículo con placa: {placa}\nHora de entrada: {registro['hora_entrada']}\nHora de salida: {hora_salida} \nNumero de parqueo: {registro['lugar']}")
        print(f"Tiempo de estancia: {duracion_minutos} minutos.")
        print(f"Costo a pagar: ${costo:.2f}")
        print("\n==============================")
        self.lugares_disponibles.append(registro['lugar'])
        del self.registros[placa]

def menu(estacionamiento):
    print("\n=== Menú ===")
    print("1. Ingresar entrada de vehículo")
    print("2. Ingresar salida de vehículo")
    print("3. Salir del programa")

    lugares_disponibles = estacionamiento.lugares_disponibles
    print(f"Lugares disponibles: {lugares_disponibles}")

if __name__ == "__main__":
    num_lugares = int(input("Ingrese el número de lugares del parqueo: "))
    estacionamiento = Estacionamiento(num_lugares)

    while True:
        menu(estacionamiento)
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            placa = input("Ingrese el número de placa del vehículo: ")
            estacionamiento.ingresar_vehiculo(placa)
        elif opcion == '2':
            placa = input("Ingrese el número de placa del vehículo que sale: ")
            estacionamiento.salir_vehiculo(placa)
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
