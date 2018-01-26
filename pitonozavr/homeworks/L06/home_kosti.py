import math, random, time
print("""Добро пожаловать в игру коcти. Это игра на двоих: 
делаете ставку и ваш противник тоже, будет выбрана меньшая из них. 
Потом бросаете кости и ставка достается тому кто выбросил больше.
Игра продолжается пока у одного из игроков не закончатся деньги""")
player1 = {"кеш": 5000}
player2 = {"кеш": 5000}

player1["имя"] = input("Имя первого игрока: ")
player2["имя"] = input("Имя второго игрока: ")
if player1["имя"] == "" or player1["имя"] == " ":
    player1["имя"] = "Гость"

if player2["имя"] == "" or player2["имя"] == " ":
    if  player1["имя"] != "Гость":
        player2["имя"] = "Гость"
    elif  player1["имя"] == "Гость":
        player2["имя"] = "Гость2"
print(player1["имя"],"против",player2["имя"])
i = 0 
print("У обоих игроков кеш 5 тысяч")
print("Ставки должны быть равны. В ином случае у обоих будет меньшая из ставок")
time.sleep(1)
while True:
    if i > 0:
        print("Следующий ход")
    i += 1
    player1["ставка"] = math.fabs(int(input("Ставка "+player1["имя"]+" : ")))
    player2["ставка"] = math.fabs(int(input("Ставка "+player2["имя"]+" : ")))
    if player1["ставка"] == 0 or player2["ставка"] == 0 :
        print("Ставка должна быть больше нуля")
        continue
    time.sleep(2)
    player1["счет"] = random.randint(2,12)
    player2["счет"] = random.randint(2,12)

    if player1["ставка"] > player1["кеш"]:
        player1["ставка"] = player1["кеш"]
        print("Так как ставка первого игрока больше его кеша ставка - все деньги")
        time.sleep(2)
    if player2["ставка"] > player2["кеш"]:
        player2["ставка"] = player2["кеш"]
        print("Так как ставка второго игрока больше его кеша ставка - все деньги")
        time.sleep(2)
    if player1["ставка"] < player2["ставка"]:
        player2["ставка"] = player1["ставка"]
    elif  player1["ставка"] > player2["ставка"]:
        player1["ставка"] = player2["ставка"]
    time.sleep(2)
    print("В итоге по правилам игры ставка",player1["имя"],":",int(player1["ставка"]),",а ставка",player2["имя"],":",int(player1["ставка"]))
    time.sleep(2)
    print("Ставки сделаны, Бросаем кости...")
    time.sleep(2.5)
    print(player1["имя"],"выбросил:", player1["счет"],"\n А ",player2["имя"],"",player2["счет"])
    time.sleep(2)
    if player1["счет"] > player2["счет"]:
        player1["кеш"] += player2["ставка"]
        player2["кеш"] -= player2["ставка"]
        print(player1["имя"],"выиграл ставку: ", int(player2["ставка"]),"у него сейчас:",int(player1["кеш"]),",\nа у",player2["имя"],"осталось ",int(player2["кеш"]))
    elif player2["счет"] > player1["счет"]:
        player2["кеш"] += player1["ставка"]
        player1["кеш"] -= player1["ставка"]
        print(player2["имя"], "выиграл ставку: ", int(player1["ставка"]),"у него сейчас: ",int(player2["кеш"]),",\nа у", player1["имя"],"осталось ",int(player1["кеш"]))
    else:
        print("Ничья")
        print("У первого игрока",player1["кеш"],",а у второго игрока ",player2["кеш"])
    if player1["кеш"] <= 0:
        print("Поздравляю!",player2["имя"],"выиграл игру!")
        break
    if player2["кеш"] <= 0:
        print("Поздравляю! ",player1["имя"],"выиграл игру!")
        break
