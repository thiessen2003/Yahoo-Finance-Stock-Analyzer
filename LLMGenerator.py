import openai
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class LLMGenerator:
    def __init__(self, text, sentiment, recommendation, openai_api_key, date_relevance, ticker):
        self.text = text
        self.sentiment = sentiment
        self.recommendation = recommendation
        openai.api_key = openai_api_key
        self.date_relevance = date_relevance
        self.ticker = ticker


    def generate_gpt_text(self):
        prompt = self.generate_prompt()
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a knowledgeable market analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        gpt_response = response['choices'][0]['message']['content']
        return gpt_response.strip()


    def generate_prompt(self):

        prompt = f"Firstly, provide a summary of the news based on the text: {self.text}. "
        prompt += f"After the summary, provide a recommendation of what an investor should do with the stock considering that the sentiment regarding the news is {self.sentiment}, the recommendation is to {self.recommendation}, and {self.date_relevance}."
        return prompt

