# -*- coding: utf-8 -*-
# Вычислить простой интеграл

# Посчитаем вручную:
# I = (6^3 - 2^3) / 3 - (6^2 - 2^2) / 2 = 53.(3)

calculated_value = 160/3

def trapezoidal(f, a, b, n):
	h = float(b - a)/n
	result = 0.5*(f(a) + f(b))
	for i in range(1, n):
		result += f(a + i*h)
	result *= h
	return result

def rectangular(f, a, b, n):
	h = float(b - a)/n
	result = f(a+0.5*h)
	for i in range(1, n):
		result += f(a + 0.5*h + i*h)
	result *= h
	return result

trap_2 = trapezoidal(lambda x: x * (x - 1), 2, 6, 2)
trap_100 = trapezoidal(lambda x: x * (x - 1), 2, 6, 100)
rect_2 = rectangular(lambda x: x * (x - 1), 2, 6, 2)
rect_100 = rectangular(lambda x: x * (x - 1), 2, 6, 100)

print '--Точное значение интеграла: ', calculated_value

print '--Аппроксимация трапециями:\n' '2 трапеции:', trap_2
print '100 трапеций: ', trap_100

print '--Погрешность для аппроксимации трапециями:\n' '2 трапеции:', abs(trap_2 - calculated_value)
print '100 трапеций: ', abs(trap_100 - calculated_value)

print '--Аппроксимация трапециями:\n' '2 трапеции:', rect_2
print '100 трапеций: ', rect_100

print '--Погрешность для аппроксимации трапециями:\n' '2 трапеции:', abs(rect_2 - calculated_value)
print '100 трапеций: ', abs(rect_100 - calculated_value)
