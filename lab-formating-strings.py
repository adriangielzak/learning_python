message1 = 'Proccessing file %s'
print(message1 % ('file_1.txt'))

message2 = 'File %s has size %d KB'
print(message2 % ('file_2.txt', 100))
# błąd! niepoprawna kolejność typów zmiennych -->    print(message2 % (100, 'file_2.txt'))

message3 = 'File %20s has size %10d KB'
print(message3 % ('file_3.txt', 300))

message4 = 'Proccessing file {0:s}'
print(message4.format('file_4.txt'))

message5 = 'File {0:s} has size {1:d}'
print(message5.format('file_5.txt', 500))
message5 = 'File {1:s} has size {0:d}'
print(message5.format(500, 'file_5.txt'))

message6 = 'File {0:20s} has size {1:10d}'
print(message6.format('file_6.txt', 600))

'''
    exercises
'''

# 1. Zadeklaruj zmienną helloMessage i wpisz do niej tekst:
#
# "Hello %s!"

helloMessage = "Hello %s!"

# 2. Korzystając z tej zmiennej oraz z operatora % wyświetl dwa powitania: raz %s należy zamienić na Kate a raz na Chirs

print(helloMessage % ("Kate"))
print(helloMessage % ("Chris"))

# 3. Zmień zawartość zmiennej helloMessage na
#
# "Hello {0:s}!"

helloMessage = "Hello {0:s}"

# 4. Podobnie , jak w punkcie drugim wyświetl powitanie z Kate i Chis, ale tym razem skorzystaj z metody format

print(helloMessage.format("Kate"))
print(helloMessage.format("Chris"))

# 5. Zmień zawartość zmiennej helloMessage na
#
# "%s has %d %s"

helloMessage = "%s has %d %s"

# 6. Korzystając z tej zmiennej oraz z operatora % wyświetl dwa komunikaty.
#
# w pierwszym komunikacie %s zamień na Kate, %d na 1, a %s na animal
#
# w drugim komunikacie %s zamień na  Chris, %d na 100000, a %s na $

print(helloMessage % ("Kate", 1, "animal"))
print(helloMessage % ("Chris", 100000, "$"))

# 7. Zmień zawartość zmiennej helloMessage na
#
# "{0:s} has {1:d} {2:s}"

helloMessage = "{0:s} has {1:d} {2:s}"

# 8. Wyświetl te same komunikaty, jak w punkcie 6, ale tym razem skorzystaj z metody format

print(helloMessage.format("Kate", 1, "animal"))
print(helloMessage.format("Chris", 100000, "$"))

# 9. [Trochę trudniejsze, ale cała trudność polega na samodzielnym zbudowaniu napisu formatującego i to w takiej postaci,
# że na każdy element w napisie ma zostać przewidziana określona liczba znaków]
# Utwórz zmienną line i wpisz do niej tekst pozwalający na wyświetlenie na 20 znakach pewnego napisu, następnie słowa
# "costs", następnie na 6 znakach pewnej liczby i następnie znaku €, np:
#
# ICE CREAM            costs      3 €
# TRIP TO VENICE       costs    119 €
# PIZZA HAWAII         costs      6 €
# ... BTW, wiesz jak uzyskać znak € z klawiatury? O ile używasz Windows powinien zadziałać prawy ALT + u

line = "{0:20s} costs {1:6d} €"

print(line.format("ICE CREAM", 3))
print(line.format("TRIP TO VENICE", 119))
print(line.format("PIZZA HAVAII", 6))

# Rozwiązanie z chr()
euro = chr(8364)
lineChrEuro = "{0:20s} costs {1:6d} " + euro

print(lineChrEuro.format("ICE CREAM", 3))
print(line.format("TRIP TO VENICE", 119))
print(line.format("PIZZA HAVAII", 6))

# 10. Korzystając ze zmiennej line i polecenia print,  zamieniaj odpowiednie znaczniki na podane niżej wartości,
# tak aby w efekcie został wyświetlony cennik usług:
#
# ICE CREAM    3
# TRIP TO VENICE  119
# PIZZA HAWAI  6

line = "{0:s} {1:5d}"

print(line.format("ICE CREAM", 3))
print(line.format("TRIP TO VENICE", 119))
print(line.format("PIZZA HAVAII", 6))