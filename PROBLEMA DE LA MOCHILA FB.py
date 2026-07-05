
"""
================================================================
FUERZA BRUTA - PROBLEMA DE LA MOCHILA 0/1
Complejidad: O(2^n)
Análisis de Algoritmos y Estrategias de Programación
================================================================
"""

import time
import os
import platform
from typing import List, Tuple



class Producto:
    def __init__(self, id_producto: int, nombre: str, peso: float, valor: float):
        self.id = id_producto
        self.nombre = nombre
        self.peso = peso
        self.valor = valor
    
    def __str__(self) -> str:
        return f"ID:{self.id:3} | {self.nombre:20} | Peso:{self.peso:6.1f}kg | Valor:${self.valor:8.2f}"



def mochila_fuerza_bruta(pesos: List[float], valores: List[float], capacidad: float) -> Tuple[float, List[int], int]:
    
    n = len(pesos)
    mejor_valor = 0.0
    mejor_combinacion = []
    combinaciones_evaluadas = 0
    
    for mascara in range(1 << n):
        combinaciones_evaluadas += 1
        peso_total = 0.0
        valor_total = 0.0
        combinacion = []
        
        for i in range(n):
            if mascara & (1 << i):
                peso_total += pesos[i]
                valor_total += valores[i]
                combinacion.append(i + 1)
        
        if peso_total <= capacidad and valor_total > mejor_valor:
            mejor_valor = valor_total
            mejor_combinacion = combinacion.copy()
    
    return mejor_valor, mejor_combinacion, combinaciones_evaluadas



