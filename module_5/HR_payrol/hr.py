
# PayrollSystem реализует метод .calculate_payroll(),
# который принимает коллекцию сотрудников
# и печатает их идентификатор, имя и сумму чека,
# используя метод .calculate_payroll(),
# представленный для каждого объекта сотрудника.
class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')


# Employee является базовым классом
# для всех типов сотрудников.
# Он объявлен с id и name.
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# Класс SalaryEmployee наследует Employee
# и инициализируется с помощью id и name, требуемыми базовым классом.
# Метод __init__ суперкласса (базового класса)
# вызывается через super()
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


# Класс HourlyEmployee инициализируется
# с помощью id и name, переменных базового класса,
# плюс hours_worked и hour_rate, необходимые для
# расчета заработной платы. Метод .calculate_payroll()
# реализован путем возврата отработанных часов,
# умноженных на часовую ставку.
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


# CommissionEmployee является подклассом SalaryEmployee,
# потому что оба класса имеют weekly_salary, + дополнительная
# надбавка commission, основанная на продажах для сотрудника
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


