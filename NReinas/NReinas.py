# Julian Camilo Gomez Vergara
# Universidad Central
# Inteligencia Artificial - 2S-2017
# 2017-08-11

# Numero de reinas
# Especifique el valor de N para procesar
N = 4

# Recorre todos los tableros desde 1 hasta N
for v in range(1,N+1):
	N = v
	
	print("\n---------------------------------------")
	print("\tN reinas " + str(N) + " x " + str(N))
	print("---------------------------------------\n\n")

	# Contadores de respuestas correctas e incorrectas
	correctas = 0
	incorrectas = 0	
	
	for z in range (N):

		# Inicializa el vector solucion
		S = []
		for r in range(N):
			S.append(-1)

		# Inicia con la reina en la posicion mas a la izquierda
		S[z] = 0
		
		for w in range(N):
			
			# Recorrer el tablero horizontalmente
			for x in range(N):

				# Recorre el tablero verticalmente
				for y in range(N):

					# Determina si las reinas se atacan
					se_atacan = 0
				
					# Valida si la posicion esta disponible en la solucion
					if S[x] == -1:
					
						# Recorre cada columna para comparar con la nueva posicion hipotetica
						for z in range(N):
							#print("\nS[" + str(z) + ", " + str(x) + "]\nP[" + str(S[z]) + ", " + str(y) + "]")
							if abs(z-x) == abs(S[z]-y):
								#print("Dentro: " + str(abs(z-x)) + " = " + str(abs(S[z]-y)))
								se_atacan = 1
								#print("diagonal")
							if S[z] == y:
								se_atacan = 1
								#print("horizontal")
						
						if se_atacan == 0:
							S[x] = y
					
		# Flag para saber si hubo solucion			
		solucion = 0
						
		for i in range(N):
			if S[i] == -1:
				solucion = 1
				
		if solucion == 1:
			mensaje = "Sin solucion completa:\t" + str(S)
			incorrectas = incorrectas+1
		else:
			mensaje = "Solucion para N = " + str(N) + " :\t" + str(S)
			correctas = correctas+1
				
		# Imprime el array Solucion
		print(mensaje)
		
	# Imprime Tableros ordenados y desordenados
	print("\n---------------------------------------")
	print("Ordenados:\t" + str(correctas) + "\nImposibles:\t" + str(incorrectas))
	print("---------------------------------------\n\n")