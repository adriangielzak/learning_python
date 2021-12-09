'''
    Part 1
'''

from __future__ import print_function
import fixpath
from colorama import init, Fore, Back, Style

init()

atext = 'This is a text.'
print(atext.endswith('ext'))
print(atext.endswith('ext.'))
print(atext.islower())
print(atext.upper())
print(atext.upper().isupper())
print(atext.find('is'))
print(atext.find('is', 3))
print(atext.replace('a', '@'))
print(atext.replace('s', '$'))
print(atext.replace('a', '@').replace('i', '1').replace('e', '3'))
print(atext.split(' '))

somethingLikeANumber = '1000'
print(somethingLikeANumber.isdigit())
print(somethingLikeANumber.isdecimal())
print(somethingLikeANumber.isalpha())
print(somethingLikeANumber.isalnum())

'''
    exercises
'''

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'
#1. Wyświetl tekst napisany tylko wielkimi literami
print(quote.upper())

#2. Wyświetl tekst tylko małymi literami
print(quote.lower())

#3. Sprawdź, czy tekst kończy się słowem 'street'
print(quote.endswith('street'))

#4. Sprawdz, czy tekst jest zapisany wielimi literami
print(quote.isupper())

#5. Sprawdź, czy tekst skonwertowany do wielkich liter jest zapisany welimi literami (astosuj złożenie funkcji)
print(quote.upper().isupper())

#6. Poszukaj, na której pozycji (licząc od zera) znajduje się w tekście słowo (podnapis) 'one'
print(quote.find('one'))

#7. Zmień w tekście słowo (podnapis) 'one' na '1'
print(quote.replace('one', '1'))

#8. Zmień w tekście słowo (podnapis) 'one' na '1', a słowo 'both' na '2'
print(quote.replace('one', '1').replace('both', '2'))

    #Dodatkowo zabawa ze zmianą kolorów w tekście i dodany import na górze

    #       from __future__ import print_function
    #       import fixpath
    #       from colorama import init, Fore, Back, Style

    #       init()
print(quote.replace('one', Fore.GREEN + '1' + Fore.RESET).replace('both', Back.GREEN + '2' + Back.RESET))

#9. Rozdziel napis na mniejsze napisy ze zględu na znak rozdzielający, jak jest spacja
print(quote.split(' '))

#10. Sprawdź, czy napis jest liczbą, liczbą dziesiętną, napisem bez cyfr, napisem z literami i cyframi
print(quote.isdigit()) #czy napis jest liczbą
print(quote.isdecimal()) #czy napis jest liczbą dziesiętną
print(quote.isalpha()) #czy napis jest napisem bez cyfr
print(quote.isalnum()) #czy napis jest napisem zliterami i cyframi

    # W ostatnim zadaniu otrzymujesz 4 wartości false.
    # Zwłaszcza 2 ostatnie wyniki mogą Cię dziwić.
    # Nasz napis zawierał spacje, składał się z wielu wyrazów i dlatego nie jest alfa-stringiem ani alfanumerykiem

'''
    Part 2
'''

drive = 'c:\\'
folder = 'scripts\\python\\'
file = 'myFirstScript.py'
path = drive + folder + file
print(path)

justText = 'text with\nnew line'
print(justText)

rawText = r'text with\nnew line' # r after text
print(rawText)

quotesTextOne = "Mc Donald's"
print(quotesTextOne)
quotesTextTwo = 'Mc Donald\'s'
print(quotesTextTwo)
quotesTextThree = 'He said "I like Python!"'
print(quotesTextThree)
quotesTextFour = "He said \"I like Python!\""
print(quotesTextFour)

'''
    exercises
'''

#1. Pracujesz w Urzędzie Stanu Cywilnego i ... korzystasz z Pythona. Dziewczyna o imieniu Kasia i nazwisku Sowa
# wychodzi za mąż za chłopaka o nazwisku Mrugała. Pani Kasia chce zachować oba nazwiska. Zdefiniuj zmienne firstName,
# famillyName i lastName i przypisz do nich napisy odpowiadające imieniu, nazwisku panieńskim i nowym nazwisku.
# Następnie utwórz zmienną newName i zapisz w niej wynik konkatenacji (czyli złączenia napisów) dla firstname, spacji,
# familyName, spacji i lastName. Wyświetl to nowe nazwisko
firstName = 'Katarzyna'
familyName = 'Sowa'
lastName = 'Mrugała'
newName = firstName + ' ' + familyName + ' ' + lastName
print(newName)

#2. Zdefiniuj zmienną music o następującej zawartości (są to tytuły i autorzy piosenek z filmu Minionki):
#   "Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I'm a Man" Steve Winwood
music = '\"Universal Fanfare\" Jerry Goldsmith \"Happy Together\" Garry Bonner \"I\'m a Man\" Steve Winwood'
print(music)

#3. W powyższym tekście mowa jest o 3 piosenkach. Zmień tekst tak, aby druga i trzecia piosenka podczas wyswietlania były umieszczone w nowej linii.
musicInNewLine = '\"Universal Fanfare\" Jerry Goldsmith \n\"Happy Together\" Garry Bonner \n\"I\'m a Man\" Steve Winwood'
print(musicInNewLine)

#4.
print('(\\(\\')
print('( -.-)')
print('O_(")(")')

'''
    Part 3
'''

