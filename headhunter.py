import requests
from itertools import count

def get_response(vacancy):
    
    full_data_in_pages={}
    items=[]
    for page in count(0):
        
        params={
                "text":f"программист {vacancy}",
                "area":'1',
                "date_from":"2019-09-01",
                "date_to":"2019-10-01",
                "currency":"RUR",
                "page":page

            }

        response = requests.get('https://api.hh.ru/vacancies',params=params)
        response.raise_for_status()
        
        
        page_data = response.json()
        
        items+=page_data["items"]
                
        if page >= page_data['pages'] or page == 99:
            full_data_in_pages["items"]=items
            full_data_in_pages["found"]=page_data["found"]

            break
    
    
    return full_data_in_pages


def predict_rub_salary(vacancy):
    

    response=get_response(vacancy)
    rub_salary=[]
    for vacancy in response['items']:
        
        if vacancy['salary'] and vacancy['salary']['currency'] =='RUR':
            
            if vacancy['salary']['from'] is None:
                
                rub_salary.append(int(vacancy['salary']['to'])*0.8 )

            elif vacancy['salary']['to']  is None:
                
                rub_salary.append(int(vacancy['salary']['from'])*1.2 )
            else:
                rub_salary.append ((int(vacancy['salary']['to']) +  int(vacancy['salary']['from']))/2 )
        
            
    return (int(sum(rub_salary)/len(rub_salary)),len(rub_salary),response["found"])
    
        


def get_statistics(vacancies):
    
    statistics={}
    for vacancy in vacancies:
        average_salary,vacancies_processed,vacancies_found =predict_rub_salary(vacancy)
        statistics[vacancy]={
                        "vacancies_found": vacancies_found,
                        "vacancies_processed":vacancies_processed,
                         "average_salary":average_salary,

                            }
    return statistics



langs = ['Python', 'PHP', 'Java', 'JavaScript',
             'Ruby', 'C++', 'Objective-C', 'Swift', 'Go', 'C#']



a=get_statistics(langs)

print(a)

