# -*- coding: utf-8 -*-
# Форматированный вывод

import math

pi = math.pi
y = 2

z = pi * y

print('Умножение {a:.5f} на {b:d} дает {c:.3f}'.format(a=pi, b=y, c=z))
