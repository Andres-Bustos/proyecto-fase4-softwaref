# main.py
from entidades import Cliente
from servicios import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from reservas import Reserva, registrar_log
from excepciones import ClienteInvalidoError, ServicioInvalidoError, ReservaIncorrectaError

def ejecutar_simulacion():
    print("=== INICIANDO SIMULACIÓN SOFTWARE FJ ===")
    registrar_log("--- INICIO DE LA SIMULACIÓN ---")

    # 1. Registro Válido de Cliente
    try:
        cliente1 = Cliente(1, "Andres Bustos", "12345678")
        print(f"[ÉXITO] Cliente creado: {cliente1.obtener_detalles()}")
    except Exception as e:
        print(f"[ERROR] {e}")

    # 2. Registro Inválido de Cliente (Cédula muy corta)
    try:
        cliente_error = Cliente(2, "Juan", "123")
        print("Esto no debería imprimirse")
    except ClienteInvalidoError as e:
        print(f"[ERROR CONTROLADO] Validación de cliente: {e}")
        registrar_log(f"Validación de cliente fallida: {e}", "ERROR")

    # 3. Creación Válida de Servicio
    servicio1 = ReservaSalas(101, "Sala de Juntas A", 50000)
    print(f"[ÉXITO] Servicio creado: {servicio1.describir()}")

    # 4. Creación Inválida de Servicio (Costo negativo)
    try:
        servicio_error = AlquilerEquipos(102, "Video Beam", -100)
    except ServicioInvalidoError as e:
        print(f"[ERROR CONTROLADO] Validación de servicio: {e}")
        registrar_log(f"Validación de servicio fallida: {e}", "ERROR")

    # 5. Reserva Exitosa
    try:
        reserva1 = Reserva(501, cliente1, servicio1, 3)
        reserva1.procesar()
        print(f"[ÉXITO] Reserva procesada. Estado: {reserva1.estado}, Total: ${reserva1.costo_total}")
    except Exception as e:
        print(f"[ERROR] {e}")

    # 6. Reserva Fallida (Horas negativas)
    try:
        reserva2 = Reserva(502, cliente1, servicio1, -2)
        reserva2.procesar()
    except ReservaIncorrectaError as e:
        print(f"[ERROR CONTROLADO] Fallo en reserva: {e}")
        print("-> Nota: El sistema sigue funcionando a pesar del error.")

    # 7. Otro Servicio (Polimorfismo)
    servicio2 = AsesoriaEspecializada(103, "Asesoría Python", 80000)
    reserva3 = Reserva(503, cliente1, servicio2, 6) # 6 horas (aplica descuento automático)
    reserva3.procesar()
    print(f"[ÉXITO] {servicio2.describir()} - Total con descuento: ${reserva3.costo_total}")

    # 8. Servicio No Disponible
    servicio2.disponible = False
    try:
        reserva4 = Reserva(504, cliente1, servicio2, 2)
        reserva4.procesar()
    except ReservaIncorrectaError as e:
        print(f"[ERROR CONTROLADO] Servicio no disponible: {e}")

    # 9. Cancelación de Reserva Exitosa
    reserva1.cancelar()
    print(f"[INFO] Estado de reserva 501: {reserva1.estado}")

    # 10. Intento de Cancelar Reserva Fallida
    reserva2.cancelar() # Esta ya había fallado
    print(f"[INFO] Estado de reserva 502: {reserva2.estado}")

    print("\n=== SIMULACIÓN TERMINADA CON ÉXITO ===")
    print("Revisa el archivo 'logs.txt' en tu carpeta para ver los registros.")
    registrar_log("--- FIN DE LA SIMULACIÓN ---")

if __name__ == "__main__":
    ejecutar_simulacion()