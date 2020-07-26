import numpy as np
import pandas as pd
from csv import reader
data = pd.read_csv('CCMLEmployeeData.csv')

domains = pd.DataFrame(data['Domain'].value_counts()).reset_index()
events = pd.DataFrame(data['Event1'].value_counts()).reset_index()
domains.pop('Domain')
events.pop('Event1')
domains.rename(columns={'index':'domain'},inplace=True)
events.rename(columns={'index':'event'},inplace=True)

Domain = {}
Event = {}
for domain in domains['domain']:
    Domain[domain]=domain.lower().split()
for event in events['event']:
    Event[event]=event.lower()[:-1].split() #Removed (s)

def textPreprocessing(data):
#   StopwordsRemoval
    words = data.split()
    from nltk.corpus import stopwords
    removeStopwords = [word for word in words if word.lower() not in stopwords.words('english')]
    
    return removeStopwords
