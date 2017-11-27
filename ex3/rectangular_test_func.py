# -*- coding: utf-8 -*-
# Вычисления вручную для формулы прямоугольников

# Посчитаем вручную:
# 1 * f(1.5) + 1 * f(2.5) = 6.75 + 31.25 = 38

calculated_value = 38

def rectangular(f, a, b, n):
	h = float(b - a)/n
	result = f(a+0.5*h)
	for i in range(1, n):
		result += f(a + 0.5*h + i*h)
	result *= h
	return result

def test_func():
	result = rectangular(lambda x: 2 * (x ** 3), 1, 3, 2)
	print 'Результат вычисления с помощью функции rectangular:', result
	print 'Результат вычисления вручную:', calculated_value
	if result == calculated_value:
		print 'Равны'
	else:
		print 'Неравны'

test_func()
