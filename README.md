# Book Scraper

Questo progetto utilizza **Selenium** per effettuare lo scraping del sito [Books to Scrape](https://books.toscrape.com/) e raccogliere informazioni dettagliate sui libri, tra cui:

- Titolo
- Valutazione in stelle
- Prezzo
- Disponibilità

I dati estratti vengono poi salvati in un file CSV strutturato.

## Requisiti

Prima di eseguire il progetto, assicurati di avere installato i seguenti strumenti:

- Python 3.x
- Selenium
- Un driver per il browser Chrome (es. [ChromeDriver](https://sites.google.com/chromium.org/driver/))

## Installazione

1. Installa le dipendenze richieste:
    ```bash
    pip install selenium pandas
    ```

2. Scarica il **ChromeDriver** compatibile con la tua versione di Chrome e aggiungilo alla directory del progetto.

## Utilizzo

1. Esegui lo script Python per avviare il processo di scraping:

    ```python
    python <nome_del_tuo_script>.py
    ```

2. Lo script navigherà automaticamente attraverso le pagine del sito e raccoglierà i dati richiesti.

3. I dati verranno salvati nel file `books.csv` nella directory del progetto.

## Struttura del progetto

- **Progetto_finale.ipynb**: Jupyter Notebook contenente il codice per l'esecuzione dello scraping.
- **books.csv**: File CSV generato contenente i dati dei libri.

## Dettagli tecnici

Lo script utilizza **Selenium** per automatizzare il browser e navigare tra le pagine del sito web. Le informazioni sui libri vengono estratte e salvate utilizzando **Pandas** per la gestione dei dati e la loro esportazione in formato CSV.

## Contributi

Se vuoi contribuire a migliorare questo progetto, sentiti libero di aprire una issue o una pull request.

## Licenza

Questo progetto è distribuito sotto licenza MIT. Per maggiori dettagli, consulta il file LICENSE.
