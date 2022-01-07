for number in range(20) :
    print(number)

for number in range(1, 21) :
    print(number)

for number in range(0, 20, 2) :
    print(number)

for number in range(1, 21) :
    if number %2 == 0 :
        print("Number %2d is %s" % (number, "even"))
    else :
        print("Number %2d is %s" % (number, "odd"))

'''
    exercises
'''

# Dane są następujące napisy:
#
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'
# Korzystając z polecenia FOR wyświetl:
#
# +---+---+---+---+
# +---+---+---+---+
# +---+---+---+---+
# +---+---+---+---+
# +---+---+---+---+
# +---+---+---+---+
# +---+---+---+---+
# +---+---+---+---+
# +---+---+---+---+
# +---+---+---+---+

for number in range(10) :
    print(string_A)

# Korzystając z polecenia FOR wyświetl:
#
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
print("\n\n\n\n\n")

for number in range(9) :
    if number %2 == 0 :
        print(string_A)
    else :
        print(string_B)

# Korzystając z polecenia FOR wyświetl:
#
# x
# xx
# xxx
# xxxx
# xxxxx
# xxxxxx
# xxxxxxx
# xxxxxxxx
# xxxxxxxxx
# (wskazówka: aby wyświetli 5 liter x użyj "x" *5

for number in range(1, 10) :
    print("x" * number)

# Korzystając z polecenia FOR wyświetl:
#
# o
# xx
# ooo
# xxxx
# ooooo
# xxxxxx
# ooooooo
# xxxxxxxx
# ooooooooo

string_o = "o"
string_x = "x"

for number in range(1, 10) :
    if number %2 != 0 :
        print(string_o * number)
    else :
        print(string_x * number)