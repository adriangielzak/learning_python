print(8 * 3)

five = 5
three = 3
print(five * three)

print(type(five))

print(type(five * three))

print(five / three)

print(type(five / three))

import sys
print(sys.maxsize)

veryBigValue = 99999999999999999999999999999999999999999999999999
print(veryBigValue)
print(veryBigValue + 1)
print(type(veryBigValue))

print((veryBigValue + 1) / 2)
print(type((veryBigValue + 1) / 2))

print("Dzielenie całkowite //", five // three)
print("Reszta z dzielenia modulo %", five % three)

print("Rzutowanie napisu 'inf' (od infinity - nieskończoność) do typu float", float('inf'))
print("Czy float('inf) > od 9999999999999999999999999999999999 -", float('inf') > 9999999999999999999999999999999999)

print("Minus nieskończoność - '-float('inf')'")