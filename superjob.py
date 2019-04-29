from dotenv import load_dotenv
import requests
import os
from itertools import count
from average_salary import predict_rub_salary



load_dotenv()
skey = os.getenv('SKEY')

def get_predict_rub_salary_sj(lang):
    url='https://api.superjob.ru/2.0/vacancies/'
    headers={
        'X-Api-App-Id':skey,
        
    
    }
    params={
        'keyword':f'{lang}',
        'town':'Москва',
        'catalogues':'Разработка, программирование',
        'currency':'rub'
    }

    salars={}
    vacancies_info = {}
    response=requests.get(url,headers=headers,params=params)
    # print(response.text)
    # print(response.json()['objects'][1]['catalogues'][0]['positions'][0]['id'])
    
    for num_vac in range(0,len(response.json()['objects'])):

        salary_from=response.json()['objects'][num_vac]['payment_from']
        salary_to=response.json()['objects'][num_vac]['payment_to']
        salars[salary_from]=salary_to
        salary_info = predict_rub_salary(
            salars)
    



    vacancies_info[lang] = {

        'vacancies_found': response.json()['total'],
        'vacancies_processed':'',
        'average_salary': len(response.json()['objects'])
    }

    print(vacancies_info[lang])
get_predict_rub_salary_sj('Python')