from time import sleep
from numbError import intError as intErr
input
class Users:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def register(self):
        bool_aut = False
        f = open("List_of_users.txt", "r+", encoding = "utf-8")
        for log in f:
            if self.login == log.split(" : ")[0]:
                print("Пользователь с таким именем уже есть.\n")
                answer = intErr("1 - Попробовать еще\n2 - Войти",1,2,1)
                if answer == 1:
                    register()
                    break
        else:
            input("Введите ваше имя")
            input("Введите вашу фамилию")
            input("Введите ваш возраст")
            f.write(self.login + " : " + self.password + "\n")
            print("Регистрация прошла успешно! Шаааа!!!")
            basket_f = open("Basket_"+self.login+".txt", "w", encoding = "utf-8")
            bool_aut = True
            basket_f.write("Список покупок пользователя " + user.login + "." + '\n')
            basket_f.close()
        f.close()
        return bool_aut
    def autorize(self):
        bool_aut = False
        f = open("List_of_users.txt", "r", encoding = "utf-8")
        for log in f:
            if self.login == log.split(" : ")[0] and self.password == log.rstrip("\n").split(" : ")[1]:
                print("Авторизация прошла успешно")
                bool_aut = True
                break
        else:
            print("Не удается авторизоваться")
            choice = intErr(("1 - Ввести данные заново\n2 - Зарегистрироваться"),1,2,1)
            if choice == 1:
                self.login = input("Введите логин")
                self.password = input("Введите пароль")     
                self.autorize()
            elif choice == 2:
                self.register()
        f.close()
        return bool_aut

def show_tickets():
    f = open("Shop_list.txt", "r", encoding = "utf-8")
    print("Список товаров:")
    for tick in f:
        print(tick.split(" : ")[0].rstrip("\n"))
    f.close()

def buy_tickets(user):
    f = open("Shop_list.txt", "r", encoding = "utf-8")
    while True:
        name = input("Введи название Товара или 1 если хотите посмотреть список товаров")
        if name == "1":
            show_tickets()
            continue
        break
    while True:
        i = input("Для выхода из меню покупок введите 0 для продолжения что хотите")
        if i == "0":
            break
        for bask in f:
            print(bask.split(" : ")[0])
            if name == bask.split(" : ")[0]:
                print("Товар успешно найден и добавлен в корзину")
                basket_f = open("Basket_"+self.login+".txt", "a", encoding = "utf-8")
                basket_f.write(bask)
                break
        else:
            print("Товар "+name+" не найден")



print("Приветствуем вас на нашем сайте\n")
sleep(1)
print("Перед тем как зайти на него пройдите авторизацию:")
sleep(1)
i = intErr("1 - Войти\n2 - Зарегистрироваться\n3 - е хочу регестрироваться",1,3,1)
if i != 3:
    user = Users(input("Введите логин:"), input("Введите пароль:"))
if i == 1:
    bool_aut = user.autorize()
elif i == 2: 
    bool_aut = user.register()
else:
    print("Хорошо, но многие функции сайта недоступны")
    bool_aut = False
while True:
    print("Хотите посмотреть товары или добавить их в корзину")
    answer = intErr("1 - Посмотреть\n2 - Добавить\n3 - Выйти из магазина",1,2,1)
    if answer == 1:
        show_tickets()
        continue
    elif answer == 2:
        if bool_aut == True:
            buy_tickets(user)
        else:
            print("Отправлять товары в корзину могут только авторизованные пользователи")
            sleep(1)
            answer = intErr("1 - Зарегистрироваться\n2 - Войти\n3 - Не отправлять в корзину",1,2,1)
            if answer == 1:
                user = Users(input("Введите логин:"), input("Введите пароль:"))
                user.register()
            elif answer == 2:
                user = Users(input("Введите логин:"), input("Введите пароль:"))
                user.autorize()
            else:
                continue
    else:
        print("До свидания!!")
        sleep(2)
        break


