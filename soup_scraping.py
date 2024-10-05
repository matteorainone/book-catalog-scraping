import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
from typing import List, Dict, Any
import time
from log_config.logger_config import get_logger
from utils.scraping_functions import extract_books_from_page, get_next_page_url

logger = get_logger(__name__)

#definizione del url del sito da cui fare l'estrazione
url = "https://books.toscrape.com/"

# Si definisce una lista di appoggio in cui inserire tutte le informazioni estratte da tutti i libri del catalogo
all_books = []

while True:
    try:
        response = requests.get(url)
        if response.status_code != 200:
            logger.error(f"Failed to retrieve page: {url}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        # Si estraggono le informazioni dei libri della pagina
        books_info = extract_books_from_page(soup)
        # Si aggiungono alla lista d'appoggio
        all_books.extend(books_info)

        # Si cerca di ottenere il link della pagina successiva
        next_page = get_next_page_url(soup)
        if not next_page:
            break

        # Costruisci il nuovo URL
        if "catalogue" not in next_page:
            url = "https://books.toscrape.com/"+"catalogue/"+next_page
        else:
            url = "https://books.toscrape.com/" + next_page

        # Si inserisce un ritardo per evitare di sovraccaricare il server
        time.sleep(1)

    except Exception as e:
        logger.error(f"Error during scraping: {e}")
        break

# Creazione del DataFrame e salvataggio in un file CSV
try:
    df = pd.DataFrame(all_books)
    df.to_csv("books.csv", index=False)  # Si salvano i dati nel file CSV richiesto, escludendo la colonna dell'indice
    logger.info("Data saved to books.csv successfully.")
except Exception as e:
    logger.error(f"Error saving data to CSV: {e}")
