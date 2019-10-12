
def predict_salary(salary_range, total):
    salary = []
    for payment_from, payment_to in salary_range:
        if payment_from == 0:
            salary.append(int(payment_to)*0.8)
        elif payment_to == 0:
            salary.append(int(payment_from)*1.2)
        else:
            salary.append((int(payment_to) + int(payment_from))/2)

    if salary:
        return (int(sum(salary)/len(salary)), len(salary), total)
    else:
        return 0, 0, 0
