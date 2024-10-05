from typing import Any, Dict, List
from bs4 import BeautifulSoup
from log_config.logger_config import get_logger

logger = get_logger(__name__)

def extract_books_from_page(soup: BeautifulSoup) -> List[Dict[str, Any]]:
    """
    Estrae le informazioni sui libri da una pagina web.

    Args:
        soup (BeautifulSoup): L'oggetto BeautifulSoup della pagina web.

    Returns:
        List[Dict[str, Any]]: Una lista di dizionari, ciascuno contenente le informazioni di un libro.
            Ogni dizionario ha le seguenti chiavi:
                - 'title': Il titolo del libro (str).
                - 'rating': La valutazione del libro (str).
                - 'price': Il prezzo del libro (str).
                - 'stock availability': La disponibilità in magazzino (str).
    """
    books = []
    book_elements = soup.find_all('article', class_='product_pod')
    for book in book_elements:
        try:
            title_element = book.find('h3').find('a')
            title = title_element['title'] if title_element else 'No Title'
            price = book.find('p', class_='price_color').text if book.find('p', class_='price_color') else 'No Price'
            stock_availability = book.find('p', class_='instock availability').text.strip() if book.find('p', class_='instock availability') else 'Unknown'
            rating_element = book.find('p', class_='star-rating')
            rating = rating_element['class'][-1] if rating_element else 'No rating'

            # Verifica della coerenza e validità dei dati
            if title == 'No Title' or price == 'No Price':
                logger.warning(f"Book with incomplete data: title={title}, price={price}")

            books.append({
                'title': title,
                'rating': rating,
                'price': price,
                'stock availability': stock_availability
            })
        except Exception as e:
            logger.error(f"Error extracting book data: {e}")
    return books

def get_next_page_url(soup: BeautifulSoup) -> str:
    """
    Ritorna l'URL della pagina successiva se il pulsante 'Next' è presente.

    Args:
        soup (BeautifulSoup): L'oggetto BeautifulSoup della pagina web.

    Returns:
        str: L'URL della pagina successiva, o None se non esiste.
    """
    next_button = soup.find('li', class_='next')
    if next_button:
        return next_button.find('a')['href']
    return None
