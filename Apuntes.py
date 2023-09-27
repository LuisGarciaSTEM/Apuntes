
"""
Todo lo que vaya dentro de las triples comillas va a ir comentado
Y todo esto no se va a ver tienes que abrir y cerrarlo
"""

# Apuntes # = Para poner comentarios pero si pones
# \n = Salto de linea
# \t = Tabulación
# \\ = Para que salga la barra\
# \ = Una barra sola anula el salto de linea
# modulo% = es el resto de la división
# nombre = input("sirve para preguntar por pantalla")
#          siempre guarda el valor introducido a String.
#          Si queremos que sea un int hay que transformarlo.
#          int(input("sirve para preguntar por pantalla"))
# Para saber el tipo de algo -> print(type(numero))  
# Existen 2 tipos de (=) 
#   =  -> Asigna lo que hay ala izquierda a lo de la derecha
#         Ej. numero = 5    
#   == -> Es un igual LOGICO. ¡Compara los valores que tiene izq y drc!
#         Devuelve true, si son iguales; o false si son distintos.


"""
#Crear una variable con texto -> String
nombre = "Luis"
numero = 8
print(nombre)
print("Sumo nombre + numero")
print('print ("Luis"+"8"):')
print("Luis" + "8")
print(nombre + str(numero))
print("Escribo 10 veces CuCu con el '*'")
print("CuCu"*10)

#Hacemos operaciones matemáticas    
print("\nHacemos operaciones matemáticas")
num1 = 2
num2 = 8
suma = num1+num2
resta = num2-num1
multi = num1*num2
div = num2/num1
modulo = num1%num2
print("La suma es = " + str(suma) + " | La resta es = " + str(resta) +
      "\ | La multiplicacion es = " + str(multi) + " | La division es = " + str(div))
print(resta)
print ("Modulo es = " +str(modulo))
"""

"""
#Solicitar cosas por pantalla String/Integer
nombre = input("Dime tu nombre: ")
print("Hola " + nombre)
print("Vamos a dividir números !!!!")
num1 = int(input("Dime el primer número a dividir: "))
"""

"""
#Condicionales if/else. Ej:
#El else siempre tiene que ir detras de un if, no puede haber nada en medio.
#Debajo del if/else tiene que tener una tab para indicar donde se abre/cierra
#Que no se te olviden los : detras, y las condiciones del if/else pueden ir
#entre() aunque no se deba.
#Para concatenar if/else se usa = elif y que no se olvide los 2 puntos.
nota = int(input("¿Qué nota has sacado?"))
comprobarNota = (nota >=5 and nota<=10)
if(comprobarNota):
    print("¡Enhorabuena has aprobado!")
elif(comprobarNota > 11): 
    print("Esa nota no se puede sacar !!!! ")
else(comprobarNota):
    print("LO SIENTO ¡Has suspendido!")
"""


#Funciones.

#num1, num2, num3 son argumentos de entrada.
#resultado son argumentos de salida
def mediaTresNumeros(num1, num2, num3):
    resultado = (num1+num2+num3)/3
    #print(resultado)#No se puede poner un print dentro de una función.
    return resultado #Return devuelve el resultado
def otraMediaTresNumeros(num1, num2, num3):
    suma = (num1+num2+num3)
    return suma/3
def otraOtraMediaTresNumeros(num1, num2, num3):
    return (num1+num2+num3)/3
#--------------------------------------------------------------------
#  Código principal - MAIN.
print ("Probando funcion: ")
a = 1
b = 2
c = 3
media = mediaTresNumeros(a,b,c)
print (media)
media = mediaTresNumeros(20,30,40) #El 20, 30, 40 = num1, num2, num3.
print (media) #media es la variable que hemos creado para mostrarla.

print (mediaTresNumeros(1,2,3))
print (otraMediaTresNumeros(1,2,3))
print (otraOtraMediaTresNumeros(1,2,3))



#Ejercicio: Nombre funcion -> programarla
nombre = input("Dime tu nombre: ")
edad = int(input("Dime tu edad: "))

print (presentacion(nombre, edad))


def presentacion(nombre, edad):
    if (edad < 0):
        print ("NO puedes tener edad si no has nacido")
   
    return("Tu nombre es: " + nombre + " y tu edad son " + str(edad) + " años")







