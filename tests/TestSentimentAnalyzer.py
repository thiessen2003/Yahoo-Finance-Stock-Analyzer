import unittest
from SentimentAnalyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.positive_text = "I love python and I really like coding."
        self.negative_text = "I hate python and I despise coding."

    def test_evaluate_sentiment_positive(self):
        analyzer = SentimentAnalyzer(self.positive_text)
        sentiment, weight, recommendation = analyzer.evaluate_sentiment()
        self.assertEqual(sentiment, 'positive')
        self.assertGreaterEqual(weight, 0.7)
        self.assertEqual(recommendation, 'buy')

    def test_evaluate_sentiment_negative(self):
        analyzer = SentimentAnalyzer(self.negative_text)
        sentiment, weight, recommendation = analyzer.evaluate_sentiment()
        self.assertEqual(sentiment, 'negative')
        self.assertGreaterEqual(weight, 0.7)
        self.assertEqual(recommendation, 'sell')

if __name__ == "__main__":
    unittest.main()