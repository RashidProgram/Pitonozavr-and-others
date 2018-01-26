print("Мы проверим ваше знание Таблицы умножения")
import random, time
score = 0
while True:
    num_1 = random.randint(0,10)
    num_2 = random.randint(0,10)
    summa = num_1 * num_2
    userAnswer = input("Сколько будет "+ str(num_1) + " * " + str(num_2)+" Если хотите выйти введите exit ")
    if userAnswer == "exit":
        break;
    if userAnswer == str(summa):
        time.sleep(1)
        score += 1
        print("Верно. У вас ",score,"очков")
    else:
        time.sleep(1)
        print("Не верно правильный ответ",summa," у вас ",score,"очков")
print("Вы всего заработали",score,"очков")