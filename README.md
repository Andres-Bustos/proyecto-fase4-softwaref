# Sistema Integral de Gestión - Software FJ
###  Proyecto Fase 4 - Programación (Código: 213023) - UNAD

Este proyecto consiste en el desarrollo de un sistema orientado a objetos en **Python** para gestionar clientes, servicios y reservas para la empresa ficticia *Software FJ*. 


## Tecnologías y Conceptos Aplicados
*   **Lenguaje:** Python 3
*   **Paradigma:** Programación Orientada a Objetos
*   **Conceptos:** Abstracción, Herencia, Polimorfismo, Encapsulación y Sobrecarga de métodos.
*   **Robustez:** Manejo avanzado de excepciones (`try/except/else/finally`), excepciones personalizadas y encadenamiento de errores.

##  Estructura del Proyecto
*   `excepciones.py`: Definición de errores personalizados del sistema.
*   `entidades.py`: Clase abstracta base y gestión de la clase Cliente.
*   `servicios.py`: Clase abstracta Servicio y sus 3 derivados.
*   `reservas.py`: Lógica de reservas y sistema de logs.
*   `main.py`: Script principal con la simulación de las 10 operaciones.
*   `logs.txt`: Archivo de auditoría y registro de errores generado en tiempo de ejecución.

##  ¿Cómo ejecutarlo?
1. Clona este repositorio o descarga los archivos.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el archivo principal:
```bash
python main.py