somethingLikeANumberTwo = '1000'
print(somethingLikeANumberTwo)
# print(somethingLikeANumberTwo + 1) # nie można dodać int do stringa
addIntFromStringAndInt = int(somethingLikeANumberTwo) + 1
print('int(string) + int =', addIntFromStringAndInt)

addStringAndStringFromInt = somethingLikeANumberTwo + str(1)
print('string + str(int) = ', addStringAndStringFromInt)

typeOfSomethingLikeNumberTwo = type(somethingLikeANumberTwo)
print(typeOfSomethingLikeNumberTwo)

typeOfSomethingLikeNumberTwo = type(int(somethingLikeANumberTwo))
print(typeOfSomethingLikeNumberTwo)

'''
    exercises
'''

#1. Wejdź na stronę Wikipedii poświęconej Monty Pytonowi
#   https://en.wikipedia.org/wiki/Monty_Python
#   Skopiuj fragment z paragrafu zatytuowanego "Monty Python".
#   W skrypcie utwórz zmienną article i przypisz jej wartość skopiowanego tesktu.

article = '''Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupe who created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and influence, including touring stage shows, films, albums, books and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Regarded as an enduring icon of 1970s pop culture, their sketch show has been referred to as being "an important moment in the evolution of television comedy".[7]
Broadcast by the BBC between 1969 and 1974, Monty Python's Flying Circus was conceived, written and performed by its members Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. Loosely structured as a sketch show, but with an innovative stream-of-consciousness approach aided by Gilliam's animation, it pushed the boundaries of what was acceptable in style and content.[8][9] A self-contained comedy team responsible for both writing and performing their work, the Pythons had creative control which allowed them to experiment with form and content, discarding rules of television comedy. Following their television work, they began making films, including Monty Python and the Holy Grail (1975), Life of Brian (1979) and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while in North America, it has coloured the work of cult performers from the early editions of Saturday Night Live through to more recent absurdist trends in television comedy. "Pythonesque" has entered the English lexicon as a result.
At the 41st British Academy Film Awards in 1988, Monty Python received the BAFTA Award for Outstanding British Contribution To Cinema. In 1998, they were awarded the AFI Star Award by the American Film Institute. Many sketches from their TV show and films are well-known and widely quoted. Both Holy Grail and Life of Brian are frequently ranked in lists of greatest comedy films. In a 2005 poll of over 300 comics, comedy writers, producers and directors throughout the English-speaking world to find "The Comedian's Comedian", three of the six Pythons members were voted to be among the top 50 greatest comedians ever: Cleese at No. 2, Idle at No. 21, and Palin at No. 30.[10][11]'''

#2. Skonwertuj tekst do dużych liter i wyświetl go. Zrób to w jednej instrukcji.
print(article.upper())

#3. Wyświetl tekst zamieniając 'monty' na 'flying'. Ponieważ python rozpoznaje małe i duże litery przed zamianą skonwertuj go na małe litery. Ponownie postaraj się to zrobić w jednym poleceniu.
print(article.lower().replace('monty', 'flying'))

#4. Rozbij tekst na słowa ze względu na spacje i wyświetl tą listę.
print(article.split(' '))

#5. Wyświetl tekst w postaci:
#        word python appears 3 times
#   oczywiście liczba (tutaj 3) powinna być wyliczona, jako ilość wystąpień tekstu python w zmiennej article
print('word python appears', article.lower().split().count('python'), 'times')

#6. Poleceniem print wyświetl tekst:
#   to print the \ you need to put \ twice in your text like this: \\
print('to print the \\ you need to put \\ twice in your text like this: \\\\')

#7. Poleceniem print wyświetl tekst

#   The best hits of '80s!!!

#   Zrób to na 2 sposoby:
#   -raz tekst powinien być zamknięty w pojedynczym apostrofie '
#   -a drugi raz tekst powinien być zamknięty w cudzysłowiu "
print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")

#8. Teraz zrobisz "mini kalkulator" do kantoru wymiany walut. Chcemy wyświetlić tabelkę w postaci:

#   cur   exchange amount
#   USD   3.65     64.10958904109589
#   EUR   4.23     55.31914893617021
#   w tym celu:

#   -najpierw zadeklaruj zmienną amountPLN i wpisz do niej wartość 234
#   -następnie wyświetl teksty rozdzielając wartości tabulatorem, tak aby to co zostanie wypisane na ekranie przypominało tabelkę (skorzystaj do tego z kilku poleceń print, jednolinijkowy print byłby zbyt trudny do zrozumienia)
#   -wartości w kolumnie amount wylicz dzieląc amountPLN przez aktualny kurs USD i EUR (w tym przykładzie są to 3.65 i 4.23)
amountPLN = 234
print('cur', '\texchange', 'amount')
print('USD', '\t', 3.65, '\t', amountPLN/3.65)
print('EUR', '\t', 4.23, '\t', amountPLN/4.23)

#9. Zadeklaruj zmienną ValueAsText i wpisz do niej wartość '123.45'
valueAsText = '123.45'

#10. Zadeklaruj zmienną factor o wartości 1.23
factor = 1.23

#11. Wyświetl tekst:
#   value is 123.45 factor is 1.23 value*factor= 151.8435
#   podczas obliczania value * factor skonwertuj zmienną ValueAsText na typ float
print('value is', valueAsText, 'factor is', factor, 'value*factor =', float(valueAsText)*factor)