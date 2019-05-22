import requests
from itertools import count
from average_salary import predict_rub_salary





def search_by_hh(lang):

    vacancies_info = {}
    salars={}
    number_of_vac=0

    for page in count():
        params = {'text': f'программист {lang}', 'area': 1,
                  'period': 30, 'only_with_salary': 'True', 'currency': 'RUR',
                  'page': page

                  }
        page_data = requests.get('https://api.hh.ru/vacancies', params=params)

        # print(page_data.json()['pages'])
        
       
        if page >= page_data.json()['pages']:
            break
    
        for num_vac in range(0, len(page_data.json()['items'])):
            
            if page_data.json()['items'][num_vac]['salary']['currency'] != 'RUR':
                break
                       

            salary_from=page_data.json()['items'][num_vac]['salary']['from']
            salary_to=page_data.json()['items'][num_vac]['salary']['to']
 
            salars[salary_from]=salary_to
            
            
    salary_info = predict_rub_salary(
            salars)
            
    
    vacancies_info[lang] = {

        'vacancies_found': page_data.json()['found'],
        'vacancies_processed': salary_info[1],
        'average_salary': salary_info[0],
    }

    return vacancies_info


