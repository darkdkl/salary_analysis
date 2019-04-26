import requests


langs=['Python','PHP','Java','JavaScript','Ruby','C++','Objective-C','Swift','Go','C#']


def predict_rub_salary(url):
   
    
    salars=[]
    
    for num_vac in range(0,len(url.json()['items'])):

        salary_from=url.json()['items'][num_vac]['salary']['from']
        salary_to=url.json()['items'][num_vac]['salary']['to']
        
        salary = 0
        
        if url.json()['items'][num_vac]['salary']['currency'] == 'RUR':
                      
            if salary_from is None:
                salary=salary_to*1.2
            elif salary_to is None:
                salary=salary_from*0.8
            else :
                salary=salary_from+salary_to
            
            salars.append(salary)

    average_salary=sum(salars)/len(salars)



    return int(average_salary)
    
        




def main(vacansy):

    params={'text':f'программист {vacansy}','area':1,'period':30,'only_with_salary':'True','currency':'RUR'}
    url= requests.get('https://api.hh.ru/vacancies',params=params)
    a=predict_rub_salary(url)
    return a
    vacancies_info={}
    




a=main(langs[0])
print (a)