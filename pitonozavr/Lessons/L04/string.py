amin = "Мороз и солнце - день чудесный. Ещё ты дремлешь, друг прелестный? "
print(amin[1]) # Вывести вторую букву(отчет с нуля)
print(amin[0]) # Вывести первую букву(отчет с нуля)
print(amin[-1]) # Вывести последнюю букву(обратный отчет идет с -1)
print(amin[8:14]) # Вывести всё с девятой буквы(включительно) до пятнадцатой буквы(не включительно)
print(amin[:14:2]) # Вывести с начала до 15 буквы через 2 т.е вывелется мрзислне
print(amin[14:0:-1]) # Вывести 
print(amin[:]) # Вывести 
print(amin.len) # Вывести 
print(amin.lower()) # Вывести 
print(amin.upper()) # Вывести 
print(amin.title()) # Вывести 

print(amin.find("Д")) # Вывести 
print(amin.rfind("Д")) # Вывести 
print(amin.replace("д","м")) # Вывести 
print(amin.count("д")) # Вывести 