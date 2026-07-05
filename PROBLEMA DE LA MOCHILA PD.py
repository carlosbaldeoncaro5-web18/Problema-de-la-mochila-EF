
"""
================================================================
PROGRAMACIÓN DINÁMICA - PROBLEMA DE LA MOCHILA 0/1
Complejidad: O(n × W)
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



def mochila_programacion_dinamica(pesos: List[float], valores: List[float], capacidad: float) -> Tuple[float, List[int], List[List[float]]]:
    
    n = len(pesos)
    W = int(capacidad)
    
    
    dp = [[0.0] * (W + 1) for _ in range(n + 1)]
    
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if pesos[i-1] <= w:
                incluir = dp[i-1][w - int(pesos[i-1])] + valores[i-1]
                no_incluir = dp[i-1][w]
                dp[i][w] = max(no_incluir, incluir)
            else:
                dp[i][w] = dp[i-1][w]
    
    
    w = W
    combinacion = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            combinacion.append(i)
            w -= int(pesos[i-1])
    combinacion.reverse()
    
    return dp[n][W], combinacion, dp


def mochila_dp_optimizada(pesos: List[float], valores: List[float], capacidad: float) -> float:
    """
    Programación Dinámica Optimizada - O(W) en espacio
    """
    W = int(capacidad)
    dp = [0.0] * (W + 1)
    
    for i in range(len(pesos)):
        for w in range(W, int(pesos[i]) - 1, -1):
            if dp[w - int(pesos[i])] + valores[i] > dp[w]:
                dp[w] = dp[w - int(pesos[i])] + valores[i]
    
    return dp[W]



class SistemaProgramacionDinamica:
    def __init__(self):
        self.productos: List[Producto] = []
        self.capacidad: float = 0.0
        self.contador_id: int = 1
        self.historial: List[dict] = []
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
            print("\n  No hay productos registrados")
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
            print("  ID inválido")
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
                    print("  Operación cancelada")
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
    
    def mostrar_tabla_dp(self, dp: List[List[float]]):
        
        print("\n" + "=" * 50)
        print("  TABLA DE PROGRAMACIÓN DINÁMICA")
        print("=" * 50)
        
        print("    ", end="")
        for w in range(len(dp[0])):
            print(f"{w:6}", end="")
        print()
        print("   " + "-" * (6 * len(dp[0])))
        
        for i, fila in enumerate(dp):
            print(f"{i:3} ", end="")
            for valor in fila:
                print(f"{valor:6.0f}", end="")
            print()
    
    def ejecutar_dp(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("PROGRAMACIÓN DINÁMICA - OPTIMIZACION DE CARGA")
        
        if not self.productos:
            print("\n  No hay productos registrados")
            self.pausar()
            return
        
        if self.capacidad <= 0:
            print("\n  Configure la capacidad del camión primero")
            self.pausar()
            return
        
        n = len(self.productos)
        pesos = [p.peso for p in self.productos]
        valores = [p.valor for p in self.productos]
        
        print(f"\n  Productos disponibles: {n}")
        print(f"  Capacidad del camion: {self.capacidad:.1f} kg")
        print(f"  Tamaño de tabla: {n} × {int(self.capacidad) + 1} = {n * (int(self.capacidad) + 1):,} celdas")
        print("-" * 50)
        print("  Ejecutando...")
        
        inicio = time.time()
        mejor_valor, combinacion, dp = mochila_programacion_dinamica(pesos, valores, self.capacidad)
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
        
        if combinacion:
            print("\n  Detalle de productos seleccionados:")
            print("  " + "-" * 45)
            for idx in combinacion:
                p = self.productos[idx-1]
                print(f"    {p}")
        
        self.mostrar_tabla_dp(dp)
        
        
        print("\n" + "=" * 50)
        print("  ⚡ DP OPTIMIZADA (O(W) espacio)")
        print("=" * 50)
        inicio = time.time()
        valor_opt = mochila_dp_optimizada(pesos, valores, self.capacidad)
        tiempo_opt = (time.time() - inicio) * 1000
        print(f"  Valor maximo: ${valor_opt:.2f}")
        print(f"  Tiempo: {tiempo_opt:.4f} ms")
        
        self.pausar()
    
    def menu(self):
        while True:
            self.limpiar_pantalla()
            print("\n" + "=" * 60)
            print("  PROGRAMACIÓN DINÁMICA - PROBLEMA DE LA MOCHILA")
            print("=" * 60)
            print(f"  Productos: {len(self.productos)} | Capacidad: {self.capacidad:.1f} kg")
            print("=" * 60)
            print("\n  1. Registrar producto")
            print("  2. Listar productos")
            print("  3. Eliminar producto")
            print("  4. Configurar capacidad")
            print("  5. Ejecutar Programación Dinámica")
            print("  6. Salir")
            print("-" * 60)
            
            opcion = input("  Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.registrar_producto()
            elif opcion == "2":
                self.listar_productos()
            elif opcion == "3":
                self.eliminar_producto()
            elif opcion == "4":
                self.configurar_capacidad()
            elif opcion == "5":
                self.ejecutar_dp()
            elif opcion == "6":
                print("\n  gracias por usar el sistema!")
                break
            else:
                print("\n  Opcion invalida")
                self.pausar()



if __name__ == "__main__":
    sistema = SistemaProgramacionDinamica()
    sistema.menu()