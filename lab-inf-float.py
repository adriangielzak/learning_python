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

'''
    exercises
'''

# 1. Zadeklaruj zmienną name i przypisz do niej swoje imie

name = 'Adrian'

# 2. Zadeklaruj zmienną age i przypisz do niej wiek

age = 35

# 3. Zadeklaruj zmienną daysInYear i przypisz jej wartość 365

daysInYear = 365

# 4. Zadeklaruj zmienną message i przypisz jej wartość jak poniżej.
# Uwaga w miejscu ??? należy umieścić znaczniki pozwalające na wyświetlenie kolejno napisu i dwóch liczb
# '??? is ??? years old, so is about ??? days old'

message = "%s is %d years old, so is about %d days old"

# 5. Wyświetl informację jak poniżej (wykorzystaj funkcje formatowania napisów)j:
# Jan is 26 years old, so is about 9490 days old

print(message % (name, age, age * daysInYear))

# 6. Zmień imie i wiek w zmiennych name i age i jeszcze raz wyświetl komunikat korzystając z tej samej instrukcj
# co poprzednio

name = "Jasiu"
age = 1
print(message % (name, age, age * daysInYear))

# 7. Zmień wartość zmiennej message na:
# message = '{???} is {???} years old, so is about {???} days old'
# Ponownie w miejscu ??? należy umieścić odpowiednie napisy formatujące pozwalające wyświetlić napis i 2 liczby

message = "{0:s} is {1:d} years old, so is about {2:d} days old"

# 8. Stosując metodę format dla zmiennej message wyświetl komunikat w postaci:
# Chris is 17 years old, so is about 6205 days old

print(message.format(name, age, age * daysInYear))

# 9. Wyznacz wynik dzielenia całkowitego i resztę z dzielenia 1234567890 przez 12345:
# Wynik powinien wyglądać tak:
# 1234567890 divided by 12345 is 100005 and the rest is 6165

numberOne = 1234567890
numberTwo = 12345
divided = numberOne // numberTwo
rest = numberOne % numberTwo
message = "{0:d} divided by {1:d} is {2:d} and the rest is {3:d}"

print(message.format(numberOne, numberTwo, divided, rest))