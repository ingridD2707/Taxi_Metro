# Taximeter – Proyecto en Python

Objetivo: este proyecto es una introduccion a PYTHON, en el que practicaremos y daremos un repaso a los conceptos basicos pero fundamentales de este lenguaje.

El proyecto se trata de un taxímetro interactivo en consola, que permite simular un trayecto de taxi calculando:

- Tiempo parado

- Tiempo en movimiento

- Tarifa total generada según los segundos en cada estado

- Registro de eventos mediante logging

- Historial de trayectos (si usas history.txt)
  

## Funcionalidades principales

### Comandos disponibles:

start → Inicia el trayecto en estado stopped

stop → Cambia el estado del taxi a parado

move → Cambia el estado del taxi a en movimiento

finish → Finaliza el viaje, calcula tiempos y tarifa

exit → Cierra el programa

Tarifa: 
2.0 €/s precio inicial

0.02 €/s parado

0.05 €/s en movimiento

Sistema de logs:

Guarda eventos como inicio de viaje, cambios de estado, errores del usuario, fin del trayecto y salida del programa.

Archivo generado: taximeter.log

## Estructura del proyecto

```
TAXI_METRO/
│
├── __pycache__/           # Archivos generados automáticamente por Python
├── venv/                  # Entorno virtual (no se sube a GitHub)
│
├── .gitignore             # Archivos y carpetas que Git debe ignorar
├── config.json            # Configuración (tarifas, valores base…)
├── history.txt            # Histórico de trayectos completados
├── logging_setup.py       # Configuración del sistema de logging
├── README.md              # Documentación del proyecto
├── taximeter.log          # Registro de eventos generado automáticamente
└── taximeter.py           # Programa principal del taxímetro
```

## Cómo ejecutar el proyecto

Clonar el repositorio:

git clone https://github.com/Bootcamp-IA-P6/Proyecto_1_Ingrid_Martinez.git

Ejecutar el programa:

python taximeter.py

### logging_setup.py

logging_setup.py 
configura un logger que escribe tanto en consola como en el archivo taximeter.log.
También evita la duplicación de handlers y usa un formato limpio y legible.


