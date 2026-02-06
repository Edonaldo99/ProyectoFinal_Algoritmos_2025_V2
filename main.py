from algorithms.prim import ejecutar_prim
from algorithms.kruskal import ejecutar_kruskal
from algorithms.dijkstra import ejecutar_dijkstra
from algorithms.huffman import ejecutar_huffman

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ejecutar Prim")
        print("2. Ejecutar Kruskal")
        print("3. Ejecutar Dijkstra")
        print("4. Ejecutar Huffman")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_prim()
        elif opcion == "2":
            ejecutar_kruskal()
        elif opcion == "3":
            nodo = input("Ingrese nodo origen: ")
            ejecutar_dijkstra(nodo)
        elif opcion == "4":
            ejecutar_huffman()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
