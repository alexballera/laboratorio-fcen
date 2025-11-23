# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
# %%
feriados = {}
feriados[(1,1)] = 'Año nuevo'
feriados[(1,5)] = 'Día del trabajador'
feriados[(13,9)] = 'Día del programador'
print(feriados)

cuadrados = dict([(1,1), (2,4), (3,9), (4,16)])
print(cuadrados[1])

for t in zip([1,2,3,4], [5,6,7,8]):
    print(t)

cuadrados2 = dict(zip([1,2,3,4], [5,6,7,8]))
print(cuadrados2[1])
# %%