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

        'vacancies_found': len(response.json()['objects']),
        'vacancies_processed':salary_info[1],
        'average_salary': salary_info[0]
    }

if __name__ == "__main__":
    get_predict_rub_salary_sj()