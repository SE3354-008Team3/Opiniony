import pymongo
from pymongo import MongoClient
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import dbcontroller
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd

cluster = MongoClient("mongodb+srv://admin:gJp1hbBR0wtAJY0u@cluster0.sd2zwqa.mongodb.net/?retryWrites=true&w=majority")
#print(cluster)
def sentimentAnalysis(userInput):
    tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

    model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

    tokens = tokenizer.encode('harley pastornak is a horrible person, he drugged me into becoming a well behaved celebrity', return_tensors='pt')
    result = model(tokens)
    result.logits
    #analysisString = "It was good but couldve been better. I hate my life"
    analysisVal = int(torch.argmax(result.logits))+1
    print(analysisVal)

    r = requests.get('https://www.yelp.com/biz/social-brew-cafe-pyrmont')
    soup = BeautifulSoup(r.text, 'html.parser')
    regex = re.compile('.*comment.*')
    results = soup.find_all('p', {'class':regex})
    reviews = [result.text for result in results]
    print(reviews)

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



# mgr = dbcontroller.DBController()
# db = cluster['project_database']
# collection = db['analysis']
#mgr.createUser('nibs', 12345, 'ryansfake@gmail.com','Ryan', 'Nibu')
#user = mgr.getUser('nibs',12345)
#user = mgr.getUser('collinmatz',12345)
#print(user)
# post = {"_id": 2, "value": analysisVal, "string": analysisString}
# #
# collection.insert_one(post)
#user = mgr.getUser('collinmatz', 12345)
#mgr.uploadAnalysis(user, analysisVal, analysisString)