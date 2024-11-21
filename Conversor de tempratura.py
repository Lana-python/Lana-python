#Conversor de temperaturas
print ("---------- Conversor de Temperaturas --------------")
conv = int(input('''\nEscolha a conversão: 
	[1] °C -> °F
	[2] °F -> °C
	[3] °C -> K
	[4]  K -> °C
	[5] °F -> K
	[6]  K -> °F '''))
print ("---------------------------------------------------")

if conv == 1:
	C = float(input("Temperatura em °C: "))
	F = ((9*C)/5) + 32
	print ("Temperatura em °F: ", round(F, 2))
elif conv == 2:
	F = float(input("Temperatura em °F: "))
	C = (F - 32)/1.8
	print ("Temperatura em °C: ", round(C, 2))
elif conv == 3:
	C = float(input("Temperatura em °C: "))
	K = C + 273.15 
	print ("Temperatura em K: ", round(K, 2))
elif conv == 4:
	K = float(input("Temperatura em K: "))
	C = K - 273.15
	print ("Temperatura em °C: ", round(C, 2))
elif conv == 5:
	F = float(input("Temperatura em °F: "))
	K = ((F - 32)*5)/9 + 273.15
	print ("Temperatura em K: ", round(K, 2))
elif conv == 6:
	K = float(input("Temperatura em K: "))
	F = (K - 273.15)*1.8 + 32
	print ("Temperatura em °F: ", round(F, 2))
else:
	print ("Código inválido")



