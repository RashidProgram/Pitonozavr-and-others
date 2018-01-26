import Error as err
from time import sleep
def sydjet():
	print("Вы проснулись у себя дома.")
	sleep(2)
	print("Первым делом посмотрели в окно и увидели нечто!")
	sleep(2)
	print("В ваш дом пытаются зайти зомби, проламывая двери")
	sleep(2)
	print("Вы быстро хватаете имеющийся у вас травматический пистолет")
	sleep(3)
	print("И стреляя в зомби прорываетесь наружу")
	sleep(2.3)
	print("Вы выбрались наружу но вас окружили зомби")
	while True:	
		try:
			answer = int(input('1 - стрелять, 2 - бить кулаками, 3 - ничего не делать'))
			if answer < 1 or answer > 3:
				raise err.NumberError('Напишите чило 1, 2 или 3!')
		except err.NumberError as e:
			print(e)
		except ValueError:
			print('Введите число!!!')
		else:
			break
		finally:
			sleep(2)
	if answer == 1:
		print("Вы убили несколько зомби, но вам это не помогло кто му же у вас закончились патроны")
		sleep(3.5)
	elif answer == 2:
		print("Вы ударили несколько зомби но на большее ничего")
		sleep(2)
	elif answer == 3:
		print("Вы ничего не делали а они приближались")
		sleep(2)
	print("Вы думали что вам уже конец как сзади кто-то растрелял этих зомби")
	sleep(2)
	print('О! Выживший идем за мной я отведу тебя в убежище')
	while True:	
		try:
			answer = int(input("1 - пойти 2 - убежать"))
			if answer < 1 or answer > 2:
				raise err.NumberError('Напишите чило 1 или 2!')
		except err.NumberError as e:
			print(e)
		except ValueError:
			print('Введите число!!!')
		else:
			break
		finally:
			sleep(1)

	if answer == 1:
		print("вы куда-то направились")
	elif answer == 2: 
		print("Вы хотели убежать но увидев приближающихся зомби передумали")
	sleep(2)
	print('Вы с ним разговаривали а зомби оставались позади')
	sleep(2)
	print("Я - военный. Мы с ребятами начали сопротивляться зомби но многие погибли")
	sleep(3)
	print("А те кто жи разбросались по всей планете и обороняются")
	sleep(2)
	print('Я взял много оружия из военного склада и нашел подземелье')
	sleep(2)
	print('В этом подземельи безопасно, зомби не знают о нём')
	sleep(2)
	print('-Кстати у тебя есть деньги')
	while True:	
		try:
			answer = int(input("1 - соврать 2 - сказать правду(У вас нет денег)"))
			if answer < 1 or answer > 2:
				raise err.NumberError('Напишите чило 1 или 2!')
		except err.NumberError as e:
			print(e)
		except ValueError:
			print('Введите число!!!')
		else:
			break
		finally:
			sleep(1)
	if answer == 1:
		print("Есть. Ну тогда хорошо я думал может дать.")
		sleep(1)
		print("Вы признались что денег нет")
		sleep(0.9)
	elif answer == 2:
		pass
	print('Вот возьми на первое время, вот еще 3 аптечки  на всякий случай. PS вам дали 100 биткоинов и 3 аптечки')
	sleep(3.4)
	print("А вот и подземелье")


