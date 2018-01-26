group = input("Введите состав подразделения, солдат")
print(group)
group_list = group.split(", ")#split() - разделение на список
print(group_list)
final_group = " <3 ".join(group_list)
print(final_group)
number = [3, 5, 11, 30]
print(len(number))
print(max(number))
print(min(number))
number.sort()
print(number)

guess = int(input("Отгадой число, мальчонка: "))
#print(number in guess)

if guess in number:
	print("А ю лаки мен?!")
else:
	print("Ю лох")
print(range(0, 19))
print(guess in range(0, 19))
i = 1
acteres = ["Скарлет Йоханнсеннн","Галя Гадот","Маргарита"]
for person in acteres:
	if i == 2:
		print("Не так себе " + person)
		i+= 1
		continue
	print("так себе " + person)
	i+= 1