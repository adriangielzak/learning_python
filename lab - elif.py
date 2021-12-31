age = 18
isDrunk = True
isRestrictedArea = True

if age < 18:
    print("You are too young to buy alcohol")
else:
    if isDrunk:
        print("Are you drunk? We cannot sell you alcohol")
    else:
        if isRestrictedArea:
            print("Restricted area! Alcohol is forbiden!")
        else:
            print("OK, you can buy alcohol")

print("\n----------\n")

if age < 18:
    print("You are too young to buy alcohol")
elif isDrunk:
    print("Are you drunk? We cannot sell you alcohol")
elif isRestrictedArea:
    print("Restricted area! Alcohol is forbiden!")
else:
    print("OK, you can buy alcohol")

'''
    exercises
'''

# 1. Jak pamiętasz (mam nadzieję) sklep odzieżowy uruchamiał promocję tylko jeżeli ilość lajków była większa lub
# równa 500 a ilość udostępnień co najmniej 100. Kiedy oba warunki były spełnione sprawa była prosta - rozpoczynała
# się obniżka cen. Kiedy jednak brakowało lajków lub udostępnień, to wypadałoby dać znać czego brak.
#
# Najpierw napisz zagnieżdżone wyrażenie if / else, a potem przekształć do postaci if/elif/else. Możesz to zrobić
# "po swojemu", ale jak chcesz możesz stosować się do moich podpowiedzi. To propozycje kroków w rozwiązaniu z
# zagnieżdżonymi if/else

MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 500
num_shares = 99

# jeśli warunki są spełnione - świetnie, rozpoczynamy promocj

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print("GREAT! Today our prizes drop 10%!!!")
# w przeciwnym razie
else:
# jeśli brakuje lajków wyświetl informację o braku lakjów
    if num_likes < MIN_LIKES:
        print("We still need more likes to start the promotion")
    else:
# w przeciwnym razie (musi brakować udostępnień - to logiczne!)
        print("We still need more shares to start the promotion")
# wyświetl informację o braku udostępnień
#
# Przepisujac instrukcje do if/elif/else stosuj sie do tych zaleceń:
# jeśli warunki są spełnione, zaczynamy promocję
# w przeciwnym razie jeśli ilość lajków jest za mała - wyświetl komunikat o brakujących lajkach
# w przeciwnym razie wyświetl komunikat o brakujących udostępnieniach

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print("GREAT! Today our prizes drop 10%!!!")
elif num_likes < MIN_LIKES:
    print("We still need more likes to start the promotion")
else:
    print("We still need more shares to start the promotion")

# 2. Restauracja oferowała kupon na burgera, jeżeli zamówiłeś pizzę lub duży napój w dzień nie będący dniem weekendowym.
# Kiedy warunki promocji były spełnione, sprawa była prosta - dajemy kupon. Jednak w przypadku niespełnienia warunków
# wypadałoby poinformować, który warunek nie jest spełniony.
#
# Wskazówki do rozwiązania z zagnieżdżonym if/else
# jeżeli warunki są spełnione wydajemy kupon na burgera
# w przeciwnym razie
# jeżeli jest weekend, to wyświetlamy informację, że promocja dotyczy tylko dni poza weekendem
# w przeciwnym razie (już wiadomo, że to nie jest weekend, więc brakło na zamówieniu pizzy lub dużego napoju!)
# wyświetlamy informację o braku pizzy

isPizzaOrdered = True
isWeekend = True
isBigDrinkOrdered = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Burger for FREE!!!")
else:
    if isWeekend:
        print("Come back on non-Weekend day")
    else:
        print("You need to order Pizza or Big drink to have a Burger coupon")

# Przepisując rozwiązanie na if/elif/else stosuj się do wskazówek:
# jeśli warunki są spełnione - wydaj kupon na burgera
# w przeciwnym razie jeśli jest to weekend, wyświetl komunikat o tym, że promocja obowiązuje wyłącznie w poza weekendem
# w przeciwnym razie wyświetl komunikat o tym, że należy zamówić pizze lub duży napój

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Burger for FREE!!!")
elif isWeekend:
    print("Come back on non-Weekend day")
else:
    print("Come back on non-Weekend day")

# Pamiętaj, że stosowanie if/elif/else jest znacznie lepsze jeśli chodzi o styl programowania!