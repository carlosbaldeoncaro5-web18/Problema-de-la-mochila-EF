Algoritmo mochila_programacion_dinamica
	
	Definir n, capacidad, i, w Como Entero
	Definir mejor_valor, peso_total Como Entero
	Definir mejor_combinacion Como Cadena
	Definir pesos, valores Como Entero
	Definir dp Como Entero
	Definir seleccionado Como Logico
	
	capacidad = 7
	n = 4
	
	Dimension pesos[n]
	Dimension valores[n]
	Dimension seleccionado[n]
	Dimension dp[n+1, capacidad+1]
	
	pesos[1] = 2
	pesos[2] = 3
	pesos[3] = 5
	pesos[4] = 4
	
	valores[1] = 10
	valores[2] = 15
	valores[3] = 25
	valores[4] = 20
	
	Para i = 1 Hasta n Hacer
		seleccionado[i] = Falso
	FinPara
	
	Escribir "=============================================="
	Escribir "PROBLEMA DE LA MOCHILA - PROGRAMACION DINAMICA"
	Escribir "=============================================="
	Escribir "Productos disponibles: ", n
	Escribir "Capacidad del camion: ", capacidad, " kg"
	Escribir ""
	
	
	Para i = 0 Hasta n Hacer
		dp[i+1, 1] = 0
	FinPara
	
	Para w = 0 Hasta capacidad Hacer
		dp[1, w+1] = 0
	FinPara
	
	
	Para i = 1 Hasta n Hacer
		Para w = 1 Hasta capacidad Hacer
			Si pesos[i] <= w Entonces
				Si dp[i, w+1] > dp[i, w - pesos[i] + 1] + valores[i] Entonces
					dp[i+1, w+1] = dp[i, w+1]
				Sino
					dp[i+1, w+1] = dp[i, w - pesos[i] + 1] + valores[i]
				FinSi
			Sino
				dp[i+1, w+1] = dp[i, w+1]
			FinSi
		FinPara
	FinPara
	
	mejor_valor = dp[n+1, capacidad+1]
	w = capacidad
	
	Para i = n Hasta 1 Con Paso -1 Hacer
		Si dp[i+1, w+1] <> dp[i, w+1] Entonces
			seleccionado[i] = Verdadero
			w = w - pesos[i]
		FinSi
	FinPara
	
	mejor_combinacion = ""
	peso_total = 0
	
	Para i = 1 Hasta n Hacer
		Si seleccionado[i] = Verdadero Entonces
			mejor_combinacion = mejor_combinacion + ConvertirATexto(i) + " "
			peso_total = peso_total + pesos[i]
		FinSi
	FinPara
	
	Escribir "=============================================="
	Escribir "RESULTADO"
	Escribir "=============================================="
	Escribir "Mejor valor obtenido: $", mejor_valor
	Escribir "Productos seleccionados: ", mejor_combinacion
	Escribir "Peso total: ", peso_total, " kg"
	Escribir ""
	
	Escribir "=============================================="
	Escribir "TABLA DP"
	Escribir "=============================================="
	Escribir Sin Saltar "     "
	Para w = 0 Hasta capacidad Hacer
		Escribir Sin Saltar w, " "
	FinPara
	Escribir ""
	
	Para i = 0 Hasta n Hacer
		Escribir Sin Saltar i, "   "
		Para w = 0 Hasta capacidad Hacer
			Escribir Sin Saltar dp[i+1, w+1], " "
		FinPara
		Escribir ""
	FinPara
	Escribir "=============================================="
	
FinAlgoritmo