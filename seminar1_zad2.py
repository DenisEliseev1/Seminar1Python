# Задача 2. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


from secrets import randbits

x = bool (randbits (1))
y = bool (randbits (1))
z = bool (randbits (1))
print (type(x))
print (f'x={x} \ny= {y}, \nz={z}')
if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print (f'Утверждение ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}  является ИСТИННЫМ')
else:
    print (f'Утверждение ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}  является ЛОЖНЫМ')    