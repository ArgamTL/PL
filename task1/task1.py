#############
# Задание 1 #
############# 
n = input("ENTER  n ")
m = input("ENTER  m ")
print("\nANSWER:")
#n = 5
#m = 4

i = 1
while True:
    print(i, end='')
    i = 1 + (i + int(m) - 2) % int(n)
    if i == 1:
        break

###########################################


#############
# Задание 1 v2 #
############# 
d = input("Введите n И m, ПРИМЕР: 43 ")
print("\nОТВЕТ:")
#n = 5
#m = 4

i = 1
while True:
    print(i, end='')
    i = 1 + (i + int(d[1]) - 2) % int(d[0])
    if i == 1:
        break

###########################################
