def lenNumber():
	i = 0
	for q in number_list:
		i += 1
	if i == 1:
		print("Всего",i,"числj")
	elif i <= 4:
		print("Всего",i,"числа")
	else:
		print("Всего",i,"чисел")	
def strInInt():
	for x in strNumber_list:
		x = int(x)
		number_list.append(x)
def maxNumber(number):
	for dopNumber in number_list :
		if dopNumber > number:
			number = dopNumber
	print("Большее из чисел:",number)
def minNumber(number):
	for dopNumber in number_list :
		if dopNumber < number:
			number = dopNumber
	print("Меньшее из чисел:",number)
strNumber = input("Введите несколько чисел и программа выведет большее \n \
 Примечание: все числа дожны отделятся одним пробелом ").strip()
strNumber_list = strNumber.split(" ") 
number_list = []
strInInt()
print(number_list)
maxNumber(number_list[0])
minNumber(number_list[0])
lenNumber()
