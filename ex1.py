pets = dict()

print("Кличка питомца:", end = '')
a=input()
print("Вид питомца:", end = '')
b=input()
print("Возраст питомца:", end = '')
c=int(input())
print("Имя владельца:", end = '')
d=input()
pets[a] = {'Вид':b, 'Возраст':c, 'Имя владельца':d}

if (c > 10 and c < 20) or (c % 10 == 0) or (c % 10 in (5, 6, 7, 8, 9)):
    agewrd = "лет"
elif (c % 10 == 1):
    agewrd = "год"
else:
    agewrd = "года"

for i in pets.keys():
    name = i
    break

print(f"Это {pets[name]['Вид']} по кличке \"{name}\". Возраст питомца: {pets[name]['Возраст']} {agewrd}. Имя владельца: {pets[name]['Имя владельца']}")