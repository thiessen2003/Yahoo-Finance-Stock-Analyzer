# COMM 4190 - Yahoo Finance Stock Analyzer

### Main components and explanation

Yahoo Finance Stock Analyzer is the final project developed for COMM 4190. The core idea of this project is to provide an easy 
way for users to interact with an application that utilizes concepts approached throughout the semester to get financial advice on 
performing operations in the stock market. Essentially, the user selects an article from Yahoo Finance that mentions a particular stock, and the 
program will scrap the most important data from the article's text, including the title, the date it was published, and the core text. 

Once the program scrapped all the necessary data, it proceeds to employ the sentiment analyzer, which is a Python class that incorporates a Hugging Face 
pre-trained Robustly Optimized BERT Pretraining Approach (RoBERTA) model to analyze the sentiment on the text. Essentially This part of the code uses the BERT LLM, 
which basically tokenizes the words in the text and classifies the word as either negative, neutral, or positive, as well as a numerical value that indicates the strength of such 
emotion. Therefore, with this value returned, it is possible to understand the overall sentiment of the text. 

Once the sentiment is analyzed, the program applies the response obtained by the RoBERTA model as parameters in a ChatGPT API application that is populated with a predefined prompt. 
Then, this instance of OpenAI's LLM generates a response by prompt engineering the sentiment parameters so that the response generated is similar to a financial analyzer providing 
orientations on whether the user should buy, hold, or sell this particular stock.

Just to summarize one more time, this project employs LLMs in two different ways. Firstly, it uses BERT which is one of the first LLMs ever developed to actually perform the analysis of the sentiment, 
a task that some years ago was usually developed by using Logistic Regression models. Additionally, it uses ChatGPT 4.0 and prompt engineering to generate a recommendation to the user.

### Motivation 

First and foremost, I must mention that one of the main aspects that led me to develop this project is my interest for finance. I personally invest in the stock market and truly appreciate reading the news as often
as possible. However, as a college student that takes multiple classes and have several other responsibilities, I often see myself in a position where I am not able to truly 
keep track of the recent events that can potentially affect my stock portfolio. Also, when I can keep track of such events, I mostly do not go through the whole reading; I usually just skim the text. 

Therefore, I decided to develop this app to solve this problem that I constantly face of not being able to properly accompany the investment that I have. Surely, it does not substitute a fundamental and careful analysis of texts 
and conditions that can affect positions that I hold in the stock market, but it indeed provides an easy and intuitive way to properly understand the gist of what is happening at the present moment with the stocks that I am interested in. 

Additionally, it is relevant to say that I truly believe that this project in particular provided me with an easy an interesting way to apply all the concepts that we learned this semester, from utilizing Hugging Face to 
prompt engineering LLMs in order to obtain more precise results. 

### Running Locally 

Unfortunately, Yahoo Finance is quite inconsistent with the formatting of its publications. Sometimes, writers identify with specific HTML tags the stock ticker of the 
company being mentioned. Sometimes, they don't. Therefore, the code can present some issues with scrapping data form particular articles. Therefore, I would highly recommend using as an example the one below.

Link to the article: https://finance.yahoo.com/news/tsmc-just-gave-investors-another-085500926.html

### Imports/Libraries and technologies used  

- **openai**
- **unittest**
- **scipy**
- **transformers**
- **datetime**
- **requests**
- **re**
- **urllib.parse**
- **bs4**
- **pandas**
- **numpy**
- **Flask**
- **langchain**

### File Structure
- `./static`: contains images used in the application. 
- `./templates`: contains the html templates used in Flask app.
- `./data`: contains files with stock data to properly set the functionalities of the `StockReader` class. 
- `./tests`: contains files to perform unit tests on the most important classes utilized in the program.
- `app.py`: class with the main part of the Flask application and the specified routes. 
- `LLMGenerator.py`: class that implements a local instance of ChatGPT to generate a recommendation on the stock presented in the news. 
- `SentimentAnalyzer.py`: class that implements Roberta model to evaluate the sentiment of an arbitrary text 
- `StockReader.py`: class that is a simple implementation of pandas to evaluate if the stock being analyzed in the news exists in the set of stocks present in Nasdaq
- `WebScraper.py`: class that scrapes data from the url inputted by the user. 
