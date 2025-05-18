#Вариант 19
import numpy
import pandas

numpy.random.seed(242)
s = pandas.Series(numpy.random.normal(size=150))
s = s * 3
s.index = s.index * 2
number = (s[s.index <= 150] > 0).sum()
print(number)
