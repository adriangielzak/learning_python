s = "A Python script"

print(s[0])
print(s[2])
print(s[2:7])
print(s[2:8])
print(s[:8])
print(s[8:])
print(s[2:999])
print(s[222:999])

message = 'Document "cv.doc" was printed on printer: XEROX'
print(message.find(':'))
print(message[message.find(':') + 2:])

print(message[message.find('"') + 1:])

tmp = message[message.find('"') + 1:]

print(tmp[:tmp.find('"')])

'''
    exercises
'''

# 1.  Anagram to słowa, które składają sie z tych samych liter, ale mające różne znaczenia
# np. "arbuz" >> "burza", "alergia" >> "galeria". Tu pobawimy się trochę anagramami.
#
# 2. Tutaj każdą literkę wyodrębnisz i wykorzystasz oddzielnie. Do zmiennej q zapisz tekst "THE EYES".
# Wyświetl napis zbudowany z liter zmiennej q w kolejności: 0,1,2,5,3,7,4,6. Wyświetlając literki skorzystaj z print
# lub dodaj do siebie literki budując napis.

q = 'THE EYES'
print(q[0], q[1], q[2], q[5], q[3], q[7], q[4], q[6])
qa = q[0] + q[1] + q[2] + q[5] + q[3] + q[7] + q[4] + q[6]
print(qa)

# 3. Tutaj użyjesz notacji, która pozwoli wyodrębnić fragment napisu rozpoczynając od określonej pozycji do końca.
# Do zmiennej q zapisz  "a gentleman" a potem wyświetl litery w kolejności 3,6,7,2,0,4,5,1,8 - do końca

q = "a gentleman"
print(q[3] + q[6] + q[7] + q[2] + q[0] + q[4] + q[5] + q[1] + q[8:])

# 4. Wiesz jak z napisu  "THE MORSE CODE" zrobić tekst "HERE COME DOTS"? Gdzie się da korzystaj z notacji "od-do"

q = "THE MORSE CODE"
print(q[1:3] + q[6] + q[8:12] + q[4] + q[8:10] + q[12] + q[11] + q[0] +q[7])

# 5. Zostajesz zatrudniony w firmie, która wykonuje analizę oglądalności poszczególnych programów TV.
# Na bardzo początkowym etapie, Twój program musi przeczytać dane z pliku tekstowego z zapisanym harmonogramem
# poszczególnych programów. Plik zawiera linie zbudowane tak, że tytuł programu znajduje się w cudzysłowie,
# a kończy się napisem o:, po którym następuje godzina, np tak:
#
# 'Program "Kropka nad i" nadamy o: 22:00'
#
# Musisz wyodrębnić tytuł programu i godzinę o której zostanie nadany. W tym celu:
#
# Do zmiennej line wpisz tekst "'Program "Kropka nad i" nadamy o: 22:00'"

line = 'Program "Kropka nad i" nadamy o: 22:00'

# Do zmiennej time wyodrębnij samą tylko godzinę (musisz poszukać znaku dwukropek i pobrać wszystkie dalsze znaki)

time = line[line.find(':') + 2 :]

# Wyświetl napis time

print(time)

# Do zmiennej tmp wyodrębnij fragment tekstu ze zmiennej line rozpoczynający się za znakiem cudzysłów do końca

tmp = line[line.find('"') + 1 :]

# Do zmiennej title wyodrębnij z tmp fragment tekstu od początku do znaku cudzysłów

title = tmp[:tmp.find('"')]

# Wyświetl title i time
print(title, time)

# To samo wykonaj dla linii

# 'Program "Pytanie na śniadanie" nadamy o: 6:00'

line = 'Program "Pytanie na śniadanie" nadamy o: 6:00'

time = line[line.find(':') + 2 :]

tmp = line[line.find('"') + 1 :]
title = tmp[:tmp.find('"')]

print(title, time)