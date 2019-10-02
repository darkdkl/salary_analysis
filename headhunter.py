import requests




def predict_rub_salary(vacancy):
    params={
                "text":f"программист {vacancy}",
                "area":'1',
                "date_from":"2019-09-01",
                "date_to":"2019-10-01",
                "currency":"RUR",

            }
    response=requests.get('https://api.hh.ru/vacancies',params=params)

    

    for vacancy in response.json()['items']:
        
        if vacancy['salary'] and vacancy['salary']['currency'] =='RUR':
            
            if vacancy['salary']['from'] is None:
                
                yield int(vacancy['salary']['to'])*0.8

            elif vacancy['salary']['to']  is None:
                
                yield int(vacancy['salary']['from'])*1.2
            else:
                yield (int(vacancy['salary']['to']) +  int(vacancy['salary']['from']))/2
        else:
            yield None
             
    
        

g=predict_rub_salary('Python')
for sg in g:
    print(sg)

# langs = ['Python', 'PHP', 'Java', 'JavaScript',
    #          'Ruby', 'C++', 'Objective-C', 'Swift', 'Go', 'C#']