# excepciones.py

class SoftwareFJError(Exception):
    """Clase base para las excepciones del sistema Software FJ"""
    pass

class ClienteInvalidoError(SoftwareFJError):
    """Se lanza cuando los datos del cliente no son válidos"""
    pass

class ServicioInvalidoError(SoftwareFJError):
    """Se lanza cuando los parámetros del servicio son incorrectos"""
    pass

class ReservaIncorrectaError(SoftwareFJError):
    """Se lanza cuando hay un problema al crear o procesar una reserva"""
    pass