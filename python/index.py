nombre = int("10")
numero = int(nombre)
texto = """
    a) entrar al menu
    b) ver saldo
    c) depositar
    d) retirar
    e) salir
"""
x, y = 12, 10
print(type(nombre))
print(type(numero))
print(texto)
print(x)
print(y)
arreglo = ["fer", "leo", "doki", "xyz"]
print(type(arreglo))
print(arreglo)
print(arreglo[1])
arreglo[1] = "cerdo"
print(arreglo[1])
print(len(arreglo))
del arreglo[0]
print(arreglo)
arreglo[0] = "xd"
print(arreglo)
arreglo.clear()
print(arreglo)
arreglo2 = ["Fer", 20, True, ["doki", "noa"]]
print(arreglo2[3][0])
objeto = {"fer", "nice", 20}
print(objeto)
objeto.add("xd")
print(objeto)
print("xdd" in objeto)

biblioteca = {
    "nombre": "fernando",
    "apellido": "flores",
    "edad": 22,
    "idiomas": ["ingles", "italiano", "frances"]
}
print(biblioteca["idiomas"][2])

if (10 > 50):
    print("10 es mayor")
else: 
    print("50 es mayor")
    

numerox = input("Ingrese un numero: ")
print(numerox)