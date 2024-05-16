import datetime

import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from StockReader import StockReader
from SentimentAnalyzer import SentimentAnalyzer

class WebScrapper():

    def __init__(self, url):
        self.url = url
        self.stock_reader = StockReader()
        self.df = "./data/stocklist.csv"

    def validate_url(self):
        parsed_url = urlparse(self.url)
        if parsed_url.netloc == 'finance.yahoo.com':
            return True
        if 'finance.yahoo.com' in parsed_url.netloc:
            return True
        if re.search(r'finance\.yahoo\.com', parsed_url.path):
            return True
        return False

    def extract_stock_ticker(self, text):
        pattern = r'\([\w]+:\s*([A-Z]+)\)'
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        else:
            return None

    def ticker_scrapper(self):
        if self.validate_url():
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, "html.parser")
            result = str(soup.find("span", class_="ticker"))
            treated_result = self.extract_stock_ticker(result)
            if self.stock_reader.stock_exists(treated_result, self.df):
                return treated_result
        else:
            print("Invalid URL")

    def title_scrapper(self):
        if self.validate_url():
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, "html.parser")
            title_elements = soup.find_all("h1")
            for title_element in title_elements:
                title = title_element.get_text().strip()
                if title.lower() not in ["yahoo finance", "yahoo", "finance"]:
                    print(f"Extracted Title: {title}")
                    return title
            print("Title not found or matches Yahoo Finance header")
            return None
        else:
            print("Invalid URL")
            return None

    def text_scrapper(self):
        if self.validate_url():
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, "html.parser")
            paragraphs = soup.find_all("p")
            different_p = [p.get_text() for p in paragraphs]
            full_text = ""
            for p in different_p:
                full_text += p
            return full_text.strip()
        else:
            return "Invalid URL"

    def date_scrapper(self):
        if self.validate_url():
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, "html.parser")
            date_tag = soup.find("time")
            return date_tag['datetime'] if date_tag and date_tag.has_attr('datetime') else "No date found"

    def get_date_relevance(self):
        news_date = self.date_scrapper()
        if news_date == "No date found":
            return "No date found; relevance cannot be determined."

        news_date_obj = datetime.datetime.fromisoformat(news_date.replace('Z', '+00:00'))  # Parse the date
        current_date = datetime.datetime.now(datetime.timezone.utc)
        delta = current_date - news_date_obj
        if delta.days > 5:
            return "this news might not be relevant because of date published (too old)"
        else:
            return "this news is still relevant in terms of date published (recent)"

