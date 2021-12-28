title = "Python"
print("title is", type(title))

version = 3
print("version is", type(version))

progress = 0.21
print("progress is", type(progress))

print("This expression is", type(progress * version))

x = 1
y = 1
z = 1
print(x, y, z)

a = b = c = 2
print(a, b, c)

c = 3
print(a, b, c)

print(2 + 2 * 2)

print(6 / 2 * (1 + 2))

print(4 ** 3 ** 2)

print(4 ** 9)

print("4 ** 3 ** 2 = 4 ** 9")

x = 1
print("x =", x)
print("x + 1 =", x + 1)
print("x =", x)
x = x + 1
print("x = x + 1 =", x)
x += 1
print("x += 1 =", x)
x -= 1
print("x -= 1 =", x)

'''
    exercises
'''

# 1. Zadeklaruj zmienne:
# v1 o wartości 126
# v2 o wartości '126'
# v3 o wartości 126.0
# v4 o wartości '126.0'

v1 = 126
v2 = '126'
v3 = 126.0
v4 = '126.0'

# 2. Zastanów się (na razie bez sprawdzania), jaki typ mają te zmienne

# 3. Poleceniami print wyświetl wartości zmiennych i ich typ. Dobrze odgadłeś(aś) typ zmiennych?

print("v1 =", v1, "and v1 is", type(v1))
print("v2 =", v2, "and v2 is", type(v2))
print("v3 =", v3, "and v3 is", type(v3))
print("v4 =", v4, "and v4 is", type(v4))

# 4. Poleceniami print wyświet:
# wynik dodawania v1 i v3 oraz typ tak wyznaczonego wyniku

sumOfV1V3 = v1 + v3
print("v1 + v3 =", sumOfV1V3, "sum v1 and v3 is", type(sumOfV1V3))

# wynik dodawania v2 i v4 oraz typ tak wyznaczonego wyniku

sumOfV2V4 = v2 + v4
print("v2 + v4 =", sumOfV2V4, "sum v2 and v4 is", type(sumOfV2V4))

# 5. Ile to jest:
# 7-1*0+3+3
# Najpierw policz w pamięci, a potem z Pythonem

print(7-1*0+3+3)

# 6. Ile to jest  4 do potęgi piątej podzielone przez 2 do potęgi 3

print(4 ** 5 / 2 ** 3)

# 7. To zadanie to raczej matematyczna łamigłówka, niż typowe zadanie z Pythona, ale z drugiej strony to
# "smaczek" bycia programistą lub matematykiem...
#
# Wyobraż sobie, że zepsuła Ci się klawiatura. Działa tylko klawisz 9, klawisze z działaniami +-*/ oraz klawisze
# nawiasów i enter. Na dodatek klawisz 9 możesz nacisnąć tylko maksymalnie 4 razy, bo po kolejnym naciśnięciu....
# komputer się restartuje.
#
# Twoim zadaniem jest napisanie na tej zepsutej klawiaturze w interpreterze Python takiego działania, aby jego wynik
# wynosił 100

print(99 + (9/9))