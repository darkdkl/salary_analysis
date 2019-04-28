import requests
from itertools import count

def predict_rub_salary(page_data):

    salars = []

    for num_vac in range(0, len(page_data.json()['items'])):

        salary_from = page_data.json()['items'][num_vac]['salary']['from']
        salary_to = page_data.json()['items'][num_vac]['salary']['to']

        salary = 0

        if page_data.json()['items'][num_vac]['salary']['currency'] == 'RUR':

            if salary_from is None:
                salary = salary_to*1.2
            elif salary_to is None:
                salary = salary_from*0.8
            else:
                salary = salary_from+salary_to

            salars.append(salary)

    average_salary = sum(salars)/len(salars)

    return int(average_salary)


def search_by_hh(lang):

    
    vacancies_info = {}
    for page in count():
        params = {'text': f'программист {lang}', 'area': 1,
                  'period': 30, 'only_with_salary': 'True', 'currency': 'RUR',
                  'page':page
                  
                  }
        page_data = requests.get('https://api.hh.ru/vacancies', params=params)
        print(page_data.url)
        print(page_data.json()['pages'])
        if page >= page_data.json()['pages']:
            break

        vacancies_info[lang] = {

            'vacancies_found':  page_data.json()['found'],
            'vacancies_processed': page_data.json()['per_page']* page_data.json()['pages'],
            'average_salary': predict_rub_salary(page_data),
        }
        

    return vacancies_info



# def main():

#     langs = ['Python', 'PHP', 'Java', 'JavaScript',
#              'Ruby', 'C++', 'Objective-C', 'Swift', 'Go', 'C#']
#     for lang in langs:
#         search_by_hh(lang)
    
print(search_by_hh('Программист PHP'))