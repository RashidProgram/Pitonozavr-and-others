f = open('exsample.txt',"w")
f.write("Hello World!")
f.close()

f = open('exsample.txt',"r")
print(f.read(6))
f.seek(1)
print(f.read(6))
