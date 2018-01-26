import random, time
cooks = input("Введите ингридиенты блюда (Обязательно через пробел)")
cooks_list = cooks.split(" ")
for products in cooks_list:
	cooking_method = ["пожарили","сварили","согрели","разогрели","перемешали","сьели","кинули коту"]
	cooking_method_element = random.choice(cooking_method)
	print("Вы",cooking_method_element,products)
	time.sleep(1)
i = 0
cooks_name_list = []
for element_name in cooks_list:
	cooks_name_list.append(cooks_list[i][0])
	i += 1
cooks_name = "".join(cooks_name_list)
print("ы приготовили блюдо:",cooks_name)