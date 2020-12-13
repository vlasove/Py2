"""
Скоро конец декабря, а значит пришло время посчитать зарплату и премии
"""


class Employee:
    """
    pYLINT отвали
    """

    def __init__(self, basic_salary_per_month, coeff_premia):
        self.__salary = basic_salary_per_month
        self.__premia = basic_salary_per_month * coeff_premia

    def pay(self):
        return self.__salary + self.__premia


class Freelancer:
    """
    Умное описание для класса Freelancer
    """

    def __init__(self, salary_per_hour, hours):
        self.__salary = salary_per_hour * hours

    def pay(self):
        return self.__salary

    def drink_smoothie(self):
        print("Drink kiwi smoothie!")


class Intern:
    def __init__(self):
        pass

    def pay(self, plushka: int = 10):
        return 10 + plushka


TOTAL_SALARY = 0
employees = [
    Employee(
        100, 1.3), Employee(
            200, 1.5), Employee(
                90, 4.5), Freelancer(
                    5, 40), Freelancer(
                        2.5, 75), Intern(), Intern()]
for employee in employees:
    TOTAL_SALARY += employee.pay()
print("Amount $:", TOTAL_SALARY)


def main():
    command = input()
    if command == "Employee":
        basic_salary = input()
        coeff_preimea = input()
        employes.append(Employee(basic_salary, coeff_preimea))
    elif command = "Freelancer":
        salary_per_hour = input()
        hours = input()
        emplyees.append(Freelancer(salary_per_hour, hours))