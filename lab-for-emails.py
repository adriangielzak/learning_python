persons = ["Elizabeth", "Steven", "Sebastian", "Margaret", "Svetlana", "Raphael"]
emails = []
domain = "mycompany.com"

for person in persons :
    email = person.lower() + "@" + domain
    emails.append(email)
    print("Email for\t", person, "\tis\t", email)
else :
    print("-- end of the list --")

print(emails)

'''
    exercises
'''

# ZADANIE 1
# Dana jest lista:
# data = ['Error:File cannot be open',
#         'Error:No free space on disk',
#         'Error:File missing',
#         'Warning:Internet connection lost',
#         'Error:Access denied']
# Napisz pętlę for, która wyświetli elementy tej listy jeden po drugim. Podczas wyświetlania elementów konwertuj
# napisy do wielkich liter.

data = ['Error:File cannot be open', 'Error:No free space on disk', 'Error:File missing', 'Warning:Internet connection lost',
        'Error:Access denied']
print(data)

for errorMessage in data :
    print(errorMessage.upper())

# ZADANIE 2
# Jak widzisz, każdy z elementów listy zawiera znak ":".
# W pętli for każdy z przetwarzanych napisów rozbij ze względu na ":" korzystając z funkcji split.
# Wynik zapamiętaj w nowej dwuelementowej liście elements.
# Następnie wyświetl elements[0] konwertując napis do wielkich liter, a elements[1] wyświetl bez żadnej konwersji

print(data[1].split(":"))
elements = []

for errorMessage in data :
    message = errorMessage.split(":")
    print(message[0].upper())
    print(message[1])
    elements.append(message[0].upper() + " " + message[1])

print(elements)
# ZADANIE 3
# Rozpocznij od poprzednio utworzonej pętli. Zmieniamy zasady wyświetlania:
# Jeżeli w elements[0] znajduje się napis "Error", wyświetl elements[1] konwertując tekst do wielkich liter
# w przeciwnym razie wyświetl elements[1] bez żadnej konwersji

for errorMessage in data :
    message = errorMessage.split(":")
    print(message[0].upper())
    if message[0] == "Error" :
        print(message[1].upper())
    else :
        print(message[1])