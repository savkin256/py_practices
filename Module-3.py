#!/usr/bin/env python
# coding: utf-8

# In[13]:


## Part 1 Level 1

def input_number():

    # input only numeric
    
    while True:
        number = input()
        if number.isnumeric():
            return number
        else:
            print("    ОШИБКА, разрешены только числа, введите еще раз: ", end='')


def annual_deposit_calc(deposit_amount, deposit_interest):

    # annual deposit calculation:
    # initial ammount + percents, and convert to INT

    return(int(deposit_amount*(100+deposit_interest)/100))


def syntax_years(years):
    
    # returns right ending depends on last digit

    # last digit
    last = abs(years) % 10
    
    # last two digit
    last2 = abs(years) % 100
    
    # conditions
    if last == 0 or 5 <= last <= 9 or 5 <= last2 <= 20:
        return('лет')
    elif last == 1:
        return('год')
    elif 2 <= last <= 4:
        return('года')
    

def main():
    
    # input initial deposit ammount
    print('Введите начальную сумму депозита: ', end = '')
    x = float(input_number())

    # input deposit interest
    print('Введите процент по депозиту: ', end = '')
    p = int(input_number())
    
    # input target deposit ammount
    print('Введите желаемую сумму вклада с учетом полученных процентов: ', end = '')
    y = float(input_number())
    
    # years count
    y_count = 0
    
    while x < y:
        x = annual_deposit_calc(x, p)
        y_count += 1

    if y_count == 0:
        print('У вас уже есть требуемая сумма, копить не надо, УРА!')
    else:
        print('Вам понадобится минимум', y_count, syntax_years(y_count), ', и Вы накопите', x, 'рублей')
        
if __name__ == '__main__':
    main()


# In[12]:


## Part 1 Level 2

def main():
    
    n = int(input())
    count = 0
    
    while count < n:
        print('for - частный случай цикла while')
        count += 1
    
if __name__ == '__main__':
    main()


# In[16]:


## Part 1 Level 3

def main():
    
    number = int(input())
    summ = 0
    
    for digit in str(number):
        summ += int(digit)
    
    print(summ)
    
if __name__ == '__main__':
    main()


# In[19]:


## Part 2 Level 1

def main():
    
    L = [1, 4, 1, 6, 7, "hello", "a", 5, "hello", "7"]
    RESULT = []
    
    for index1 in range(0, len(L)):

        for index2 in range(index1+1, len(L)):
            
            if L[index1] == L[index2]:
                RESULT.append(L[index1])
                
    print(RESULT)

if __name__ == '__main__':
    main()


# In[24]:


## Part 2 Level 2

from random import randint

def create_matrix(size):
    return([[randint(0, 100) for i in range(size)] for j in range(size)])

def main():
    
    matrix_size = int(input('Введите размерность матрицы: '))
    matrix = create_matrix(matrix_size)
    maximum = 0
       
    for string in matrix:
        
        print(string)
        
        for element in string:
            if maximum < element:
                maximum = element
    
    print('Максимальный элемент:', maximum)
    
if __name__ == '__main__':
    main()


# In[29]:


## Part 2 Level 3 (variant with new dict)

def main():
    
    d = {"Ann": 15, "Joe": 14, "Nike": 5, "Steve": 18}
    out = {}
    
    for name, age in d.items():
        out.update({age: name})
    
    print(out)
        
        
if __name__ == '__main__':
    main()


# In[34]:


## Part 2 Level 3 (variant with modification of existing dict)

def main():
    
    d = {"Ann": 15, "Joe": 14, "Nike": 5, "Steve": 18}
    
    for name in list(d.keys()):
        d.update({d[name]: name})
        d.pop(name)
    
    print(d)
        
        
if __name__ == '__main__':
    main()


# In[55]:


## Part 3 Level 1

def area(a, b, c):
    
    p = (a + b + c)/2
    return ((p * (p - a) * (p - b) * (p - c)) ** 0.5)

def main():
    
    side_one, side_two, side_three = map(int, input('Введите стороны треугольника через пробел: ').split())
    print('Площадь треугольника =', area(side_one, side_two, side_three))
        
if __name__ == '__main__':
    main()


# In[77]:


## Part 3 Level 2

def main():
    
    s = '''Было просто пасмурно, дуло с севера,
    А к обеду насчитал сто градаций серого.
    Так всегда первого ноль девятого,
    То ли весь мир сошёл с ума, то ли я - того...
    На столе записка от неё смятая,
    Недопитый виски допиваю с матами.
    Посмотрю в окно, допишу главу,
    Первое сентября, дворник жжёт листву.
    И серым облакам наплевать на нас,
    Если знаешь как жить - живи,
    Ты хотела быть как все - так плыви!'''

    s_new = []
    word = ''

    for i in s:
        if i != ' ' and i.isalpha():
            word += i
        else:
            if len(word) < 5  and  word != '':
                s_new.append(word)
            word = ''

    print(s_new)

if __name__ == '__main__':
    main()


