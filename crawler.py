# mi_scraper/crawler.py
import urllib.request
import urllib.error
import time
import random

class Crawler:
    def __init__(self, user_agents=None, delay_range=(1, 3)):
        """
        :param user_agents: Lista de posibles User-Agent para rotar.
        :param delay_range: Rango (min, max) en segundos para dormir entre peticiones.
        """
        if user_agents is None:
            self.user_agents = [
                "MiScraperBot/1.0",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
            ]
        else:
            self.user_agents = user_agents
        
        self.delay_range = delay_range

    def fetch(self, url):
        """
        Descarga la página en 'url' y devuelve el contenido (HTML).
        """
        # Elegimos un User-Agent al azar
        user_agent = random.choice(self.user_agents)
        headers = {
            "User-Agent": user_agent
        }
        request = urllib.request.Request(url, headers=headers)

        # Retardo aleatorio para evitar bloqueos
        time.sleep(random.uniform(*self.delay_range))

        try:
            with urllib.request.urlopen(request) as response:
                if response.status == 200:
                    data = response.read().decode('utf-8', errors='replace')
                    return data
                else:
                    print(f"Error: Status code {response.status} en {url}")
                    return None
        except urllib.error.URLError as e:
            print(f"Error al conectar con {url}: {e}")
            return None
