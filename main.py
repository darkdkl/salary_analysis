
from __future__ import print_function

from terminaltables import AsciiTable, DoubleTable, SingleTable
from superjob import get_statistics_sj
from headhunter import get_statistics_hh

def make_table(job_search_sites_name,statistics_data):
    
    title=f'{job_search_sites_name}Moskow'
    table_data=[ ]
    table_data.append(['Язык программирования',
                        'Вакансий найдено ',
                        'Вакансий обработано',
                        'Средняя зарплата'])

    for prog_lang in statistics_data.items():
        table_data.append([prog_lang[0],
                           prog_lang[1]['vacancies_found'],
                           prog_lang[1]['vacancies_processed'],
                           prog_lang[1]['average_salary']])
       
      
    table = AsciiTable(table_data,title)
    print (table.table)




def main():


    langs = ['Python', 'PHP', 'Java', 'JavaScript',
             'Ruby', 'C++', 'Objective-C', 'Swift', 'Go', 'C#']

    make_table('SuperJob ',get_statistics_sj(langs))
    make_table('HeadHunter',get_statistics_hh(langs))
    

if __name__ == '__main__':
    main()