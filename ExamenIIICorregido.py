
#Funcion del largo
def largo1(matriz):
     cont=0
     for i in matriz:
          cont+=1
     return cont



#Problema 1
#Escriba un programa con sintaxis Python cuya función principal se llame
#construir_digitos(lista), que reciba como entrada una lista con sublistas que contiene dígitos
#enteros positivos incluyendo el cero, y debe retornar una lista de números formados a partir
#cada sublista. Se debe omitir aquellos dígitos que sean impares. 

def validacion_enteros_positivos(lista):
     cont=0
     for i in lista:
          if i==[]:
               cont+=1
               break
          for k in i:
               if isinstance(k,str):
                    cont+=1
                    break
               else:
                    if isinstance(k,int):
                         if k<0:
                              cont+=1
                              break
                    else:
                         cont+=1
                         break
     if cont>0:
          return False
     else:
          return True

                    
def construir_digitos(matriz):
     if isinstance(matriz,list) :
          if matriz==[]:
               return "Error en la entrada, no se permite lista vacía" 
          if validacion_enteros_positivos(matriz)==True:
               return construir_digitos_aux(matriz)
          else:
               return "La matriz tiene que estar conformada por numeros enteros mayores a 0 y diferente vacio"
     else:
          return "El paramtro de entrada tiene que ser una matriz"
def construir_digitos_aux(matriz):
     res=[]
     for i in matriz:
          temp=0
          cont=0
          for j in range(1,largo1(i)+1):
               if (i[-j]%2==0):
                    temp+=i[-j]*10**cont
                    cont+=1
          res+=[temp]
     return res
print("problema 1")
print("Opereaciones a evaluar")
print("1-[[2,3], [6,7,5,6], [5,5,3,3], [8, 1, 1]] .","resultado:",construir_digitos( [[2,3], [6,7,5,6], [5,5,3,3], [8, 1, 1]] ),"Respuesta correcta [2, 66, 0, 8]") 
print("2-([[1,5], [2,9], [6,0], [0,0,0,1]]).","resultado:",construir_digitos ([[1,5], [2,9], [6,0], [0,0,0,1]]),"Respuesta correcta [0, 2, 60, 0] " )
print("3- ([]).","resultado:",construir_digitos ([]) )


#Problema2
#Escriba una función en Python llamada es_computable(num), que recibe un número entero
#positivo mayor que cero. La función debe indicar si el número es Computable o no. Un
#número es Computable si cumple con lo siguiente:
# En el número ingresado el dígito ubicado en la máxima potencia sea divisible por el
#dígito en la mínima potencia (unidad).
# En la representación en sistema octal (base 8) del número ingresado, la cantidad de
#dígitos pares sean mayor a sus impares. 
def largo(num):
     cont=0
     while num!=0:
          cont+=1
          num=num//10
     return cont
