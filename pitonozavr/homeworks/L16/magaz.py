from time import sleep
import numbError as ne
class User:
    def signUp(self):
        qwe = open('user.txt','r',encoding="utf-8")
        print("Введите данные. * помечено то что надо написать обязательно")
        while True:   
            self.login = input("Введите логин*")
            if self.login in qwe:
                print("Такой логин уже существует")
                continue
            break
        while True:
            self.password = input('Введите пароль(минимум 4 символа максимум 10)*')
            if 3 < len(self.password) < 11:
                prova = input("Повторите пароль*")
                if self.password != prova:
                    print("Пароли не одинаковы")
                    continue
                break
            else:
                print("Вы ввели не то кол-во символов")
                continue
        self.name = input("Введите ваше имя*")
        self.lastname = input("Введите вашу фамилию")
        self.arg = input("Введите ваш возраст")
        qwe.close()
        qwe = open("user.txt","a",encoding = "utf-8")
        qwe.write(self.login+":"+self.password+","+self.lastname+" "+self.name+";"+self.arg+"=")#asdasd:123,Велиханов Рашид;13=
        qwe.close()
    def signIn(self):
        qwe = open("user.txt", "r", encoding = "utf-8")
        print("Введите логин и пароль:")
        self.login = input("Логин:")
        self.password = input("Пароль:")
        avtoris = False
        for line in qwe:  
            if self.password in line and self.login in line:
                name = False
                lastname = False
                age = False
                self.lastname = ""
                self.age = ""
                self.name = ""
                while i < len(line):
                    if lastname == True:
                        self.lastname += line[i]
                    if age == True:
                        self.age += line[i]
                    if name == True:
                        self.name += line[i]
                    if line[i] == ",":
                        lastname = True
                        age = False
                        name = False
                    if line[i] == " ":
                        lastname = False
                        age = False
                        name = True
                    if line[i] == ";":
                        lastname = False
                        age = True
                        name = False
                        #asdasd:123,Велиханов Рашид;13=
                print("Вы успешно авторизовались")
                avtoris = True
                break
        if avtoris == False:
            print("Вы ввели не правильно логин или пароль")
            answer = ne.intError('1 - Попробовать еще раз\n2 - зарегестрироваться',1,2,1)
            if answer == 1:
                self.singIn()
            else:
                self.signUp()
def viborCorsina(user):
    answer = ne.intError("1 - Перейти к отправлению товаров в корзину\n2 - Просмотреть список товаров\n",1,2,1)
    f = open("tovars.txt", "r", encoding = "utf-8")
    if  answer == 1:
        goToCorsina(user)
    elif answer == 2:
        for line in f:
            print(line)
            sleep(1)
        viborCorsina(user)
def getSpisokTovars():
    f = open('tovars.txt',"r", encoding="utf-8")
    print("Хотите посмотреть все товары или каталоги")
    answer = ne.intError("1 - все товары,\n2 - каталоги\n3 - выйти из сайта",1,3,0.7)

    if answer == 1:
        for line in f:
            print(line)
            sleep(1)
    elif answer == 2:
        print("Вот список наших каталогов:")
        for line in f:
            if "-" in line: 
                print(line[:-2])
        answer = input("Какой хотите посмотреть\nВведите название каталога(на англ)").strip()
        answer = answer.capitalize()
        prov = False
        print(line)
        for line2 in f:
            print(answer)
            if answer in line2:
                prov = True
            if line2 == '':
                break
            if prov == True:
                print(line2)
            sleep(1)
    else:
        return False
def goToCorsin(user):
    pass

answer = ne.intError("Приветствуем на нашем сайте,\nХотите войти или зарегестрироваться?\n1 - войти\n2 - зарегестрироваться",1,2,1)
if answer == 1:
    user = User()
    user.signIn()
elif answer == 2:
    user = User()
    user.signUp()
tof = getSpisokTovars()
if tof == False:
    pass
else:
    viborCorsina(user)

