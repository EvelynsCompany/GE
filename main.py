#print("hola soy angel")


#variables

nombre = "Angel"
apellido = "lopez"
altura = "180 cm"
nacimiento = "tegucigalpa"

#print(f"{nombre} - {apellido} - {altura} - {str(nacimiento)}")

#entradas

#myweb = input ("¿quieres entrar a mi web? :")
#print("entrar" + myweb)

#condiciones

#altura = int(input("¿cual es tu altura?:   "))

#if altura >= 180:
    #print("eres muy alto")
#else:
    #print("eres muy bajo")

#funciones

#var_altura = int(input("¿cual es tu altura?:   "))

#def mostrarAltura(altura):
   # Resultado = ""

  #  if altura >= 180:
       #  Resultado = "eres muy alto"
  #  else:
         #Resultado = "eres muy bajo"

    #return Resultado

#print(mostrarAltura(var_altura))

#listas

#personas = ["lopez" ,  "angel"]

#print(personas[1])

#for persona in personas:
   # print("-" + persona)

#tupla

#tupla = ("la tierra es plana", True, False)

#print((1,))

#conjunto.

#print(set([5, 2, 5, 1, 1.5]))
#print(set((5, 2, 5, 1, 1.5)))
#print(set("52511.5"))

#conjunto = set ([2,3,3,4])
#print(conjunto)

#conjunto.add(1)
#print(conjunto)

#conjunto.remove(1)
#print(conjunto)

#conjunto_2 = set([5,3,5,6])
#conjunto_3 = set([4, 2])
#print(conjunto, conjunto_2, conjunto_3)
#print(conjunto.intersection(conjunto_2))
#print(conjunto & conjunto_2)

#diccionarios

#diccionario ={1: "uno" , 2: "dos"}
#diccionario[3] =  "Tres"
#print(diccionario)

#dict_lista_tuplas = dict([(1, "uno"), (2, "dos"), (3, "tres")])
#print(diccionario)

#dict_lista_string = dict(uno = 1, dos = 2, tres = 3)
#print(dict_lista_string)

#dict_tipos = {1: "integer", 2.2: "float", "texto": "string", (1, 2): "tupla"}
#print(dict_tipos)

#dic_repiticion = {1: "primero", 1: "ultimo"}
#print(dic_repiticion)

#print(diccionario, diccionario.keys(), diccionario.values(), diccionario.items())
#claves = diccionario.values()
#print(claves)
#diccionario[1] = "one"
#print(claves)
#diccionario.pop(2)
#print(diccionario)

#type

#print(type("palabra"))
#print(type(3))
#print(type(2.3))
#print(type(True))
#print(type([]))
#print(type(()))
#print(type({0}))
#print(type({}))

#str int float bool

#variable = 3

#print(variable, type(variable))
#variable = float(variable)
#print(float("esto va a petar"))

#list tuple set dict

#list = list((1,2,3))
#tupla = tuple((1,2,3))
#conjunto = set((1,2,3))
#diccionario = dict((("uno",1),("dos", 2), ("tres", 3)))

#print(lista, type(lista))
#print(tupla, type(tupla))
#print(conjunto, type(conjunto))
#print(diccionario, type(diccionario))

#print(list("deletrea"))
#print(dict(uno=1, dos=2, tres=3))

#len sorted

#lista = [2,1,4,3]
#diccionario = {"clave_2": "valor_1", "clave_2": "valor_2"}

#print("el tamaño de la lista es:", len(lista))
#print("el tamaño del diccionario es:", len(diccionario))

#print("lista ordenada", sorted(lista))
#print("lista ordenada inversa:", sorted(lista, reverse=True))


# range enamurate zip

#print(list(range(2, 5)))

#print(list(enumerate(["uno", "dos", "tres"], start=2)))

#print(list(zip([1,2,3], ["uno", "dos", "tres"])))

#pokemon

def eligePokemon():
    bola = int(input("¿Que Pokemon Quieres?"))
    if bola == 1 :
        print("Has elegido a bulbasaur")
    if bola == 2 :
        print("Has elegido a Charmander")
    if bola == 3 :
        print("Has elegido a Squirtle")

eligePokemon()