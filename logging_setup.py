import logging

def setup_logger():
    """
    Configura un logger básico que escribe en:
    - Consola
    - Archivo taximeter.log
    """
    logger = logging.getLogger("taximeter")
    logger.setLevel(logging.INFO)

    """
     Evita duplicar handlers si ya está configurado
    """
    if logger.handlers:
        return logger

    """
     Formato del mensaje, para que se vea de manera más legible por decirlo de alguna manera.
    """
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    """Handler para archivo taximeter.log, se crea automaticamente al ejecutar los logs
    y va registrando los mismis."""
    file_handler = logging.FileHandler("taximeter.log", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    """
    Handler para ver en consola sin tener que ir al archivo de logs
    """
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    """
    Registrar handlers en el archivo de logs y tambien en la consola.
    """
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
