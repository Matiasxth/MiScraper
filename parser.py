# mi_scraper/parser.py
from html.parser import HTMLParser

class SimpleHTMLParser(HTMLParser):
    """
    Parser de HTML básico que busca, por ejemplo, todos los <title> y <h1>.
    """

    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_h1 = False
        self.titles = []
        self.h1_tags = []
        self.current_data = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'title':
            self.in_title = True
            self.current_data = []
        elif tag.lower() == 'h1':
            self.in_h1 = True
            self.current_data = []

    def handle_endtag(self, tag):
        if tag.lower() == 'title' and self.in_title:
            text = "".join(self.current_data).strip()
            self.titles.append(text)
            self.in_title = False
            self.current_data = []
        elif tag.lower() == 'h1' and self.in_h1:
            text = "".join(self.current_data).strip()
            self.h1_tags.append(text)
            self.in_h1 = False
            self.current_data = []

    def handle_data(self, data):
        if self.in_title or self.in_h1:
            self.current_data.append(data)

def parse_html(html_content):
    """
    Función de conveniencia que crea el parser, alimenta el contenido HTML
    y devuelve resultados.
    """
    parser = SimpleHTMLParser()
    parser.feed(html_content)
    parser.close()
    return {
        "titles": parser.titles,
        "h1_tags": parser.h1_tags
    }