class SistemaFuerzaBruta:
    def __init__(self):
        self.productos: List[Producto] = []
        self.capacidad: float = 0.0
        self.contador_id: int = 1
        self.cargar_datos_ejemplo()
    
    def limpiar_pantalla(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    def pausar(self):
        input("\nPresione Enter para continuar...")
    
    def mostrar_titulo(self, titulo: str):
        print("\n" + "=" * 60)
        print(f"  {titulo}")
        print("=" * 60)
    
    def cargar_datos_ejemplo(self):
        productos_ejemplo = [
            ("Laptop", 2.5, 800),
            ("Tablet", 1.2, 400),
            ("Smartphone", 0.5, 600),
            ("Monitor", 4.0, 300),
            ("Teclado", 0.8, 50),
            ("Mouse", 0.2, 30),
            ("Impresora", 5.0, 200),
            ("Router", 0.8, 80),
            ("Cable HDMI", 0.3, 15),
            ("Disco Duro", 0.6, 120)
        ]
        for nombre, peso, valor in productos_ejemplo:
            self.productos.append(Producto(self.contador_id, nombre, peso, valor))
            self.contador_id += 1
        self.capacidad = 7.0
    
    def registrar_producto(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("REGISTRAR PRODUCTO")
        
        nombre = input("  Nombre: ").strip()
        while not nombre:
            print("  El nombre no puede estar vacio")
            nombre = input("  Nombre: ").strip()
        
        while True:
            try:
                peso = float(input("  Peso (kg): "))
                if peso > 0:
                    break
                print("  El peso debe ser mayor a 0")
            except ValueError:
                print("  Ingrese un numero valido")
        
        while True:
            try:
                valor = float(input("  Valor ($): "))
                if valor > 0:
                    break
                print("  El valor debe ser mayor a 0")
            except ValueError:
                print("  Ingrese un numero valido")
        
        producto = Producto(self.contador_id, nombre, peso, valor)
        self.productos.append(producto)
        self.contador_id += 1
        print(f"\n  Producto '{nombre}' registrado (ID: {producto.id})")
        self.pausar()
    
    def listar_productos(self):
        self.limpiar_pantalla()
        self.mostrar_titulo(f"LISTA DE PRODUCTOS ({len(self.productos)})")
        
        if not self.productos:
            print("\n  no hay productos registrados")
            self.pausar()
            return
        
        print("\n  ID  | Nombre               | Peso (kg) | Valor ($)")
        print("  " + "-" * 55)
        for p in self.productos:
            print(f"  {p.id:3} | {p.nombre:20} | {p.peso:9.1f} | {p.valor:9.2f}")
        
        print("\n" + "-" * 55)
        print(f"  Total productos: {len(self.productos)}")
        print(f"  Peso total: {sum(p.peso for p in self.productos):.1f} kg")
        print(f"  Valor total: ${sum(p.valor for p in self.productos):.2f}")
        self.pausar()
    
    def eliminar_producto(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("ELIMINAR PRODUCTO")
        
        try:
            id_buscar = int(input("  ID del producto a eliminar: "))
        except ValueError:
            print("  ID invalido")
            self.pausar()
            return
        
        for i, p in enumerate(self.productos):
            if p.id == id_buscar:
                print(f"\n  Producto a eliminar: {p}")
                confirmar = input("\n  ¿Confirmar? (s/n): ").lower()
                if confirmar == 's':
                    self.productos.pop(i)
                    print(f"  Producto eliminado")
                else:
                    print("  Operacion cancelada")
                self.pausar()
                return
        
        print(f"  No se encontro producto con ID {id_buscar}")
        self.pausar()
    
    def configurar_capacidad(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("CONFIGURAR CAPACIDAD")
        
        print(f"  Capacidad actual: {self.capacidad:.1f} kg")
        while True:
            try:
                nueva = float(input("  Nueva capacidad (kg): "))
                if nueva > 0:
                    self.capacidad = nueva
                    print(f"\n  Capacidad configurada a {self.capacidad:.1f} kg")
                    break
                print("  La capacidad debe ser mayor a 0")
            except ValueError:
                print("  Ingrese un numero valido")
        self.pausar()
    
    def ejecutar(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("FUERZA BRUTA - OPTIMIZACION DE CARGA")
        
        if not self.productos:
            print("\n  No hay productos registrados")
            self.pausar()
            return
        
        if self.capacidad <= 0:
            print("\n  Configure la capacidad del camion primero")
            self.pausar()
            return
        
        n = len(self.productos)
        pesos = [p.peso for p in self.productos]
        valores = [p.valor for p in self.productos]
        
        print(f"\n  Productos disponibles: {n}")
        print(f"  Capacidad del camion: {self.capacidad:.1f} kg")
        print(f"  Combinaciones a evaluar: {2 ** n:,}")
        print("-" * 50)
        print("  Ejecutando...")
        
        inicio = time.time()
        mejor_valor, combinacion, combinaciones = mochila_fuerza_bruta(pesos, valores, self.capacidad)
        fin = time.time()
        
        tiempo = (fin - inicio) * 1000
        
        print("\n" + "=" * 50)
        print("  RESULTADO")
        print("=" * 50)
        print(f"  Valor maximo: ${mejor_valor:.2f}")
        print(f"  Productos seleccionados: {combinacion if combinacion else 'Ninguno'}")
        
        if combinacion:
            peso_total = sum(pesos[i-1] for i in combinacion)
            print(f"  Peso total: {peso_total:.1f} kg")
            print(f"  Espacio utilizado: {(peso_total / self.capacidad * 100):.1f}%")
        
        print(f"  Tiempo de ejecucion: {tiempo:.4f} ms")
        print(f"  Combinaciones evaluadas: {combinaciones:,}")
        
        if combinacion:
            print("\n  Detalle de productos seleccionados:")
            print("  " + "-" * 45)
            for idx in combinacion:
                p = self.productos[idx-1]
                print(f"    {p}")
        
        self.pausar()
    
    def menu(self):
        while True:
            self.limpiar_pantalla()
            print("\n" + "=" * 60)
            print("  FUERZA BRUTA - PROBLEMA DE LA MOCHILA")
            print("=" * 60)
            print(f"  Productos: {len(self.productos)} | Capacidad: {self.capacidad:.1f} kg")
            print("=" * 60)
            print("\n  1. Registrar producto")
            print("  2. Listar productos")
            print("  3. Eliminar producto")
            print("  4. Configurar capacidad")
            print("  5. Ejecutar Fuerza Bruta")
            print("  6. Salir")
            print("-" * 60)
            
            opcion = input("  Seleccione una opcion: ").strip()
            
            if opcion == "1":
                self.registrar_producto()
            elif opcion == "2":
                self.listar_productos()
            elif opcion == "3":
                self.eliminar_producto()
            elif opcion == "4":
                self.configurar_capacidad()
            elif opcion == "5":
                self.ejecutar()
            elif opcion == "6":
                print("\n  gracias por usar el sistema!")
                break
            else:
                print("\n  Opcion invalida")
                self.pausar()



if __name__ == "__main__":
    sistema = SistemaFuerzaBruta()
    sistema.menu()