 # Напишите программу, которая принимает на вход координаты точки 
 # (X и Y), и выдаёт номер четверти плоскости, в которой находится 
 # эта точка (или на какой оси она находится).

try:
    def numquart (x, y):              
            if x > 0 and y > 0:
                print (f'точка с координатами ({x}, {y}) находится в 1 четверти')
            elif x > 0 and y < 0:
                print (f'точка с координатами ({x}, {y}) находится в 2 четверти')
            elif x < 0 and y < 0:
                print (f'точка с координатами ({x}, {y}) находится в 3 четверти')
            elif x < 0 and y > 0:
                print (f'точка с координатами ({x}, {y}) находится в 4 четверти')
            print ('X и Y должны быть больше нуля')
    
    
    num1 = int (input ('Введите координату X - '))
    num2 = int (input ('Введите координату Y - '))
    numquart (num1, num2)
except:
    print ('Введите целое число')