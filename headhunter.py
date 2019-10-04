import requests
from itertools import count

def get_response_hh(vacancy):
    
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
                
        if page >= page_data['pages'] or page == 99:
            full_data_in_pages["items"]=items
            full_data_in_pages["found"]=page_data["found"]

            break
    
    
    return full_data_in_pages


def predict_rub_salary_hh(vacancy):
    

    response=get_response_hh(vacancy)
    
    rub_salary=[]

    if response['items']:
        for vacancy in response['items']:
            
            if vacancy['salary'] and vacancy['salary']['currency'] =='RUR':
                
                if vacancy['salary']['from'] is None:
                    
                    rub_salary.append(int(vacancy['salary']['to'])*0.8 )

                elif vacancy['salary']['to']  is None:
                    
                    rub_salary.append(int(vacancy['salary']['from'])*1.2 )
                else:
                    rub_salary.append ((int(vacancy['salary']['to']) +  int(vacancy['salary']['from']))/2 )
            
                
        return (int(sum(rub_salary)/len(rub_salary)),len(rub_salary),response["found"])
    
    else:
        return 0,0,0
        


def get_statistics_hh(vacancies):
    
    statistics={}
    for vacancy in vacancies:
        average_salary,vacancies_processed,vacancies_found =predict_rub_salary_hh(vacancy)
        statistics[vacancy]={
                            "vacancies_found": vacancies_found,
                            "vacancies_processed":vacancies_processed,
                            "average_salary":average_salary,

                            }
    return statistics


if __name__ == "__main__":
    print(get_statistics_hh('Python'))   



