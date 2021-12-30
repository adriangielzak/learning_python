tax = (4, 7, 8, 23)

print(tax)
print(tax[1])
print(tax[-1]) # wyświetla ostatni element tuple
print(tax.index(7)) # na której pozycji znajduje się 7
print(tax.count(8)) # ile razy w tuple występuje 8
print(max(tax)) # zwraca maksymalną wartość tuple

taxDwa = ("zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć")
print(taxDwa)

#tax.revert() - nie ma takiej funkcji. Nie można zmieniać tuple. Tuple jest stały.
taxList = list(tax)
taxList.append(30)
newTax = tuple(taxList)

print(tax)
print(taxList)
print(newTax)

(tax1, tax2, tax3, tax4) = tax
print("tax1 =", tax1, "tax2 =", tax2, "tax3 =", tax3, "tax4 =", tax4)

a = 1
b = 10
print("a =", a, "\tb =", b)

# temp = a
# a = b
# b = temp
# print("a =", a, "\tb =", b)

# Tak wygodniej...
(a, b) = (b, a)
print("a =", a, "\tb =", b)

'''
    exercises
'''

# Przygotowujesz się do analizy email-marketingu. Po każdym zadaniu poniżej wyświetl listę:
#
# 1. Utwórz listę o nazwie marketing z elementami:
# -loyality program
# -client promotion
# -market research

marketing = ["loyality program", "client promotion", "market research"]
print(marketing)

# 2. Dodaj do listy element 'public relations'

marketing.append("public relations")
print(marketing)

# 3. Wyświetl pozycję numer 3

print(marketing[3])

# 4. Wstaw na pozycję numer 2 element 'investor relations'

marketing.insert(2, "investor relations")
print(marketing)

# 5. Chcesz jednak aby lista znajdowała się w zmiennej o nazwie emailMarketing. Skopiuj elementy z listy marketing
# do listy emailMarketing

emailMarketing = marketing.copy()
print(emailMarketing)

# 6. Posortuj listę emailMarketing

emailMarketing.sort()
print(emailMarketing)

# 7. Utwórz nową jednoelementową listę internalEmails. Jedyny element to 'internal communication'

internalEmails = ["internal communication"]
print(internalEmails)

# 8. Dodaj listę internalEmails do listy emailMarketing

emailMarketing.extend(internalEmails)
print(emailMarketing)

# 9. Utwórz tuple, którego wartości pochodzą z listy emailMarketing. Podczas wyświetlania tuple zwróć uwagę na nawiasy,
# z jakich skorzystał Python

tupleFromEmailMarketing = tuple(emailMarketing)
print(tupleFromEmailMarketing)