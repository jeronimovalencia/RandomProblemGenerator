import numpy as np
import random as rdm
from scipy.stats import binom

def RandomProblemGenerator(i):


	#Seccion 3.3


	if i==1:
		#Dados: 3.22
		pos=rdm.randint(1,6)
		lista=[4,6,8,10,12,20]		
		cant=lista[pos-1]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Lanzar dados"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		pregunta += "Un dado balanceado de "+str(cant)+" caras se lanza una vez. Sea X el número en su cara superior. ¿Cuál de las siguientes opciones es cierta sobre la variable aleatoria X?"+"\n"	
		muReal=0
		muError=0
		sigmaReal=0
		sigmaError=0
		for i in range(1,cant+1):
			muReal+=(i*1.0)/cant
			muError+=i
		for i in range(1,cant+1 ):
			sigmaReal+=(i*1.0-muReal)**2/cant
			sigmaError+=(i*1.0)**2/cant
		print(" ")
		if pos%2==0:
			respuestas += "a. El valor esperado es "+str(round(muReal,2))+" y la varianza es "+str(round(sigmaError,2))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. El valor esperado es "+str(round(muReal,2))+" y la varianza es "+str(round(sigmaReal,2))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. El valor esperado es "+str(round(muError,2))+" y la varianza es "+str(round(sigmaError,2))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. El valor esperado es "+str(round(muError,2))+" y la varianza es "+str(round(sigmaReal,2))+"\n"

		elif pos%2==1:
			respuestas += "a. El valor esperado es "+str(round(muError,2))+" y la varianza es "+str(round(sigmaReal,2))+"\n"
			respuestas += " "+"\n"
			respuestas +="b. El valor esperado es "+str(round(muError,2))+" y la varianza es "+str(round(sigmaError,2))+"\n"
			respuestas += " "+"\n"
			respuestas +="c. El valor esperado es "+str(round(muReal,2))+" y la varianza es "+str(round(sigmaError,2))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. El valor esperado es "+str(round(muReal,2))+" y la varianza es "+str(round(sigmaReal,2))+"\n"

		return [titulo, version, pregunta, respuestas]

	elif i==2:
		#Cartas: 3.23
		#Al menos dos opciones por lista para que quede bien el texto de la pregunta
		lista=[[["J","Q"],["K","As"]],[["9","10","J"],["Q","K"]],[["As","2","3"],["J","Q","K"]]]
		pos=rdm.randint(1,len(lista))				
		opcion=lista[pos-1]
		titulo = ""
		version = ""
		respuestas = ""
		titulo += "Title: Lanzar dados"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		val1 = rdm.randint(10,20)
		val2 = rdm.randint(5,10)
		val3 = rdm.randint(1,5)
		lista1 = opcion[0]
		lista2 = opcion[1]
		pregunta = "En un juego de azar, una persona saca una sola carta de una baraja ordinaria de 52 cartas. A la persona le pagan \$"+str(val1)+" por sacar "
		for i in range(0,len(lista1)):
			if i==len(lista1)-1:
				pregunta += " y " + str(lista1[i])
			elif i==len(lista1)-2:
				pregunta += str(lista1[i])
			else: 
				pregunta += str(lista1[i]) + ", "
				
		pregunta += ", \$"+str(val2)+" por sacar "
		for i in range(0,len(lista2)):
			if i==len(lista2)-1:
				pregunta += " y " + str(lista2[i])
			elif i==len(lista2)-2:
				pregunta += str(lista2[i])
			else:
				pregunta += str(lista2[i]) + ", "
		
		pregunta+=", y \$"+str(val3)+" por sacar cualquier otra carta. La ganancia esperada en este juego es "+"\n"
		
		muReal = 0.0
		muError1 = 0.0
		muError2 = 0.0
		muError3 = 0.0
		
		muReal = (1/52)*(4*len(lista1)*val1+4*len(lista2)*val2+(52-4*len(lista1)-4*len(lista2))*val3)
		muError1 = (1/52)*(len(lista1)*val1+len(lista2)*val2+(52-len(lista1)-len(lista2))*val3)
		muError2 = (1/52)*(val1+val2+(52-4*len(lista1)-4*len(lista2))*val3)
		muError3 = (1/52)*(4*len(lista1)*val1+4*len(lista2)*val2+(52)*val3)		

		if pos%2==0:
			respuestas += "*a. \$"+str(round(muReal,2))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. \$"+str(round(muError1,2))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. \$"+str(round(muError2,2))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. \$"+str(round(muError3,2))+"\n"

		else:
			respuestas += "a. \$"+str(round(muError3,2))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. \$"+str(round(muError1,2))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. \$"+str(round(muReal,2))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. \$"+str(round(muError2,2))+"\n"

		return [titulo, version, pregunta, respuestas]



	#Seccion 3.4


	elif i==3:
		#Examen Opcion Multiple : 3.41
		lista=[10,12,14,16,18,20]
		pos=rdm.randint(1,len(lista))				
		cant=lista[pos-1]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Examen de Opción Múltiple"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		numOpciones = rdm.randint(3,5)
		parar=False
		while parar==False:
			cantRespuestas = rdm.randint(8,16)
			if cantRespuestas < cant:
				parar=True
		pregunta += "Un examen de opción múltiple tiene "+str(cant)+" preguntas, cada una con "+str(numOpciones)+" posibles respuestas, con una sola correcta. Suponga que un alumno contesta el examen con una adivinación aleatoria independiente en cada pregunta. ¿Cuál es la probabilidad de que conteste bien al menos "+str(cantRespuestas)+" preguntas correctamente?"+"\n"

		pReal = 1 - binom.cdf(cantRespuestas-1, cant, 1/numOpciones)
		pError1 = binom.cdf(cantRespuestas-1, cant, 1/numOpciones) 
		pError2 = 1 - binom.cdf(cantRespuestas, cant, 1/numOpciones)
		pError3 = 1 - binom.cdf(cantRespuestas-1, cant, 1/cant)
		
		cifras=7

		if pos%2==0:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError3,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]


	elif i==4:
		#Ventas con devolución: 3.59
		lista=[[5,"motores"],[7,"estéreos"],[9,"celulares"],[10,"teclados"]]
		pos=rdm.randint(1,len(lista))				
		params=lista[pos-1]
		cantProductos = params[0]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Venta de "+str(params[1])+" con devolución"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		precio = rdm.randint(1,5)*100
		dev = rdm.randint(10,20)/10
		#Esto podría variarse
		p = 0.05
		pregunta += str(params[0])+" "+str(params[1])+" se van a vender en un almacen a \$"+str(precio)+" cada uno. El almacen tiene una política de devolución de "+str(dev)+" veces el valor pagado en caso que el producto esté defectuoso. Uno de los "+str(params[1])+" tiene un defecto con probabilidad "+str(p)+". La ganancia neta esperada por el almacen tras vender todos los productos es"+"\n"

		gananciaReal = 0.0 
		gananciaError1 = 0.0 
		gananciaError2 = 0.0
		gananciaError3 = 0.0

		for i in range(cantProductos+1):
			gananciaReal += (cantProductos*precio-i*(dev-1)*precio)*binom.pmf(i,cantProductos,p)
			gananciaError1 += (cantProductos*precio-i*(dev)*precio)*binom.pmf(i,cantProductos,p)
			gananciaError2 += (cantProductos*precio)*binom.pmf(i,cantProductos,p)
			gananciaError3 += (cantProductos*precio-i*(dev-1)*precio)*binom.pmf(i,cantProductos,1-p)

		cifras=0

		if pos%2==0:
			respuestas += "a. \$"+str(round(gananciaError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. \$"+str(round(gananciaError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. \$"+str(round(gananciaError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. \$"+str(round(gananciaReal,cifras))+"\n"
		else:
			respuestas += "*a. \$"+str(round(gananciaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. \$"+str(round(gananciaError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. \$"+str(round(gananciaError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. \$"+str(round(gananciaError2,cifras))+"\n"

		return [titulo, version, pregunta, respuestas]
	

	#Sección 3.5
	

	elif i==5: 
		#Geométrica sin memoria: 3.72
		lista = [0.1,0.2,0.3,0.4,0.5,0.6]
		pos=rdm.randint(1,len(lista))				
		p=lista[pos-1]	
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Moneda no justa"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		cant1 = rdm.randint(10,100)
		cant2 = rdm.randint(2,5)
		
		pregunta += "Suponga que se tiene una moneda con probabilidad de obtener cara de "+str(p)+". Si ésta se lanza "+str(cant1)+" veces y no se obtiene cara, ¿cuál es la probabilidad de que al lanzarla al menos "+str(cant2)+" veces más se obtenga la primera cara?"+"\n"

		pReal = (1-p)**(cant2-1)
		pError1 = p**(cant2)	
		pError2 = (1-p**cant2)
		pError3 = (1-p)**cant2

		cifras=4

		if pos%2==0:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError3,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]


	elif i==6: 
		#Preferencia de marca: 3.77
		lista = ["par","impar"]	
		pos=rdm.randint(1,len(lista))				
		paridad=lista[pos-1]	
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Probabilidad total geométrica"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		
		pregunta+="Sea X una variable aleatoria con distribución de probabilidad geométrica con probabilidad de éxito $p$. La probabilidad que X sea cualquier número "+paridad+" es (acá, $q=1-p$)"+"\n"

		pPar = "$\ "+"frac{p}{q-q^3}$" 
		pPar = pPar.replace(" ","")
		pImpar = "$\ "+"frac{p}{1-q^2}$"
		pImpar = pImpar.replace(" ","")
		pError1 = "$\ "+"frac{q}{1-p}$"
		pError1 = pError1.replace(" ","")
		pError2 = "$\ "+"frac{q}{1-p^2}$"
		pError2 = pError2.replace(" ","")
		
		if pos%2==0:
			respuestas += "a. "+pPar+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+pImpar+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+pError1+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+pError2+"\n"

		else:
			respuestas += "*a. "+pPar+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+pImpar+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+pError1+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+pError2+"\n"
		
		return [titulo, version, pregunta, respuestas]
	
	elif i==7: 
		#Moneda no justa: 3.81
		lista = [0.05,0.1,0.4,0.8]
		pos=rdm.randint(1,len(lista))			
		p = lista[pos-1]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Moneda con probabilidad de cara p="+str(p)+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		pregunta += "Suponga que tiene una moneda no justa con una probabilidad de obtener cara de "+str(p)+". ¿Cuántas veces esperaría lanzar la moneda para obtener la primera cara?"+"\n"
		#pregunta += " "+"\n"
		cantReal = 1.0/p
		cantError1 = (1.0-p)/(p**2)
		cantError2 = (1.0-p**2)/(p**2)
		cantError3 = 1.0/(1-p**2)
		cifras=0
		if pos%2==0:
			respuestas += "a. "+str(int(round(cantError1,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(int(round(cantReal,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "c. "+str(int(round(cantError3,cifras)))+"\n"
			respuestas += " "+"\n"		
			respuestas += "d. "+str(int(round(cantError2,cifras)))+"\n"

		else:
			respuestas += "*a. "+str(int(round(cantReal,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "b. "+str(int(round(cantError2,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(int(round(cantError3,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(int(round(cantError1,cifras)))+"\n"

		return [titulo, version, pregunta, respuestas]

	#Sección 3.6

	elif i==8:
		#

#TODO
#Pedir en consola cantidad y rango (secciones) de los ejercicios a imprimir.


#Escribir documento en .tex

print("\documentclass{article}")

str0 = "\ "+"usepackage[utf8]{inputenc}"
print(str0.replace(" ", ""))
str01 = "\ "+"usepackage{enumitem,amsmath}"
print(str01.replace(" ", ""))

#Encabezado
#str1 = "\ "+"title{Random Exercises}"
#print(str1.replace(" ", ""))
#str2 = "\ "+"author{Jerónimo Valencia Porras}"
#print(str2.replace(" ",""))
#print("\date{July 2020}")


str3 = "\ "+"begin{document}"
print(str3.replace(" ",""))

#print("\maketitle")

#TODO: Configurar esto con la entrada del TODO anterior

ejercicios = [5,6]

str4 = "\ "+"begin{enumerate}[label=\ "+"arabic"+"*]"
print(str4.replace(" ",""))

for i in ejercicios: 
	data = RandomProblemGenerator(i)
	#Titulo y version del problema
	#print(data[0])
	#print(data[1])
	print("\item "+data[2])
	print(data[3])

print("\end{enumerate}")

print("\end{document}")
