# In[ ]:





# In[120]:


## Part 3 Level 3

from random import randint

def quicksort(nums):
    
    nums_len = len(nums)
    
    if nums_len == 0:
        return []
    
    elif nums_len == 1:
        return nums
    
    else:
        
        pivot = nums[0]
        
        smaller = []
        bigger = []
        pivot_list = []
        pivot_list.append(pivot)
    
        i = 1
        
        while i < nums_len:
 
            # debug string
            # print('\n', nums[i], pivot, first_is_smaller(nums[i], pivot), '\n')
    

            if first_is_smaller(nums[i], pivot):
                smaller.append(nums[i])
            else:
                bigger.append(nums[i])
            
            i += 1
    
    return(quicksort(bigger) + pivot_list + quicksort(smaller))
    

def first_is_smaller(num1, num2):

    num1_str = str(num1)
    num2_str = str(num2)
    
    len1 = len(num1_str)
    len2 = len(num2_str)

    i = 1
    j = 1
    
    # in the begining, compare numbers just by first digit
    if int(num1_str[0]) < int(num2_str[0]):
        return True
    elif int(num1_str[0]) > int(num2_str[0]):
        return False

    # in case of first digits are equal
    else:
    
        # if lengths are equal, then simply compare numbers
        if len1 == len2:

            if num1 <= num2:
                return True
            else:
                return False
    
        # if lengths are not equal, compare digits by digits

        # in case of first number is shorter
        elif len1 < len2:
            
                while j < len2:
                    
                    # if we have reached end of shorter, than start it over
                    if i == len1:
                        i = 0
                        
                    if int(num1_str[i]) < int(num2_str[j]):
                        return True
                    elif int(num1_str[i]) > int(num2_str[j]):
                        return False
                    
                    i += 1
                    j += 1
                
        # in case of second number is shorter
        else:
            
                while j < len1:
                    
                    if i == len2:
                        i = 0
                        
                    if int(num2_str[i]) < int(num1_str[j]):
                        return False
                    elif int(num2_str[i]) > int(num1_str[j]):
                        return True
                    
                    i += 1
                    j += 1
                    
        # if we here, than numbers are fully identical
        # and no matter what will be smaller.
        # 
        # let first will be smaller
        return True


def main():

    massive = [randint(0,99) for i in range(5)]

#     massive = [56, 9, 11, 2]
#     massive = [3, 81, 5]
    
    print(massive, '->', int(''.join(map(str, quicksort(massive)))))

    
if __name__ == '__main__':
    main()


# In[152]:


## Part 4 Level 1

from getpass import getpass
import json

def register(login, passwd):

    file_name = 'credentials.json'
    path = Path(file_name)
    credentials = {}
    
    try:
        with open(file_name, 'r') as file:
            credentials = json.load(file)
    except:
        pass

    credentials.update({login: passwd})
    with open(file_name, 'w') as file:
        json.dump(credentials, file)


def main():

    username = input('Username: ')
    password = getpass('Password: ')

    register(username, password)

if __name__ == '__main__':
    main()


# In[155]:


## Part 4 Level 2

from getpass import getpass
import json

def register(login, passwd):

    file_name = 'credentials.json'
    path = Path(file_name)
    credentials = {}
    
    try:
        with open(file_name, 'r') as file:
            credentials = json.load(file)
    except:
        pass
    
    if login in credentials:
        print('This username is busy')
    else:
        credentials.update({login: passwd})
        with open(file_name, 'w') as file:
            json.dump(credentials, file)
        print('You have successfully registered')


def main():

    username = input('Username: ')
    password = getpass('Password: ')

    register(username, password)

if __name__ == '__main__':
    main()


# In[164]:


## Part 4 Level 3

from getpass import getpass
import json


file_name = 'credentials.json'


def enter_cred():
    username = input('Username: ')
    password = getpass('Password: ')
    return(username, password)


def register(login, passwd):

    path = Path(file_name)
    credentials = {}
    
    try:
        with open(file_name, 'r') as file:
            credentials = json.load(file)
    except:
        pass
    
    if login in credentials:
        print('This username is busy')
    else:
        credentials.update({login: passwd})
        with open(file_name, 'w') as file:
            json.dump(credentials, file)
        print('You have successfully registered')

        
def login(login, passwd):

    try:
        with open(file_name, 'r') as file:
            credentials = json.load(file)
    except:
        print('Database is not available, sorry for inconvenience')
        return
    
    if login in credentials:
        if passwd == credentials[login]:
            print('You have successfully login')
        else:
            print('Username or password is not correct')
    else:
        print('Username or password is not correct')



def main():

    way = input ('Enter what you want to do:\n\t1 - Register as new user\n\t2 - Login as existing user\n')
    
    username, password = enter_cred()
    
    while True:
        if way == '1':
            register(username, password)
            break
        elif way == '2':
            login(username, password)
            break
        else:
            print('Please, press 1 or 2')

            
if __name__ == '__main__':
    main()


# In[ ]:




