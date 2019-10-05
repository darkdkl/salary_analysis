import requests
from itertools import count
from predict_salary import predict_salary

def get_response_hh(vacancy):
    max_limit_pages_hh=99
    full_data_in_pages={}
    items=[]
    for page in count(0):
        
        params={
                "text":f"программист {vacancy}",
                "area":'1',
                "currency":"RUR",
                "page":page

            }

        response = requests.get('https://api.hh.ru/vacancies',params=params)
        response.raise_for_status()
        
        
        page_data = response.json()
        
        items+=page_data["items"]
                
        if page >= page_data['pages'] or page == max_limit_pages_hh:
            full_data_in_pages["items"]=items
            full_data_in_pages["found"]=page_data["found"]

            break
    
    
    return full_data_in_pages


def predict_rub_salary_hh(vacancy):
    
    response=get_response_hh(vacancy)
    
    salary=[]

    if response['items']:
        for vacancy in response['items']:
            if vacancy['salary'] and vacancy['salary']['currency'] =='RUR':
                salary.append((int(vacancy['salary']['from'] or 0),int(vacancy['salary']['to'] or 0) ))
    
        return predict_salary(salary,response["found"])
              
    else:
        return 0,0,0
        


def get_statistics_hh(vacancies):
    if type(vacancies) is list:
        statistics={}
        for vacancy in vacancies:
            average_salary,vacancies_processed,vacancies_found =predict_rub_salary_hh(vacancy)
            statistics[vacancy]={
                                "vacancies_found": vacancies_found,
                                "vacancies_processed":vacancies_processed,
                                "average_salary":average_salary,

                                }
        return statistics
    else:
        return 'Допустим только список '

if __name__ == "__main__":
    print(get_statistics_hh(['Python']))   



