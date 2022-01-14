from bs4 import BeautifulSoup
import requests


class WebScrape:

    def scrape(self, URL):
        """function for getting the web content"""
        html_text = requests.get(URL).text
        html_content = BeautifulSoup(html_text, "lxml").text
        return html_content




