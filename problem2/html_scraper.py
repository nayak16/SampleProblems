from html.parser import HTMLParser
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CustomHTMLParser(HTMLParser):
    LINK_TAG = 'a'
    HREF_ATTR = 'href'

    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == self.LINK_TAG:
            for attr in attrs:
                if attr[0] == self.HREF_ATTR:
                    self.links.append(attr[1])


class HTMLScraper():
    __name__ = 'html scraper'

    def __init__(self, target_link):
        self.target_link = target_link

    def has_target_link(self, html_file):
        with open(html_file, 'r') as contents:
            parser = CustomHTMLParser()
            parser.feed(contents.read())
            for link in parser.links:
                if self.target_link in link:
                    return True

        return False
