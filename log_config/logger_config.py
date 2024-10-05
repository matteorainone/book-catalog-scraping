import logging

# Configurazione del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# Creazione di un handler per il file
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Creazione di un formatter e aggiunta all'handler del file
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Aggiungi l'handler del file al logger
logger.addHandler(file_handler)

def get_logger(name):
    return logging.getLogger(name)