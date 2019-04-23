import requests


langs=['Python','PHP','Java','JavaScript','Ruby','C++','Objective-C','Swift','Go','C#']
number_found={}
for lang in langs:
    params={'text':f'программист {lang}','area':1,'period':1}
    url= requests.get('https://api.hh.ru/vacancies',params=params)
      
    number_found[lang] = url.json()['found']


print(number_found)