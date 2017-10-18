# -*- coding: utf-8 -*-
# Программа для вычисления положения мяча при вертикальном движении

# 1  Привет  ^ SyntaxError: invalid syntax
# 2  Начальная скорость  ^ SyntaxError: invalid syntax
# 3  v0  5        #Начальная скорость  ^ SyntaxError: invalid syntax
# 4  3.0
# 6  pint y  ^ SyntaxError: invalid syntax
# 7 3.0

v0 = 5  # Начальная скорость
g = 9.81  # Ускорение свободного падения
t = 0.6  # Время

y = v0*t - (1/2.)*g*t**2

print y
