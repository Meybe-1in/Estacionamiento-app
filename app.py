from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__)

class Estacionamiento:
    def __init__(self, num_lugares):
        self.num_lugares = num_lugares
        self.lugares_disponibles = list(range(1, num_lugares + 1))
        self.registros = {}

    def ingresar_vehiculo(self, placa):
        if not self.lugares_disponibles:
            return "Lo siento, no hay lugares disponibles en este momento."

        lugar = random.choice(self.lugares_disponibles)
        hora_entrada = datetime.now().strftime("%H:%M")
        fecha = datetime.now().strftime("%Y-%m-%d")
        self.registros[placa] = {'lugar': lugar, 'hora_entrada': hora_entrada, 'fecha': fecha}
        self.lugares_disponibles.remove(lugar)
        return f"Vehículo con placa {placa} ingresado al lugar {lugar} a las {hora_entrada}"

    def salir_vehiculo(self, placa):
        if placa not in self.registros:
            return "Este vehículo no está registrado en el estacionamiento."

        registro = self.registros[placa]
        hora_salida = datetime.now().strftime("%H:%M")
        duracion_minutos = (datetime.strptime(hora_salida, "%H:%M") - datetime.strptime(registro['hora_entrada'], "%H:%M")).seconds / 60
        costo = duracion_minutos * 0.05
        recibo = f"Vehículo con placa {placa}\nHora de entrada: {registro['hora_entrada']}\nFecha de entrada: {registro['fecha']}\nHora de salida: {hora_salida} \nNumero de parqueo: {registro['lugar']}\nTiempo de estancia: {duracion_minutos} minutos.\nCosto a pagar: ${costo:.2f}"
        self.lugares_disponibles.append(registro['lugar'])
        del self.registros[placa]
        return recibo

estacionamiento = Estacionamiento(20)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        placa = request.form['placa']
        mensaje = estacionamiento.ingresar_vehiculo(placa)
        return render_template('index.html', mensaje=mensaje, registros=estacionamiento.registros)
    return render_template('index.html', registros=estacionamiento.registros)

@app.route('/salir_vehiculo', methods=['POST'])
def salir_vehiculo():
    placa = request.form['placa']
    mensaje = estacionamiento.salir_vehiculo(placa)
    return render_template('index.html', mensaje=mensaje, registros=estacionamiento.registros)

if __name__ == '__main__':
    app.run(debug=True)
