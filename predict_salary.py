
def predict_salary(response, worksite):

    salary_range = []
    vacancies_found = 0

    if worksite == 'headhunter':

        if response['items']:
            for vacancy in response['items']:
                if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
                    salary_range.append((int(vacancy['salary']['from'] or 0), int(
                        vacancy['salary']['to'] or 0)))

            vacancies_found = response["found"]

    if worksite == 'superjob':

        if response["objects"]:

            for vacancy in response["objects"]:

                if vacancy["payment_from"] != 0 or vacancy["payment_to"] != 0 and vacancy["currency"] == 'rub':
                    salary_range.append(
                        (vacancy["payment_from"], vacancy["payment_to"]))

            vacancies_found = response["total"]

    salary = []
    for payment_from, payment_to in salary_range:
        if payment_from == 0:
            salary.append(int(payment_to)*0.8)
        elif payment_to == 0:
            salary.append(int(payment_from)*1.2)
        else:
            salary.append((int(payment_to) + int(payment_from))/2)

    if salary:
        return (int(sum(salary)/len(salary)), len(salary), vacancies_found)
    else:
        return 0, 0, 0
