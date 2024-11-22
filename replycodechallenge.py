r = lambda q: (q * 2) - (q // 2)
s = lambda q: (q * 3)+(q  // 3)
x = 2
x = r(x) + s(x)
x = r(x) - s(x)
print(x)