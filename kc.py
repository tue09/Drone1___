import math
def complex_modulo(z):
    a = z.real
    b = z.imag
    return math.sqrt(a**2+b**2)
def dis(x,y):
    m=x.real
    n=x.imag
    p=y.real
    q=y.imag
    return complex_modulo(x-y)


