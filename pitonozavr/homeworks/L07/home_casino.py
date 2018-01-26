import random, time, math
def color():
    while True:
        person["ставка"] = math.fabs(int(input(person["имя"] + " делайте свою ставку.(У вас 5000) ")))
        if person["ставка"] == 0:
            print("Ставка должна быть больше нуля")
            continue
        break
    if person["ставка"] > person["кеш"]:
        person["ставка"] = person["кеш"]
        print("Так как ставка больше кеша ставка - все деньги")
    while True:
        redOrBlack = input("Ставка сделанна. Выберете цвет ").lower().strip()
        if redOrBlack != "красный" and redOrBlack != "черный":
            print("Вы можете выбрать только красный или черный")
            time.sleep(1)
            continue
        time.sleep(1)
        break
    chanse = random.randint(0,36)
    if redOrBlack == "красный":
        if chanse in range(19,36):
            person["кеш"] += person["ставка"]
            print("Победа, Ставка удваивается теперь у вас",person["кеш"])
        elif chanse in range(1,18):
            person["кеш"] -= person["ставка"]
            print("К сожалению выпал черный цвет, а значит вы проиграли ставку. Ваш кеш", person["кеш"])
        else:
            person["кеш"] -= person["ставка"]
            print("Выпал ноль, а значит вы проиграли ставку. Ваш кеш", person["кеш"])
    elif redOrBlack == "черный":
        if chanse in range(1,18):
            person["кеш"] += person["ставка"]
            print("Победа, Ставка удваивается теперь. Ваш кеш:",person["кеш"])
        elif chanse in range(19,36):
            person["кеш"] -= person["ставка"]
            print("К сожалению выпал красный цвет, а значит вы проиграли ставку. Ваш кеш:", person["кеш"])
        else:
            person["кеш"] -= person["ставка"]
            print("Выпал ноль, а значит вы проиграли ставку. Ваш кеш:", person["кеш"])
    time.sleep(3)
def delim():
    while True:
        person["ставка"] = math.fabs(int(input(person["имя"] + " делайте свою ставку.(У вас 5000) ")))
        if person["ставка"] <= 0:
            print("Ставка должна быть больше нуля")
            continue
        break
    if person["ставка"] > person["кеш"]:
        person["ставка"] = person["кеш"]
        print("Так как ставка больше кеша ставка - все деньги")
    while True:
        cetOrUncet = input("Ставка сделанна. Выберете четное или нечетное ").lower().strip()
        if cetOrUncet != "четное" and cetOrUncet != "нечетное":
            print("Вы можете выбрать только четное или нечетное")
            time.sleep(1)
            continue
        time.sleep(1)
        break
    intNumber = random.randint(0,36)
    if cetOrUncet == "четное":        
        if intNumber == 0:
            person["кеш"] -= person["ставка"]
            print("К сожалению выпал ноль. Ваш кеш ",person["кеш"])
        elif intNumber % 2 == 0 and intNumber != 0:
            person["кеш"] += person["ставка"]
            print("Победа, Ставка удваивается теперь у вас",person["кеш"])
        elif intNumber % 2 != 0:
            person["кеш"] -= person["ставка"]
            print("К сожалению выпало нечетное число. Ваш кеш ",person["кеш"]) 
    if cetOrUncet == "нечетное":
        if intNumber == 0:
            person["кеш"] -= person["ставка"]
            print("К сожалению выпал ноль. Ваш кеш ",person["кеш"])
        elif intNumber % 2 == 0 and intNumber != 0:
            person["кеш"] -= person["ставка"]
            print("К сожалению выпало четное число. Ваш кеш ",person["кеш"])
        elif intNumber % 2 != 0:
            person["кеш"] += person["ставка"]
            print("Победа, Ставка удваивается теперь у вас",person["кеш"]) 
def number():
    while True:
        person["ставка"] = math.fabs(int(input(person["имя"] + " делайте свою ставку.(У вас 5000) ")))
        if person["ставка"] <= 0:
            print("Ставка должна быть больше нуля")
            continue
        break
    if person["ставка"] > person["кеш"]:
        person["ставка"] = person["кеш"]
        print("Так как ставка больше кеша ставка - все деньги")
    while True:
        numberForAnswer = input("Ставка сделанна. Выберете число от 0 до 36 ").lower().strip()
        if numberForAnswer > 36  or numberForAnswer < 0:
            print("Вы можете выбрать только число от 0 до 36")
            time.sleep(1)
            continue
        time.sleep(1)
        break
    intNumber = random.randint(0,36)
    if numberForAnswer == intNumber:
        person["ставка"] *= 35
        person["кеш"] += person["ставка"]
        print("Вы отгадали число!!! тавка увеличивается в 35 раз.\nТеперь ваш кеш:",person["кеш"])
    else:
        person["кеш"] -= person["ставка"]
        print("К сожалению вы ошиблись.\nТеперь ваш кеш:",person["кеш"])
vip_list = input("Введите приглашенных людей ")
while True:
    person = {"кеш": 5000}
    person["имя"] = input("Представьтесь, молодой человек! ")
    if person["имя"] in vip_list:
        print("Добро пожаловать!") 
        while True:
            if person["кеш"] <= 0:
                print("Вы проиграли все деньги и ушли ")
                break
            print("Выберете тип игры:\n По цвету(Красный, Черный) \
                при отгадывании цвета ставка удваивается,\n \
                по делимости числа(четное,нечетное - ноль не считается) \
                при одгадывании ставка  так-же удваивается,\n\
                при отградывании номера числа ставка увеличивается в 36 раз")
            tipIgri = input("""1.По цвету
2.По делимости
3.По числу""").lower()
            
            if tispIgri == "1" or tipIgri == "по цвету" or tipIgri == "цвет":
                color()
            elif tipIgri == "2" or tipIgri == "по делимости" or tipIgri == "делимость":
                delim()
            elif tipIgri == "3" or tipIgri == "по числу" or tipIgri == "число":
                number()
        break
    else:
        print("Вас погнали поджопниками!")