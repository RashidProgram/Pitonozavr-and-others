technology = {
    "телевизоры": ("LG", "Samsung", "Sony","Panasonic","Toshiba"),
    "телефоны": ("Samsung", "Nokia", "Apple", "SonyExperia", "HTS", "Asus"),
    "ноутбуки": ("Lenovo","Hp", "Toshiba", "Aser", "Asus", "Apple"),
    "компьютеры": ("Lenovo","Hp", "Toshiba", "Aser", "Asus", "Apple"),
    "пылесосы": ("Philips","Samsung", "Bork", "LG", "Bosch"),
    "самолеты": ("Airbus","Boeing"),
    "машины": ("Toyota","Audi","BMW","Lada","Ford","Kia"),
    "приставки": ("Microsoft(XBox)","Sony(PlayStation)", "Nintendo(Wii U)"),
    "блендеры": ("Kenwood","Braun","Philips"),
    "холодильники": ("Samsung","Atlant","Ariston"),
    "кондиниоцеры": ("Haier","Toshiba","Fujitsu","Sanyo")
}
text = input("Введите технику марки которых хотите узнать.\n Если хотите посмореть всю нашу библиотеку ничего не вводите").lower()
if text == "" or text == " ":
    print("Вся библиотека:\n", technology)
elif text == "телевизоры" or text == "ноутбуки" or text == "телефоны" or text == "компьютеры" or text == "пылесосы" or text == "самолеты" or text == "машины" or text == "приставки" or text == "блендеры" or text == "холодильники" or text == "кондиниоцеры":
    print(technology[text])
else:
    print("К сожалению о", text ,"у нас ничего нет.")