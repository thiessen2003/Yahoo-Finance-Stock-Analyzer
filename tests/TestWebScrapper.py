import unittest
from WebScrapper import WebScrapper

class TestWebScrapper(unittest.TestCase):

    def setUp(self):
        self.scrapper = WebScrapper("https://finance.yahoo.com/news/tsmc-just-gave-investors-another-085500926.html")

    def test_validate_url_correct(self):
        self.assertTrue(self.scrapper.validate_url())

    def test_validate_url_incorrect(self):
        self.scrapper.url = "https://invalidurl.com/news"
        self.assertFalse(self.scrapper.validate_url())

    def test_extract_title(self):
        title = self.scrapper.title_scrapper()
        self.assertIsNotNone(title)


if __name__ == "__main__":
    unittest.main()