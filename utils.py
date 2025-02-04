# mi_scraper/utils.py
import random

def get_random_proxy():
    """
    Devuelve un proxy al azar de una lista predefinida.
    Este proxy luego se podría usar en Crawler.
    """
    proxies = [
        "http://123.456.78.9:8080",
        "http://98.76.54.32:3128",
        # ...
    ]
    return random.choice(proxies)
