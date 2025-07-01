# 1. Imprime "Hola, mundo"
print("Hola, mundo")

# 2. Imprime "Hola, Álvaro" con el nombre en una variable
nombre = "Álvaro"
print("Hola", nombre) # con una coma
print("Hola " + nombre) # con un +

# 4. Imprimir "Me encanta comer completos y papas fritas" con las comidas en variables
comida1 = "completos"
comida2 = "papas fritas"
print ("Me encanta comer {} y {}".format(comida1, comida2)) # con .format()
print (f"Me encanta comer {comida1} y {comida2}") # con f-string

#BONUS NINJA
print ("Me encanta comer %s y %s" % (comida1, comida2)) # con %

# 3. Imprimir "Hola 156!" con el número en una variable
numero = 777
print("Hola", numero, "!") # con una coma
print("Hola " + str(numero) + "!") # con un + y un str
print("Hola " + numero + "!") # con un + y da error





