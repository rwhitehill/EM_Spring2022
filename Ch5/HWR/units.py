#!/usr/bin/env python3

from pint import UnitRegistry
from numpy import pi

ureg = UnitRegistry()
Q_ = ureg.Quantity

D = Q_(8.96,'g/cm**3') #density
NA = Q_(6.022e23,'1/mol') #avogadro
e = Q_(1.602e-19,'C') #electron charge
M = Q_(63.546,'g/mol') #molar mass

rho = e*D*NA/M
rho = rho.to('C/m**3')

print(f'{rho:~.3e}')

I = Q_(1,'A')
d = Q_(1,'mm')

v = 4*pi*I/rho/d**2
v = v.to('m/s')

print(f'{v:~.3e}')
v = v.to('mph')
print(f'{v:~.3e}')

