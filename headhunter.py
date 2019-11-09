import requests
from itertools import count
from predict_salary import predict_salary


def get_response_hh(programming_language):
    max_limit_pages_hh = 99
    full_data_in_pages = {}
    items = []
    for page in count(0):

        params = {
            "text": f"программист {programming_language}",
            "area": '1',
            "currency": "RUR",
            "page": page

        }

        response = requests.get('https://api.hh.ru/vacancies', params=params)
        response.raise_for_status()

        page_data = response.json()

        items += page_data["items"]

        if page >= page_data['pages'] or page == max_limit_pages_hh:
            full_data_in_pages["items"] = items
            full_data_in_pages["found"] = page_data["found"]

            break

    return full_data_in_pages


def get_statistics_hh(programming_languages):
    if isinstance(programming_languages, list):
        statistics = {}
        for programming_language in programming_languages:
            average_salary, vacancies_processed, vacancies_found = predict_salary(
                get_response_hh(programming_language), 'headhunter')
            statistics[programming_language] = {
                "vacancies_found": vacancies_found,
                "vacancies_processed": vacancies_processed,
                "average_salary": average_salary,
            }
        return statistics
    else:
        return 'Допустим только список '


if __name__ == "__main__":
    print(get_statistics_hh(['Python']))
