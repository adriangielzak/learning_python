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