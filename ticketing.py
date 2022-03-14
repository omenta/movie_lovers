def movie_tix():
	price = 1
	movie_lovers = {}
	persons = int(input('Party: '))
	for i in range(persons):
		name = input('Name: ')
		age = int(input('Age: '))
		movie_lovers[name] = age
	
	print(movie_lovers) # TEMP
	print('NAME-------PRICE')
	for i in movie_lovers:
		if movie_lovers[i] > 0 and movie_lovers[i] < 65:
			if persons >= 5:
				price = 10 * 0.8
			else:
				price = 10
		elif movie_lovers[i] >= 65:
			if persons >= 5:
				price = 8 * 0.8
			else:
				price = 8
		else:
			# Invalid age
			print('Error!')
		print(i, '     $', price)
			
movie_tix()
