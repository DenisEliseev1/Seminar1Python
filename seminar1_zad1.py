# задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
try:
    print ('Введите номер дня недели, где \n 1-понедельник \n 2 - вторник \n и т.д.')
    day = 0
    while 0 >= day or day > 7:
        day = int (input ('Номер дня недели - '))
        if day == 6 or day == 7:
            print ('Ура, выходной')
        elif 0 < day < 6:
            print ('Не выходной(')
        else:
            print ('Не корректно задано число, повторите ввод')
except:
    print ('введите целое число')