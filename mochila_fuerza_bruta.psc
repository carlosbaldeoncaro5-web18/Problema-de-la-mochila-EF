Algoritmo mochila_fuerza_bruta
    
    Definir n, capacidad, i, mascara Como Entero
    Definir pesos, valores Como Entero
    Definir peso_total, valor_total, mejor_valor Como Entero
    Definir mejor_peso Como Entero
    Definir mejor_combinacion, combinacion_actual Como Cadena
    Definir total_combinaciones Como Entero
    Definir potencia Como Entero
    Definir bit_actual Como Entero
    
    capacidad = 7
    n = 4
    
    Dimension pesos[n]
    Dimension valores[n]
    
    pesos[1] = 2
    pesos[2] = 3
    pesos[3] = 5
    pesos[4] = 4
    
    valores[1] = 10
    valores[2] = 15
    valores[3] = 25
    valores[4] = 20
    
    mejor_valor = 0
    mejor_peso = 0
    mejor_combinacion = ""
    total_combinaciones = 2 ^ n
    
    Escribir "=============================================="
    Escribir "PROBLEMA DE LA MOCHILA - FUERZA BRUTA"
    Escribir "=============================================="
    Escribir "Productos disponibles: ", n
    Escribir "Capacidad del camion: ", capacidad, " kg"
    Escribir "Total de combinaciones: ", total_combinaciones
    Escribir ""
    
    Para mascara = 0 Hasta total_combinaciones - 1 Hacer
        peso_total = 0
        valor_total = 0
        combinacion_actual = ""
        
		
        Para i = 1 Hasta n Hacer
            
            potencia = 2 ^ (i - 1)
            
            bit_actual = TRUNC(mascara / potencia) % 2
            Si bit_actual > 0 Entonces
                peso_total = peso_total + pesos[i]
                valor_total = valor_total + valores[i]
                combinacion_actual = combinacion_actual + ConvertirATexto(i) + " "
            FinSi
        FinPara
        
        Si peso_total <= capacidad Y valor_total > mejor_valor Entonces
            mejor_valor = valor_total
            mejor_peso = peso_total
            mejor_combinacion = combinacion_actual
        FinSi
    FinPara
    
    Escribir "=============================================="
    Escribir "RESULTADO"
    Escribir "=============================================="
    Escribir "Mejor valor obtenido: $", mejor_valor
    Escribir "Productos seleccionados: ", mejor_combinacion
    Escribir "Peso total: ", mejor_peso, " kg"
    Escribir "=============================================="
    
FinAlgoritmo
	
