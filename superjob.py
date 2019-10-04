import requests,os

headers={"X-Api-App-Id":os.getenv("X_Api_App_Id"),}

params={
        'keyword':'PHP',
        # 'town':'Москва',
        # 'catalogues':'Разработка, программирование',
        # 'currency':'rub'
    }

response=requests.get('https://api.superjob.ru/2.27/vacancies',headers=headers,params=params)


print(response.json())