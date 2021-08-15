import logging

def verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d] ; %(levelname)s ; [%(name)s.%(funcName)s:%(lineno)d] ; %(message)s',
        datefmt='%d-%m-%Y_%H:%M:%S'
    )

def configure_logging(app):
    # Eliminamos los posibles manejadores, si existen, del logger por defecto
    del app.logger.handlers[:]
    # Añadimos el logger por defecto a la lista de loggers
    loggers = [app.logger, ]
    handlers = []
    # Creamos un manejador para escribir los mensajes por consola (este podriamos ignorarlo)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(verbose_formatter())
    handlers.append(console_handler)
    # Creamos un file handler (pa que el log persista)
    file_handler = logging.FileHandler('logs/app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(verbose_formatter())
    handlers.append(file_handler)
    # Asociamos cada uno de los handlers a cada uno de los loggers
    for l in loggers:
        for handler in handlers:
            l.addHandler(handler)
        l.propagate = False
        l.setLevel(logging.DEBUG)