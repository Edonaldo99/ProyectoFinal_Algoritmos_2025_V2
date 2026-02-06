import os
import heapq
from collections import Counter
import matplotlib.pyplot as plt

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izq = None
        self.der = None
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def generar_tabla_codigos(raiz):
    codigos = {}
    def recorrer(nodo, codigo):
        if nodo is None:
            return
        if nodo.caracter is not None:
            codigos[nodo.caracter] = codigo
            return
        recorrer(nodo.izq, codigo + "0")
        recorrer(nodo.der, codigo + "1")
    recorrer(raiz, "")
    return codigos

def dibujar_arbol(raiz, output_path="outputs/huffman_tree.png"):
    fig, ax = plt.subplots(figsize=(12, 8))
    posiciones = {}
    def asignar_posiciones(nodo, x, y):
        if nodo is None:
            return
        posiciones[nodo] = (x, y)
        asignar_posiciones(nodo.izq, x - 1, y - 1)
        asignar_posiciones(nodo.der, x + 1, y - 1)
    asignar_posiciones(raiz, 0, 0)
    for nodo, (x, y) in posiciones.items():
        ax.text(x, y, f"{nodo.caracter}\n{nodo.frecuencia}", ha="center")
        if nodo.izq:
            x2, y2 = posiciones[nodo.izq]
            ax.plot([x, x2], [y, y2])
        if nodo.der:
            x2, y2 = posiciones[nodo.der]
            ax.plot([x, x2], [y, y2])
    ax.axis("off")
    plt.savefig(output_path, dpi=200)
    plt.close()

def graficar_frecuencias(frecuencias, output_path="outputs/huffman_freq.png"):
    caracteres = list(frecuencias.keys())
    valores = list(frecuencias.values())
    plt.figure(figsize=(10, 6))
    plt.bar(caracteres, valores)
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()

def ejecutar_huffman(txt_path="data/texto.txt"):
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open(txt_path, "r", encoding="utf-8") as f:
        texto = f.read()
    frecuencias = dict(Counter(texto))
    print("Frecuencias de caracteres:")
    for c, f in frecuencias.items():
        print(repr(c), ":", f)
    heap = []
    for c, f in frecuencias.items():
        heapq.heappush(heap, NodoHuffman(c, f))
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        nuevo = NodoHuffman(None, n1.frecuencia + n2.frecuencia)
        nuevo.izq = n1
        nuevo.der = n2
        heapq.heappush(heap, nuevo)
    raiz = heap[0]
    codigos = generar_tabla_codigos(raiz)
    print("Tabla de códigos Huffman:")
    for c, code in codigos.items():
        print(repr(c), ":", code)
    dibujar_arbol(raiz, "outputs/huffman_tree.png")
    graficar_frecuencias(frecuencias, "outputs/huffman_freq.png")
