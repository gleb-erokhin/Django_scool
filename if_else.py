old = int(input('Ваш возраст: '))
 
print('Рекомендовано:', end=' ')

try:
	    if 3 <= old < 6:
	    	print('"Заяц в лабиринте"')   
		elif 6 <= old < 12:
	    	print('"Марсианин"')
		elif 12 <= old < 16:
	   	 print('"Загадочный остров"')
		elif 16 >= old:
	    	print('"Поток сознания"')
		else:
			print('ваш возраст старше, вам в другую комнату!')
except ValueError:
		print(f'введено неверное значение возраста {old} должно быть целым числом')