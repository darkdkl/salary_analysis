from dotenv import load_dotenv
import requests
import os
from itertools import count
from average_salary import predict_rub_salary



load_dotenv()
skey = os.getenv('SKEY')

def get_predict_rub_salary_sj():
    url='https://api.superjob.ru/2.0/vacancies/'
    headers={
        'X-Api-App-Id':skey,
        
    
    }
    params={
        'keyword':'Программист',
        'town':'Москва'
    }
    response=requests.get(url,headers=headers,params=params)
    for vac in count():
        try:
            print(response.json()['objects'][vac]['profession'],',',response.json()['objects'][vac]['town']['title'])
        except IndexError as error:
            break
