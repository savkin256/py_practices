# композиция

class Salary:

    def __init__(self, pay):
        self.pay = pay

    # Расчет годовой зарплаты
    def get_total(self):
        return self.pay * 12


class Employee:

    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        # Атрибут - объект класса Salary
        self.salary = Salary(pay)

    # Годовая зарплата = зарплата за 12 месяцев + бонус
    def annual_salary(self):
        # Для расчета годовой зарплаты вызываем метод get_total класса Salary
        return self.bonus + self.salary.get_total()


Engineer = Employee(1000, 500)
print(Engineer.annual_salary())

