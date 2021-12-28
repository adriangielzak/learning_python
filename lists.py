countries = ['FR', 'US', 'DE', 'RU']

print(countries)
print(countries[1])

countries[1] = 'GB'
print(countries)
print(countries[1])

countries.append('PL')
print(countries)

countries.insert(2, 'ES')
print(countries)

countries.remove('RU')
print(countries)

countries.sort()
print(countries)

countries.reverse()
print(countries)

print(countries.pop(2))
print(countries)

print(countries.index('DE')) # na którym miejscu znajduję się dany element

print(countries.count('PL')) # ile razy znajduje się dany element na liście

newList = ['FI', 'SE']

print(newList)

countries.extend(newList)
print(countries)

countriesCopy = countries
print(countries)
print(countriesCopy)

countriesCopy.clear()
print(countries)  # ups
print(countriesCopy)

countries = ['FR', 'US', 'DE', 'RU']
countriesCopy = countries.copy()  # kopiowanie listy!

countriesCopy.clear()
print(countries)
print(countriesCopy)

'''
    exercises
'''

# Jaka jest najlepsza lista? Oczywiście lista przebojów Trójki ;).
# W tych zadaniach zajmiemy się przebojami publikowanymi na http://lp3.polskieradio.pl/topnotowanie/
#
# 1. Utwórz listę hitsTitles zawierającą tytuły: 'BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN',
# 'RIDERS ON THE STORM','WISH YOU WERE HERE'

hitsTitles = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HEAVEN', 'RIDERS ON THE STORM', 'WISH YOU WERE HERE']
print(hitsTitles)

# 2. Dodaj do listy kolejne dwie piosenki: 'CHILD IN TIME' i 'AGAIN'

hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
print(hitsTitles)

# 3. Wygląda na to, że w systemie głosowania była luka. Na pozycji 3 powinna się znaleźć piosenka 'HOTEL CALIFORNIA'

hitsTitles.insert(2, 'HOTEL CALIFORNIA')
print(hitsTitles)

# 4. Ops... wygląda na to, że system był bardziej zepsuty... oczywiście to wina IT. Piosenka
# 'THE SOUND OF SILENCE' powinna znaleźć się na pierwszym miejscu

hitsTitles.insert(0, 'THE SOUND OF SILENCE')
print(hitsTitles)

# 5. To na jakiej pozycji jest teraz 'HOTEL CALIFORNIA'? Odnajdź numer indeksu dla tej piosenki

print(hitsTitles.index('HOTEL CALIFORNIA'))

# 6. A jednak 'HOTEL CALIFORNIA' powinien zostać usunięty z listy

hitsTitles.remove('HOTEL CALIFORNIA')
print(hitsTitles)

# 7. No i na pierwszym miejscu tytuł "THE SOUND OF SILENCE" powinien zostać zamieniony na "ENJOY THE SILENCE"

hitsTitles[0]= 'ENJOY THE SILENCE'
print(hitsTitles)

# 8. Utwórz kopię listy, która będzie służyła do odczytania przebojów na antenie. Nowa lista ma nazywać się hitsToRead

hitsToRead = hitsTitles.copy()
print(hitsToRead)

# 9. Lista do odczytania ma zawierać elementy w odwrotnej kolejności. Odwróć kolejność elementów na liście hitsToRead.

hitsToRead.reverse()
print(hitsToRead)

# 10. A jednak dzisiaj lista przebojów będzie  wyjątkowo prezentowana w kolejności alfabetycznej.
# Posortuj hitsToRead w kolejności alfabetycznej

hitsToRead.sort()
print(hitsToRead)

# 11. Prowadzący listę przebojów po odczytaniu tytułu usuwa z listy hitsToRead odczytany element.
# Dlatego korzysta z metody pop :). Zasymuluj odczyt dwóch pierwszych pozycji

hitsToRead.pop(0)
hitsToRead.pop(0)
print(hitsToRead)

# 12. W czasie audycji słuchacze domagali się aby zagrać dodatkowo 'NOTHING COMPARES 2 U' i 'WISH YOU WERE HERE'.
# Utwórz listę additionalSongs zawierającą te dwa tytuły.

additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
print(additionalSongs)

# 13. Dodaj do listy hitsToRead elementy z listy additionalSongs

hitsToRead.extend(additionalSongs)
print(hitsToRead)

# 14. Ile razy będzie zagrane 'WISH YOU WERE HERE' a ile razy 'RIDERS ON THE STORM'. Wyświetl ile razy te piosenki
# występują na liście hitsToRead.

print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))

# 15. Audycja się kończy. Wyczyść listę hitsToRead

hitsToRead.clear()
print(hitsToRead)

# Chcesz jeszcze więcej poćwiczyć z listami? Zrób listę upragnionych prezentów na urodziny, listę krajów jakie
# chcesz odwiedzać w wakacje, listę ulubionych knajpek w okolicy itp. Staraj się korzystać z tych samych instrukcji,
# co pokazywane na lekcji i ćwiczone w tym zadaniu