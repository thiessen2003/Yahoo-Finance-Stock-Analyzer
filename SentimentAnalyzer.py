import pandas as pd
import numpy as np
import openai
import re

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

class SentimentAnalyzer:
    def __init__(self, text, openai_api_key):
        self.text = text
        self.MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.MODEL)
        self.max_length = 512
        openai.api_key = openai_api_key

    def evaluate_sentiment(self):
        encoded_text = self.tokenizer(self.text, return_tensors='pt', max_length=self.max_length, truncation=True)
        output = self.model(**encoded_text)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        sentiment_scores = {
            'negative': scores[0],
            'neutral': scores[1],
            'positive': scores[2]
        }

        sentiment = max(sentiment_scores, key=sentiment_scores.get)
        weight = float(sentiment_scores[sentiment])

        if sentiment == 'positive' and weight >= 0.7:
            recommendation = 'buy'
        elif sentiment == 'negative' and weight >= 0.7:
            recommendation = 'sell'
        else:
            recommendation = 'hold'

        return sentiment, weight, recommendation

