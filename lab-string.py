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