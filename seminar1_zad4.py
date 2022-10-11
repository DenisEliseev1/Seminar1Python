# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, после чего применяет операцию к введённым числам 
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

try:
    number1 = float (input ('Введите первое значение'))
    number2 = float (input ('Введите второе значение'))
    num_move = input (f'Введите необходимое действие +, -, /, *, mod, pow, div, где \nmod — это взятие остатка от деления\npow — возведение в степень \ndiv — целочисленное деление\nВаше действие - ')     
    if num_move == '+':
        result = number1 + number2
        print (f'{number1} + {number2} = {result}')
    elif num_move == '-':
        result = number1 - number2
        print (f'{number1} - {number2} = {result}')
    elif num_move == '*':
        result = number1 * number2
        print (f'{number1} * {number2} = {result}')
    elif num_move == '/':
        if number2 == 0:
            print ('ошибка! деление на ноль!')
        else:
            result = number1 / number2
            print (f'{number1} / {number2} = {result}')
    elif num_move == 'mod':
        if number2 == 0:
            print ('ошибка! деление на ноль!')
        else:
            result = number1 % number2
            print (f'{number1} mod {number2} = {result}')
    elif num_move == 'div':
        if number2 == 0:
            print ('ошибка! деление на ноль!')
        else:
            result = number1 // number2
            print (f'{number1} div {number2} = {result}')
    elif num_move == 'pow':
        result = number1 ** number2
        print (f'{number1} в степени {number2} = {result}')
    else:    
        print (f'Действие не из списка доступных')            
except:
    print (f'Некорректно введённые значения: \nПервое и второе значения - числовые, \nДействия могут быть только в выбранном диапазоне')