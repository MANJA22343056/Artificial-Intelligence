dataInt = 9.1
print("data=", dataInt, "type=", type(dataInt))

dataFloat = 9.5
print("data= ", dataInt, "type=", type(dataInt))

# cara merubah dataInt diatas adalah sebagai berikut.
dataFloat = float(dataInt)
print("data=", dataFloat, "type=", type(dataFloat))
dataInt = int(dataInt)
dataStr = float(dataInt)
dataBool = bool(dataInt)
print("data =", dataFloat, "type=", type(dataFloat))
print("data =", dataInt, "type=", type(dataInt))
print("data =", dataStr, "type=", type(dataStr))
print("data =", dataBool, "type=", type(dataBool))


dtaInt = 0
dtaBool = bool(dtaInt)
print("data =", dtaInt, "type=", type(dtaInt))
print("data =", dtaBool, "type=", type(dtaBool))
