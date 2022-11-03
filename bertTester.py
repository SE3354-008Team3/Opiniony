import pymongo
from pymongo import MongoClient
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import dbcontroller
import requests
from bs4 import BeautifulSoup
import re

cluster = MongoClient("mongodb+srv://admin:gJp1hbBR0wtAJY0u@cluster0.sd2zwqa.mongodb.net/?retryWrites=true&w=majority")
#print(cluster)

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

tokens = tokenizer.encode('It was good but couldve been better. Great', return_tensors='pt')
result = model(tokens)
result.logits
analysisString = "It was good but couldve been better. I hate my life"
analysisVal = int(torch.argmax(result.logits))+1



mgr = dbcontroller.DBController()
db = cluster['project_database']
collection = db['analysis']
#mgr.createUser('nibs', 12345, 'ryansfake@gmail.com','Ryan', 'Nibu')
#user = mgr.getUser('nibs',12345)
#user = mgr.getUser('collinmatz',12345)
#print(user)
# post = {"_id": 2, "value": analysisVal, "string": analysisString}
# #
# collection.insert_one(post)
user = mgr.getUser('collinmatz', 12345)
mgr.uploadAnalysis(user, analysisVal, analysisString)