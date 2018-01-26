text = input("Что зашифровать ")
shifrPart1 = text[::-2]
shifrPart2 = text[1::2]
shifrPart3 = text[::-1]
shifr = shifrPart1  + shifrPart3 + shifrPart2
print("Вот ваш шифр",shifr)