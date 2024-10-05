# Book Scraper con BeautifulSoup

Questo progetto utilizza **BeautifulSoup** e **requests** per effettuare lo scraping del sito [Books to Scrape](https://books.toscrape.com/). Lo script raccoglie informazioni sui libri, tra cui:

- Titolo
- Valutazione in stelle
- Prezzo
- Disponibilità

I dati vengono quindi salvati in un file CSV per una consultazione strutturata.

## Requisiti

Per eseguire il progetto, assicurati di avere installato:

- Python 3.x
- Le seguenti librerie Python:
    - `requests`
    - `beautifulsoup4`
    - `pandas`
    - Un modulo di configurazione dei log (es. `log_config`)
    - Funzioni di scraping custom (es. `scraping_functions.py`)

## Installazione

1. Installa le librerie necessarie:
    ```bash
    pip install requests beautifulsoup4 pandas
    ```

2. Assicurati che il file `log_config/logger_config.py` sia presente e correttamente configurato.

3. Crea o assicurati che il file `utils/scraping_functions.py` contenga le funzioni necessarie come `extract_books_from_page` e `get_next_page_url`.

## Utilizzo

1. Esegui lo script per avviare lo scraping:
    ```bash
    python soup_scraping.py
    ```

2. Lo script raccoglierà informazioni sui libri disponibili e navigherà automaticamente tra le pagine del sito.

3. I dati verranno salvati in un file CSV nella directory del progetto.

## Struttura del progetto

- **soup_scraping.py**: Script principale che effettua lo scraping e gestisce il salvataggio dei dati.
- **log_config/logger_config.py**: File per la configurazione del logger.
- **utils/scraping_functions.py**: Contiene funzioni ausiliarie per l'estrazione dei dati e la navigazione tra le pagine.

## Contributi

Se vuoi migliorare il progetto o segnalare bug, sentiti libero di aprire una issue o una pull request.

## Licenza

Questo progetto è distribuito sotto licenza MIT.
