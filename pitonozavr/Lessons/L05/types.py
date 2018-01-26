scientists = ("Альберт","Максвелл","Диофант") #Кортедж
main = "Cobol"
langs = "Java", "Assembler","Scratch", main # Кортедж
print(langs)
print(langs[1])
x, y, z = scientists
print(x, y ,z)
a, b, c, d, e, = 1, 2, 3, 4, 5
print(a, b, c)

saeed = {}
print(saeed)
writters = {"Рей Бредбери", "Джордж Оруэлл", "Жуль Верн", \
"Джордж Мартин","Эрих Мапия Ремарк", "Джордж Оруэлл"}
print(writters)
antiutop = {"Оксана", "Рэй Бредбери", "Джордж Оруэлл","Замятин"}
print(writters & antiutop) # Пересечение
print(writters | antiutop) # Обьединение
print(writters - antiutop) # Вычитание 2 из 1
print(antiutop - writters) # Вычитание 1 из 2
print(antiutop ^ writters) # Все элменты без общих
directors = {
    ("Спилберг": "Парк Юрского Периода", "Челюсти", "Список Шидлера")
    ("Нолан": "Дюнкер","Престтиж","Начало")
    ("Бондарчук": "Притяжения","9 рота","Обитаемый Остров")
}
print(directors["Нолан"])
