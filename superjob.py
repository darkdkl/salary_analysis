import requests
import os
from itertools import count
from predict_salary import predict_salary
from dotenv import load_dotenv


def get_response_sj(programming_language):

    headers = {"X-Api-App-Id": os.getenv("X_API_APP_ID"), }

    full_data_in_pages = {}
    items = []
    for page in count(0):
        params = {
            'keyword': f"программист {programming_language}",
            'catalogues[]': 48,
            'town': 'Москва',
            'currency': 'rub',
            "count": 100,
            "page": page

        }

        response = requests.get(
            'https://api.superjob.ru/2.27/vacancies', headers=headers, params=params)
        response.raise_for_status()
        page_data = response.json()
        items += page_data["objects"]

        if not page_data["objects"]:
            full_data_in_pages["objects"] = items
            full_data_in_pages["total"] = page_data["total"]

            break

    return full_data_in_pages


def get_statistics_sj(programming_languages):

    if isinstance(programming_languages, list):

        statistics = {}

        for programming_language in programming_languages:

            average_salary, vacancies_processed, vacancies_found = predict_salary(
                get_response_sj(programming_language), 'superjob')

            statistics[programming_language] = {
                "vacancies_found": vacancies_found,
                "vacancies_processed": vacancies_processed,
                "average_salary": average_salary,
            }
        return statistics
    else:
        return 'Допустим только список '


if __name__ == "__main__":
    load_dotenv()
    print(get_statistics_sj(['PHP']))
