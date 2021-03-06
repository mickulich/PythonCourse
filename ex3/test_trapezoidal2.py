#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python 3.5.3

def trapezoidal(f, a, b, n):
	"""
	Вычисляет приближенное значение интеграла с помощью формулы трапеций
	f - подынтегральная функция
	a, b - пределы интегрирования
	n - количество частичных отрезков
	"""
	h = float(b - a)/n
	result = 0.5*(f(a) + f(b))
	for i in range(1, n):
		result += f(a + i*h)
	result *= h
	return result


def test_trapezoidal_one_exat_value():
	"""
	Тестирование на результатах, полученных в ручную
	"""
	from math import exp
	v = lambda x: 3*x**2*exp(x**3)
	n = 2
	expected = 2.463642041244344
	computed = trapezoidal(v, 0, 1, 2)
	rel_error = abs(expected - computed)
	tol = 1E-15
	success = rel_error < tol
	msg = 'погрешность = %.17f больше допуска = %.17f' % (rel_error, tol)
	assert success, msg


def test_trapezoidal_linear():
	"""
	Тестирование равенства нулю погрешности для линейной функции
	"""
	v = lambda x: 6 * 10**8 * x - 2 * 10 ** 6
	V = lambda x: 3 * 10**8 * x**2 - 2 * 10 ** 6 * x
	a = 1.1; b = 1.4
	expected = V(1.4) - V(1.1)
	tol = 1E-7
	for n in 2, 20, 21:
		computed = trapezoidal(v, a, b, n)
		rel_error = abs(expected - computed)
		success = rel_error < tol
		msg = 'n = %d, погрешность: %g' % (n, rel_error)
		assert success, msg


def convergence_rates(f, F, a, b, num_exp = 14):
	"""
	Вычисляются порядки точности для последовательных экспериментов
	Входные параметры:
	f --- подынтегральная функция
	F --- первообразная
	a, b --- пределы интегрирования
	num_exp --- количество последовательных эксперимнетов

	Возвращает массив r со значениями порядков точности
	"""
	from math import log
	from numpy import zeros
	expected = F(b) - F(a)
	n = zeros(num_exp, dtype=int)
	E = zeros(num_exp)
	r = zeros(num_exp - 1)
	for i in range(num_exp):
		n[i] = 2**(i+1)
		computed = trapezoidal(f, a, b, n[i])
		E[i] = abs((expected - computed)/expected)
		if i > 0:
			r_im1 = log(E[i]/E[i-1])/log(float(n[i]/n[i-1]))
			r[i-1] = float('%.2f' % r_im1) # оставляем только два знака после запятой
	return r


def test_trapezoidal_conv_rate():
	"""
	Сравниваем вычисленные порядки точности с ожидаемым -2.
	"""
	from math import exp
	v = lambda x: 3*(x**2)*exp(x**3)
	V = lambda x: exp(x**3)
	a = 1.1; b = 1.4
	r = convergence_rates(v, V, a, b)
	print r
	tol = 0.01
	msg = str(r[-4:]) # выводим 4 последних значения массива
	success = (abs(r[-1]) - 2) < tol # сравниваем последнее значение массива
	assert success, msg
