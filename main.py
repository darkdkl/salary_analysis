import requests
from itertools import count
from headhunter import search_by_hh
from superjob import get_predict_rub_salary_sj
def main():

    langs = ['Python', 'PHP', 'Java', 'JavaScript',
             'Ruby', 'C++', 'Objective-C', 'Swift', 'Go', 'C#']
    for lang in langs:
        print(search_by_hh(lang))
        print('#'*80)
        print(get_predict_rub_salary_sj(lang))
if __name__ == "__main__":
    main()