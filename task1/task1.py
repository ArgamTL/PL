#############
n = input("вводите n ")
m = input("вводите m ")

#n = 5
#m = 4

i = 1
while True:
print(i, end='')
i = 1 + (i + int(m) - 2) % int(n)
if i == 1:
break
