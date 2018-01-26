# описываем участников + скорость, нитро, бак, расход топлива, имя, пройденный путь
# на выбор: обычная скорость, нитро + расход топлива в 3 - каждый ход
# Побеждает тот, кто приехал первым, либо тот, у кого позже заккккончилось топливо
def state(car):
	print("Текущее состояние:",
		"Топливо: " + str(car["fuel"]),)
		"Растояние: " + str(car["distanse"] + "/" + str(track)),
def easy(car):
	car["distanse"] += car["speed"]
	car["fuel"] -= car["expen"]

def nitro(car):
	car["distanse"] += car["speed"]
	car["fuel"] -= car["expen"] * 3

def step(car):
	choose = input("Твой ход " + car["name"] + " Что будем делать \
	1 - Просто едем\n" + 
	"2 - топим!")
	if choose == "1":
		easy(car)
	elif choose == "2":
		nitro(car)
	stata(car)
	input()
track = 50
car1 = {
"name": "Бетмобиль",
"speed": 6,
"fuel": 35,
"expen": 3,
"nitro": 11,
"distanse": 0,
} 
car2 = {
"name": "Черная молния",
"speed": 8,
"fuel": 30,
"expen": 4,
"nitro": 13,
"distanse": 0,
}
while True:
	step(car1)
	step(car2)
