# servicios.py
from abc import ABC, abstractmethod
from excepciones import ServicioInvalidoError

class Servicio(ABC):
    def __init__(self, id_servicio, nombre, costo_base):
        if costo_base <= 0:
            raise ServicioInvalidoError("El costo base debe ser mayor a cero.")
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.costo_base = costo_base
        self.disponible = True

    # MÉTODO SOBRECARGADO
    @abstractmethod
    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        pass

    @abstractmethod
    def describir(self):
        pass

class ReservaSalas(Servicio):
    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        if horas <= 0:
            raise ValueError("Las horas de reserva deben ser mayores a cero.")
        costo = self.costo_base * horas
        costo += costo * impuesto
        costo -= costo * descuento
        return costo

    def describir(self):
        return f"Reserva de Salas: {self.nombre} - Costo Base/Hora: ${self.costo_base}"

class AlquilerEquipos(Servicio):
    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        if horas <= 0:
            raise ValueError("Las horas de alquiler deben ser mayores a cero.")
        costo = (self.costo_base * horas) * 1.1 
        costo += costo * impuesto
        costo -= costo * descuento
        return costo

    def describir(self):
        return f"Alquiler de Equipos: {self.nombre} - Costo Base/Hora: ${self.costo_base}"

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        if horas <= 0:
            raise ValueError("Las horas de asesoría deben ser mayores a cero.")
        costo = self.costo_base * horas
        if horas > 5:
            costo -= costo * 0.05 
        costo += costo * impuesto
        costo -= costo * descuento
        return costo

    def describir(self):
        return f"Asesoría Especializada: {self.nombre} - Costo Base/Hora: ${self.costo_base}"