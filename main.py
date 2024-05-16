

from datetime import datetime
import random


class Estacionamiento:
    def __init__(self, num_lugares):
        self.num_lugares = num_lugares
        self.lugares_disponibles = list(range(1, num_lugares + 1))
        self.registros = {}

    def ingresar_vehiculo(self, placa):
        if not self.lugares_disponibles:
            print("No hay lugares disponibles")
            return
    
        lugar = random.choice(self.lugares_disponibles)
        hora_entrada = datetime.now().strftime("%H:%M")
        fecha = datetime.now().strftime("%Y-%m-%d")
        self.registros[placa] = {'lugar': lugar, 'hora_entrada': hora_entrada, 'fecha': fecha}
        self.lugares_disponibles.remove(lugar)
        print("__________________________________________________________")
        print(f"Fecha: {fecha}\nPlaca: {placa}\nEntrada: {hora_entrada}\nNumero de parqueo: {lugar}")
        print("__________________________________________________________")

    def salida_vehiculo(self, placa):
        if placa not in self.registros:
            print("Este vehiculo no esta registrado")
            return
        
        registro = self.registros[placa]
        hora_salida = datetime.now().strftime("%H:%M")
        duracion_minutos = (datetime.strptime(hora_salida,"%H:%M") - datetime.strptime(registro['hora_entrada'], "%H:%M")).seconds /60
        costo = duracion_minutos * 0.05
        print("__________________________________________________________")
        print(f"\nFecha: {registro['fecha']}\nPlaca: {placa}\nHora entrada: {registro['hora_entrada']}\nHora salida: {hora_salida}\nNumero de parqueo: {registro['lugar']}")
        print(f"Tiempo de estancia: {duracion_minutos}")
        print(f"Costo a pagar: ${costo:.2f}")
        print("__________________________________________________________")

        self.lugares_disponibles.append(registro['lugar'])
        del self.registros[placa]

def menu(estacionamiento):
        print("__________________________________________________________")
        print("1. Ingresar Entrada de vehiculo")
        print("2. Ingresar salida de vechiculo")
        print("3. Salir del programa")
        print("__________________________________________________________")

        lugares_disponibles = estacionamiento.lugares_disponibles
        print(f"Lugares disponibles: {lugares_disponibles}")

if __name__ == "__main__":
    num_lugares = int(input("Ingrese el numero de lugares del parqueo: "))
    estacionamiento = Estacionamiento(num_lugares)

    while True:
        menu(estacionamiento)
        opcion = input('Seleccione una opción')

        if opcion == '1':
            placa = input("Ingrese el numero de placa del vehiculo")
            estacionamiento.ingresar_vehiculo(placa)
        elif opcion == '2':
            placa = input("Ingrese el numero de placa del vehiculo")
            estacionamiento.salida_vehiculo(placa)
        elif opcion == '3':
            print("saliendo del programa...")
        else:
            print("Opcion no valida. Por facor, selecciones una opcion valida")