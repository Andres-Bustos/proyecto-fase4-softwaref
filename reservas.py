# reservas.py
import datetime
from excepciones import ReservaIncorrectaError

# Función para guardar los errores y eventos en el archivo .txt
def registrar_log(mensaje, tipo="INFO"):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{fecha}] [{tipo}] {mensaje}\n")

class Reserva:
    def __init__(self, id_reserva, cliente, servicio, duracion_horas):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "Pendiente"
        self.costo_total = 0.0

    def procesar(self):
        try:
            if not self.servicio.disponible:
                raise ReservaIncorrectaError("El servicio solicitado no está disponible.")
            
            # Aquí usamos el método sobrecargado pasando el impuesto (19%)
            self.costo_total = self.servicio.calcular_costo(self.duracion_horas, impuesto=0.19)
            self.estado = "Confirmada"
            registrar_log(f"Reserva {self.id_reserva} confirmada para {self.cliente.nombre}. Total: ${self.costo_total:.2f}")
            return True
        except Exception as e:
            self.estado = "Fallida"
            # Aquí se hace el ENCADENAMIENTO DE EXCEPCIONES (raise ... from e)
            registrar_log(f"Error al procesar reserva {self.id_reserva}: {str(e)}", "ERROR")
            raise ReservaIncorrectaError(f"No se pudo procesar la reserva: {e}") from e

    def cancelar(self):
        if self.estado == "Confirmada":
            self.estado = "Cancelada"
            registrar_log(f"Reserva {self.id_reserva} cancelada.")
        else:
            registrar_log(f"Intento fallido de cancelar reserva {self.id_reserva} en estado {self.estado}.", "WARNING")