from robot.api import logger

#Colores
VERDE = "#006400"
ROJO = "#ff0000"
AMARILLO="#d8870b"

def log_correcto(log_info):
    formatted_message = _format_message(log_info, VERDE)
    logger.info(formatted_message, html=True)

def log_incorrecto(log_info):
    formatted_message = _format_message(log_info, ROJO)
    logger.error(formatted_message, html=True)
    raise AssertionError("Ending test...")

def log_advertencia(log_info):
    formatted_message = _format_message(log_info, AMARILLO)
    logger.warn(formatted_message, html=True)

def log_info(log_info):
    logger.info(log_info, html=False)

def _format_message(message, message_color):
    return f'<div style="color: {message_color};">{message}</div>'

