import requests,os
from itertools import count

def get_response_sj(vacancy):
    
    headers={"X-Api-App-Id":os.getenv("X_Api_App_Id"),}
    
    full_data_in_pages={}
    items=[]
    for page in count(0):
        params={
                'keyword':f"программист {vacancy}",
                'catalogues[]': 48,
                'town':'Москва',
                'currency':'rub',
                "count":100,
                "page":page
                
            }

        response=requests.get('https://api.superjob.ru/2.27/vacancies',headers=headers,params=params)
        response.raise_for_status()
        page_data = response.json()
        items+=page_data["objects"]

        
        if not response.json()["objects"]:
            
            full_data_in_pages["objects"]=items
            full_data_in_pages["total"]=page_data["total"]
            
            break
    
    return full_data_in_pages





def predict_rub_salary_for_sj(vacancies):
    response=get_response_sj(vacancies)
    if response["objects"]:
        rub_salary=[]
        for vacancy in response["objects"]:
            
            if vacancy["payment_from"] !=0 or vacancy["payment_to"] != 0 and vacancy["currency"] == 'rub':
                
                if vacancy["payment_from"] == 0:
                    
                    rub_salary.append(int(vacancy["payment_to"])*0.8 )

                elif vacancy["payment_to"]  == 0:
                    
                    rub_salary.append(int(vacancy["payment_from"])*1.2 )
                else:
                    rub_salary.append ((int(vacancy["payment_to"]) +  int(vacancy["payment_from"]))/2 )

        return (int(sum(rub_salary)/len(rub_salary)),len(rub_salary),response["total"])
    else:
        return 0,0,0


def get_statistics_sj(vacancies):
    
    statistics={}
    for vacancy in vacancies:
        average_salary,vacancies_processed,vacancies_found =predict_rub_salary_for_sj(vacancy)
        statistics[vacancy]={
                        "vacancies_found": vacancies_found,
                        "vacancies_processed":vacancies_processed,
                         "average_salary":average_salary,

                            }
    return statistics

if __name__ == "__main__":
    print(get_statistics_sj('Python'))