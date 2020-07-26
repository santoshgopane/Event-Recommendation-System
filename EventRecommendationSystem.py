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

Domain['Security'].append('cyber')
Domain['Security'].append('hacking')
Domain['Coding'].append('cod')
Domain['Mobile Applications'].append('android')
Domain['Networking'].append('network')
Domain['Development Processes'].remove('processes')
Domain['Machine Learning'].remove('learning')
Domain['C'].append(' c ')
Domain['C'].remove('c')
Domain['Coding'].remove('coding')
Domain['Web Development'].remove('development')
Domain['Web Development'].remove('web')
Domain['Web Development'].append('web development')
Domain['Web Development'].append('website')
Domain['Machine Learning'].append('nlp')
Domain['Machine Learning'].append('natural language processing')
Domain['Higher Education'].append('master')
Domain['Artificial Intelligence'].append('deep learning')
Domain['Artificial Intelligence'].remove('intelligence')

Event['Internships'].append('intern')
Event['Hackathons'].append('thon')
Event['Certifications'].append('certif')
Event['Certifications'].remove('certification')

def textPreprocessing(data):
#   StopwordsRemoval
    words = data.split()
    from nltk.corpus import stopwords
    removeStopwords = [word for word in words if word.lower() not in stopwords.words('english')]
    
    return removeStopwords

#This function is required to give output Domain(s) and Event(s).
def prefrences(words):
    text = ' '.join(words)
    i = True
    domain_list = []
    for domain in domains['domain']:
        for item1 in Domain[domain]:
            if item1 in text.lower():
                domain_list.append(domain)
#                 print('Domain: ',domain)
                i = False
    if i:
        domain_list.append('Other')
#         print('Domain: Other')
    event_list = []
    for event in events['event']:
        for item2 in Event[event]:
            if item2 in text.lower():
                event_list.append(event)
#                 print('Event: ',event)
    return domain_list,event_list
