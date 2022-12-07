from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd


class SentimentAnalysis:
    def sentimentAnalysis(userInput):
        tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
        model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

        tokens = tokenizer.encode(userInput, return_tensors='pt')
        result = model(tokens)
        result.logits
        analysisVal = int(torch.argmax(result.logits))+1

        r = requests.get('https://www.yelp.com/biz/social-brew-cafe-pyrmont')
        soup = BeautifulSoup(r.text, 'html.parser')
        regex = re.compile('.*comment.*')
        results = soup.find_all('p', {'class':regex})
        reviews = [result.text for result in results]

        df = pd.DataFrame(np.array(reviews), columns=['review'])
        df['review'].iloc[0]
        def sentiment_score(review):
            tokens = tokenizer.encode(review, return_tensors='pt')
            result = model(tokens)
            return int(torch.argmax(result.logits))+1
        sentiment_score(df['review'].iloc[1])
        df['sentiment'] = df['review'].apply(lambda x: sentiment_score(x[:512]))
        df
        df['review'].iloc[3]
        return analysisVal