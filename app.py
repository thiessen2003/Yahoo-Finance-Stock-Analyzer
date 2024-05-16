from flask import Flask, request, jsonify, render_template
from WebScrapper import WebScrapper
from SentimentAnalyzer import SentimentAnalyzer
from LLMGenerator import LLMGenerator
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/hello_world", methods=["GET"])
def hello_world():
    return "Hello World"

@app.route("/extract_ticker", methods=["POST"])
def extract_ticker():
    data = request.get_json()
    url = data.get("url")
    web_scrapper = WebScrapper(url)
    ticker = web_scrapper.ticker_scrapper()
    if ticker:
        return jsonify({"ticker": ticker})
    else:
        return jsonify({"error": "Invalid URL or unable to extract ticker"})

@app.route("/extract_title", methods=["POST"])
def extract_title():
    data = request.get_json()
    url = data.get("url")
    web_scrapper = WebScrapper(url)
    title = web_scrapper.title_scrapper()
    if title:
        return jsonify({"title": title})
    else:
        return jsonify({"error": "Invalid URL or unable to extract title"})

@app.route("/extract_text", methods=["POST"])
def extract_text():
    data = request.get_json()
    url = data.get("url")
    web_scrapper = WebScrapper(url)
    text = web_scrapper.text_scrapper()
    if text:
        return jsonify({"text": text})
    else:
        return jsonify({"error": "Invalid URL or unable to extract text"})

@app.route("/analyze_sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    text = data.get("text")
    if text:
        analyzer = SentimentAnalyzer(text, "OPENAI-KEY")
        sentiment, weight, recommendation = analyzer.evaluate_sentiment()
        return jsonify({"sentiment": sentiment, "weight": round(float(weight), 2), "recommendation": recommendation})
    else:
        return jsonify({"error": "Text is required for sentiment analysis"})

@app.route("/extract_date", methods=["POST"])
def extract_date():
    data = request.get_json()
    url = data.get("url")
    web_scrapper = WebScrapper(url)
    date = web_scrapper.date_scrapper()
    if date:
        return jsonify({"date": date})
    else:
        return jsonify({"error": "Invalid URL or unable to extract date"})

@app.route("/extract_date_relevance", methods=["POST"])
def extract_date_relevance():
    data = request.get_json()
    url = data.get("url")
    web_scrapper = WebScrapper(url)
    date_relevance = web_scrapper.get_date_relevance()
    if date_relevance:
        return jsonify({"date_relevance": date_relevance})
    else:
        return jsonify({"error": "Unable to determine date relevance"})

@app.route("/gpt_response", methods=["POST"])
def generate_llama_response():
    data = request.get_json()
    text = data.get("text")
    sentiment = data.get("sentiment")
    recommendation = data.get("recommendation")
    date_relevance = data.get("date_relevance")
    ticker = data.get("ticker")

    if not text or not sentiment or not recommendation or not date_relevance:
        return jsonify({"error": "Text, sentiment, recommendation, and date_relevance are required"}), 400

    try:
        gpt_generator = LLMGenerator(text, sentiment, recommendation, "OPENAI-KEY", date_relevance, ticker)
        gpt_response = gpt_generator.generate_gpt_text()
        return jsonify({"gpt_response": gpt_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)