# entidades.py
from abc import ABC, abstractmethod
from excepciones import ClienteInvalidoError

class EntidadBase(ABC):
    """Clase abstracta general del sistema"""
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad # Atributo protegido (encapsulación)

    @abstractmethod
    def obtener_detalles(self):
        pass

class Cliente(EntidadBase):
    def __init__(self, id_cliente, nombre, cedula):
        super().__init__(id_cliente)
        self.__nombre = None
        self.__cedula = None
        # Usamos los setters para que se validen desde el principio
        self.nombre = nombre
        self.cedula = cedula

    # Getters y Setters (Encapsulación)
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) == 0:
            raise ClienteInvalidoError("El nombre del cliente no puede estar vacío.")
        self.__nombre = valor

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, valor):
        if not valor or len(str(valor)) < 5:
            raise ClienteInvalidoError("La cédula debe tener al menos 5 caracteres.")
        self.__cedula = valor

    def obtener_detalles(self):
        return f"Cliente ID: {self._id_entidad} | Nombre: {self.__nombre} | Cédula: {self.__cedula}"