# -*- coding: utf-8 -*-
# Площадь круга и окружности

# Посчитаем вручную:
# 1 * (f(1) + f(2)) / 2 + 1 * (f(2) + f(3)) / 2 =
# (2 + 16) / 2 + (16 + 54) / 2 = 9 + 35 = 44

calculated_value = 44

def trapezoidal(f, a, b, n):
	h = float(b - a) / n
	result = 0.5 * (f(a) + f(b))
	for i in range(1, n):
		result += f(a + i * h)
	result *= h
	return result

def test_func():
	result = trapezoidal(lambda x: 2 * (x ** 3), 1, 3, 2)
	print 'Результат вычисления с помощью функции trapezoidal:', result
	print 'Результат вычисления вручную:', calculated_value
	if result == calculated_value:
		print 'Равны'
	else:
		print 'Неравны'

test_func()
