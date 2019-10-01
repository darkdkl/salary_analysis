import requests


def searh_vacansy():

    langs = ['Python', 'PHP', 'Java', 'JavaScript',
             'Ruby', 'C++', 'Objective-C', 'Swift', 'Go', 'C#']

    number_of_vacancies={}
    for lang in langs:

        params={
            "text":f"программист{lang}",
            "area":'1',
            "date_from":"2019-09-01",
            "date_to":"2019-10-01"
                }

        response=requests.get('https://api.hh.ru/vacancies',params=params)
        number_of_vacancies[lang]=response.json()["found"]

    return number_of_vacancies
        


print(searh_vacansy())