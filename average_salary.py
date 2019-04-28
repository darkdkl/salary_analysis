def predict_rub_salary(salars):
    
    salary = []
    for salary_from  in salars:
       

        if salary_from is None:
            salary.append(salars[salary_from]*1.2)
        elif salars[salary_from] is None:
            salary.append(salary_from*0.8)
        else:
            salary.append(salary_from+salars[salary_from])

        average_salary = sum(salary)/len(salars)

  
    print(salary)

    print(average_salary)

    return int(average_salary), len(salary)