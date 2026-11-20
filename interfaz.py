import tkinter as tk
from tkinter import ttk, messagebox

# Importamos tus clases y excepciones tal como están en tu proyecto
from entidades import Cliente
from servicios import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from reservas import Reserva, registrar_log
from excepciones import ClienteInvalidoError, ServicioInvalidoError, ReservaIncorrectaError

class AplicacionSoftwareFJ:
    def __init__(self, root):
        self.root = root
        self.root.title("Software FJ - Sistema de Gestión")
        self.root.geometry("700x550")
        
        # Listas para simular la "base de datos" en memoria
        self.lista_clientes = []
        self.lista_servicios = []
        self.lista_reservas = []
        
        # Crear pestañas (Notebook)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.frame_clientes = ttk.Frame(self.notebook)
        self.frame_servicios = ttk.Frame(self.notebook)
        self.frame_reservas = ttk.Frame(self.notebook)
        
        self.notebook.add(self.frame_clientes, text="1. Registrar Cliente")
        self.notebook.add(self.frame_servicios, text="2. Registrar Servicio")
        self.notebook.add(self.frame_reservas, text="3. Crear Reserva")
        
        self.construir_clientes()
        self.construir_servicios()
        self.construir_reservas()

    # ================= PESTAÑA CLIENTES =================
    def construir_clientes(self):
        ttk.Label(self.frame_clientes, text="Registrar Nuevo Cliente", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.frame_clientes, text="ID Cliente:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_id_cli = ttk.Entry(self.frame_clientes)
        self.entry_id_cli.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(self.frame_clientes, text="Nombre:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_nombre_cli = ttk.Entry(self.frame_clientes)
        self.entry_nombre_cli.grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(self.frame_clientes, text="Cédula:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_cedula_cli = ttk.Entry(self.frame_clientes)
        self.entry_cedula_cli.grid(row=3, column=1, padx=10, pady=5)
        
        ttk.Button(self.frame_clientes, text="Guardar Cliente", command=self.registrar_cliente).grid(row=4, column=0, columnspan=2, pady=20)
        
        self.texto_clientes = tk.Text(self.frame_clientes, height=8, width=70)
        self.texto_clientes.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def registrar_cliente(self):
        id_cli = self.entry_id_cli.get().strip()
        nombre = self.entry_nombre_cli.get().strip()
        cedula = self.entry_cedula_cli.get().strip()
        
        try:
            # Instanciamos tu clase Cliente (aquí se ejecutan tus validaciones)
            nuevo_cliente = Cliente(id_cli, nombre, cedula)
            self.lista_clientes.append(nuevo_cliente)
            
            self.texto_clientes.insert(tk.END, f"[ÉXITO] {nuevo_cliente.obtener_detalles()}\n")
            messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
            
            # Limpiar campos
            self.entry_id_cli.delete(0, tk.END)
            self.entry_nombre_cli.delete(0, tk.END)
            self.entry_cedula_cli.delete(0, tk.END)
            
        except ClienteInvalidoError as e:
            messagebox.showerror("Error de Validación", str(e))
            registrar_log(f"Validación de cliente fallida (GUI): {e}", "ERROR")
            self.texto_clientes.insert(tk.END, f"[ERROR] {e}\n")
        except Exception as e:
            messagebox.showerror("Error Inesperado", str(e))

    # ================= PESTAÑA SERVICIOS =================
    def construir_servicios(self):
        ttk.Label(self.frame_servicios, text="Registrar Nuevo Servicio", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.frame_servicios, text="Tipo de Servicio:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.combo_tipo_serv = ttk.Combobox(self.frame_servicios, values=["Sala", "Equipo", "Asesoría"], state="readonly")
        self.combo_tipo_serv.grid(row=1, column=1, padx=10, pady=5)
        self.combo_tipo_serv.bind("<<ComboboxSelected>>", self.actualizar_campos_servicio)
        
        ttk.Label(self.frame_servicios, text="ID Servicio:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_id_serv = ttk.Entry(self.frame_servicios)
        self.entry_id_serv.grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(self.frame_servicios, text="Nombre/Descripción:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_nombre_serv = ttk.Entry(self.frame_servicios)
        self.entry_nombre_serv.grid(row=3, column=1, padx=10, pady=5)
        
        ttk.Label(self.frame_servicios, text="Costo Base:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_costo_serv = ttk.Entry(self.frame_servicios)
        self.entry_costo_serv.grid(row=4, column=1, padx=10, pady=5)
        
        ttk.Button(self.frame_servicios, text="Guardar Servicio", command=self.registrar_servicio).grid(row=5, column=0, columnspan=2, pady=20)
        
        self.texto_servicios = tk.Text(self.frame_servicios, height=8, width=70)
        self.texto_servicios.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def actualizar_campos_servicio(self, event):
        # Función por si a futuro quieres agregar campos específicos según el tipo
        pass

    def registrar_servicio(self):
        tipo = self.combo_tipo_serv.get()
        id_serv = self.entry_id_serv.get().strip()
        nombre = self.entry_nombre_serv.get().strip()
        costo = self.entry_costo_serv.get().strip()
        
        try:
            if not tipo:
                raise ValueError("Debe seleccionar un tipo de servicio.")
            
            # Instanciamos la clase correspondiente según el combo
            if tipo == "Sala":
                nuevo_serv = ReservaSalas(id_serv, nombre, float(costo))
            elif tipo == "Equipo":
                nuevo_serv = AlquilerEquipos(id_serv, nombre, float(costo))
            elif tipo == "Asesoría":
                nuevo_serv = AsesoriaEspecializada(id_serv, nombre, float(costo))
            else:
                raise ValueError("Tipo no válido")
                
            self.lista_servicios.append(nuevo_serv)
            self.texto_servicios.insert(tk.END, f"[ÉXITO] {nuevo_serv.describir()}\n")
            messagebox.showinfo("Éxito", "Servicio registrado correctamente.")
            
            self.entry_id_serv.delete(0, tk.END)
            self.entry_nombre_serv.delete(0, tk.END)
            self.entry_costo_serv.delete(0, tk.END)
            
        except ValueError as e:
            messagebox.showerror("Dato Inválido", "El costo debe ser un número válido.")
        except ServicioInvalidoError as e:
            messagebox.showerror("Error de Validación", str(e))
            registrar_log(f"Validación de servicio fallida (GUI): {e}", "ERROR")
        except Exception as e:
            messagebox.showerror("Error Inesperado", str(e))

    # ================= PESTAÑA RESERVAS =================
    def construir_reservas(self):
        ttk.Label(self.frame_reservas, text="Crear Nueva Reserva", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.frame_reservas, text="ID Reserva:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_id_res = ttk.Entry(self.frame_reservas)
        self.entry_id_res.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(self.frame_reservas, text="Cédula del Cliente:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_cedula_res = ttk.Entry(self.frame_reservas)
        self.entry_cedula_res.grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(self.frame_reservas, text="ID del Servicio:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_id_serv_res = ttk.Entry(self.frame_reservas)
        self.entry_id_serv_res.grid(row=3, column=1, padx=10, pady=5)
        
        ttk.Label(self.frame_reservas, text="Horas/Días:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_horas_res = ttk.Entry(self.frame_reservas)
        self.entry_horas_res.grid(row=4, column=1, padx=10, pady=5)
        
        ttk.Button(self.frame_reservas, text="Procesar Reserva", command=self.crear_reserva).grid(row=5, column=0, columnspan=2, pady=20)
        
        self.texto_reservas = tk.Text(self.frame_reservas, height=8, width=70)
        self.texto_reservas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def crear_reserva(self):
        id_res = self.entry_id_res.get().strip()
        cedula_cli = self.entry_cedula_res.get().strip()
        id_serv = self.entry_id_serv_res.get().strip()
        horas = self.entry_horas_res.get().strip()
        
        try:
            # Buscar cliente
            cliente_encontrado = next((c for c in self.lista_clientes if str(c.cedula) == cedula_cli), None)
            if not cliente_encontrado:
                raise ClienteInvalidoError("No existe un cliente registrado con esa cédula.")
                
            # Buscar servicio
            servicio_encontrado = next((s for s in self.lista_servicios if str(s.id_entidad) == id_serv), None)
            if not servicio_encontrado:
                raise ServicioInvalidoError("No existe un servicio registrado con ese ID.")
            
            # Crear y procesar reserva
            nueva_reserva = Reserva(id_res, cliente_encontrado, servicio_encontrado, int(horas))
            nueva_reserva.procesar()
            
            self.lista_reservas.append(nueva_reserva)
            self.texto_reservas.insert(tk.END, f"[ÉXITO] Reserva {id_res} procesada. Total a pagar: ${nueva_reserva.costo_total}\n")
            messagebox.showinfo("Éxito", f"Reserva procesada. Total: ${nueva_reserva.costo_total}")
            
            self.entry_id_res.delete(0, tk.END)
            self.entry_cedula_res.delete(0, tk.END)
            self.entry_id_serv_res.delete(0, tk.END)
            self.entry_horas_res.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Dato Inválido", "Las horas deben ser un número entero.")
        except (ClienteInvalidoError, ServicioInvalidoError, ReservaIncorrectaError) as e:
            messagebox.showerror("Error en Reserva", str(e))
            registrar_log(f"Fallo en reserva (GUI): {e}", "ERROR")
            self.texto_reservas.insert(tk.END, f"[ERROR] {e}\n")
        except Exception as e:
            messagebox.showerror("Error Inesperado", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionSoftwareFJ(root)
    root.mainloop()