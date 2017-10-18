# -*- coding: utf-8 -*-
# Объем 3-ёх кубов

import numpy
import matplotlib.pyplot as plt

volumeLength = numpy.linspace(1, 3, 3)
volumeValue = volumeLength ** 3

plt.plot(volumeLength, volumeValue)
plt.xlabel('length')
plt.ylabel('value')
plt.show()