def es_computable(num):
     if isinstance(num,int) and num>=0:
          ultimoDigito=num%10
          primerDigito=(num//10**(largo(num)-1))
          if primerDigito%ultimoDigito==0:
               return computable_aux(num)
          else:
               return False
     else:
          print("Error en paramtros de entrada")
def computable_aux(numero):
     potencia=0
     nuevoNumero=0
     while numero!=0:
          nuevoNumero+= (numero%8) * (10**potencia)
          numero=numero//8
          potencia+=1
     return validar(nuevoNumero)
def validar(resultado):
     pares=[]
     impares=[]
     num=resultado
     while num!=0:
          if (num%10)%2==0:
               pares+=[num%10]
               num=num//10
          else:
               impares+=[num%10]
               num=num//10
     if largo1(pares) > largo1(impares):
          return True
     else:
          return False
print("--------------------------------------------------------------------------")
print("Problema2")
print("Opereciones a evaluar")
print("1-84361","Resultado:",es_computable(84361),",","Resultado correcto True")
print("2-8124","Resultado:",es_computable(8124),",","Resultado correcto False")
print("3-28489","Resultado:",es_computable(28489),",","Resultado correcto False")
print("4-393","Resultado:",es_computable(393),",","Resultado correcto False")

#-----------------------------------------------------------
#Problema 3
#Escriba una solución con sintaxis Python cuya función principal se llame
#matriz_seminula(matriz), recibe como parámetro de entrada una matriz cuadrada, de
#tamaño impar, donde la cantidad de mínima de filas y columnas debe ser 5, y devolverá True
#en caso de que todos los valores internos de la matriz son ceros y que los valores del borde
#de la matriz deben ser pares, False en caso de que al menos un valor interno o los bordes
#cumpla con las restricciones. Los valores internos son aquellos en posiciones que no están
#en el “borde” de la matriz. Puede asumir la existencia de una función validaMatriz(matriz)
#que retorna True si la entrada es una matriz válida. No puede descomponer la matriz de
#entrada.
def validacion_enteros_positivos(lista):
     cont=0
     for i in lista:
          if i==[]:
               cont+=1
               break
          for k in i:
               if isinstance(k,str):
                    cont+=1
                    break
               else:
                    if isinstance(k,int):
                         if k<0:
                              cont+=1
                              break
                    else:
                         cont+=1
                         break
     if cont>0:
          return False
     else:
          return True
def validarColumas(matriz):
     validar=0
     cont=0
     for i in matriz:
          for j in i:
               cont+=1
          if cont<5:
               validar+=1
               break
          else:
               cont=0
          
     if validar>0:
          return False
     else:
          return True
def validarMatriz(matriz):
     filas=0
     for i in matriz:
          filas+=1
     columnas=0
     for i in matriz:
          for j in i:
               columnas+=1
          if columnas!=filas:
               return False
          columnas=0
     return True
               
          

def matriz_seminula(matriz):
     if isinstance(matriz,list):
          if matriz==[]:
               return "Error en la entrada, no se permite lista vacía"
          else:
               if validacion_enteros_positivos(matriz)==True:
                    if largo1(matriz)<5 or validarColumas(matriz)==False:
                         return "La matriz tiene que tener un largo minimo de 5x5"
                    else:
                         if largo1(matriz)%2!=0:
                              if validarMatriz(matriz)==True:
                                   return matriz_seminula_aux(matriz)
                              else:
                                   return "No es una matriz cuadrada"
                         else:
                              return "El largo de la matriz tiene que ser impar"
                    
                    return matriz_seminula_aux(matriz)
               else:
                    return "La matriz tiene que estar conformada por numeros enteros mayores a 0 y diferente vacio"
                    
     else:
          return "El parametro de entrada tiene que ser una matriz"
def matriz_seminula_aux(matriz):
     for i in range(largo1(matriz)):
          for j in range(largo1(matriz[i])):
               if (i>0 and i<largo1(matriz)-1) and j>0 and j<largo1(matriz[i])-1:
                   
                   if (matriz[i][j]!=0):
                        return False
               else:
                    if (matriz[i][j]%2!=0):
                         return False
     return True
print("-----------------------------------------------------------------------------------")
print("Problema3")
print("Opereaciones a evaluar")
print("1-matriz=[[9,2,8,0,4],[6,0,0,0,6],[4,0,0,0,30],[0,0,0,0,18],[50,6,8,92,190]]",",","Resultado:", matriz_seminula([[9,2,8,0,4],[6,0,0,0,6],[4,0,0,0,30],[0,0,0,0,18],[50,6,8,92,190]]),",","Resultado correcto :False")
print("2-matriz=[[4,2,8,0,4],[6,0,0,0,6],[4,0,0,0,30],[0,0,0,0,18],[50,6,8,92,190]]",",","Resultado:", matriz_seminula([[4,2,8,0,4],[6,0,0,0,6],[4,0,0,0,30],[0,0,0,0,18],[50,6,8,92,190]]),",","Resultado correcto :True")
print("3-matriz=[[4,2,8,0,4],[6,0,0,0,6],[4,0,0,0,3],[0,0,0,0,18],[50,6,8,92,190]]",",","Resultado:", matriz_seminula([[9,2,8,0,4],[6,0,0,0,6],[4,0,0,0,3],[0,0,0,0,18],[50,6,8,92,190]]),",","Resultado correcto :False")                   
print("La funcion puede ser probada con matrices cuadras mayores a 5x5")  





#------------------------------------------------------------------
#Problema 4
#Escriba una solución con sintaxis Python cuya función principal se llame
#profundidadMatriz(matriz), el parámetro de entrada es una matriz especial ya que el
#contenido de cada vector será listas de un solo atributo, que estas a su vez puede ser una
#lista o solo un dígito. Objetivo es mapear la profundidad de cada índice de la matriz e imprimir
#el nivel de profundidad.      
def profundidad(lista,dato,cont):
     if (not isinstance(lista,list) or lista==[]):
          if lista==[]:
               cont+=1
          if dato[0]<cont:
               dato[0]=cont
          return None
     profundidad(lista[0],dato,cont+1)
     profundidad(lista[1:],dato,cont)
def profu(lista):
     dato=[0]
     profundidad(lista,dato,0)
     return dato[0]
def profundidadMatriz(matriz):
     if isinstance(matriz,list):
          res=[]
          for i in matriz:
               resultado=[]
               for j in i :
                    resultado+=[profu(j)]
               res+=[resultado]
          return res
     else:
          return "El parametro de entrada tiene que ser una matriz"
print("---------------------------------------------------------------------------------")
print("Problema4")
print("1- profundidadMatriz ([ [ [[]], [], 6 ], [ [[[[1]]]], 10, [] ], [ [[3]], [[[]]], 0 ] ]) ",",","Resultado:", profundidadMatriz ([ [ [[]], [], 6 ], [ [[[[1]]]], 10, [] ], [ [[3]], [[[]]], 0 ] ]) )
print("1- profundidadMatriz ([ [ [[]], [], 6 ], [ [[[[1]]]], [[10]], [] ], [ [[3]], [[[]]], 0 ] ]) ",",","Resultado:", profundidadMatriz ([ [ [[]], [], 6 ], [ [[[[1]]]], [[10]], [] ], [ [[3]], [[[]]], 0 ] ]) )

















#problema 4



     
