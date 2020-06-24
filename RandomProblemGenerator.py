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
		print("Title: Lanzar dados")
		print("%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos))
		print("Un dado balanceado de "+str(cant)+" caras se lanza una vez. Sea X el número en su cara superior. ¿Cuál de las siguientes opciones es cierta sobre la variable aleatoria X?")		
		muReal=0
		muError=0
		sigmaReal=0
		sigmaError=0
		for i in range(1,cant+1):
			muReal+=(i*1.0)/cant
			muError+=(cant)/(i*1.0)
		for i in range(1,cant+1 ):
			sigmaReal+=(i*1.0-muReal)**2/cant
			sigmaError+=(i*1.0)**2/cant
		print(" ")
		if pos%2==0:
			print("a. El valor esperado es "+str(round(muReal,2))+" y la varianza es "+str(round(sigmaError,2)))
			print("*b. El valor esperado es "+str(round(muReal,2))+" y la varianza es "+str(round(sigmaReal,2)))
			print("c. El valor esperado es "+str(round(muError,2))+" y la varianza es "+str(round(sigmaError,2)))
			print("d. El valor esperado es "+str(round(muError,2))+" y la varianza es "+str(round(sigmaReal,2)))

		elif pos%2==1:
			print("a. El valor esperado es "+str(round(muError,2))+" y la varianza es "+str(round(sigmaReal,2)))
			print("b. El valor esperado es "+str(round(muError,2))+" y la varianza es "+str(round(sigmaError,2)))
			print("c. El valor esperado es "+str(round(muReal,2))+" y la varianza es "+str(round(sigmaError,2)))
			print("*d. El valor esperado es "+str(round(muReal,2))+" y la varianza es "+str(round(sigmaReal,2)))

	elif i==2:
		#Cartas: 3.23
		#Al menos dos opciones por lista para que quede bien el texto de la pregunta
		lista=[[["J","Q"],["K","As"]],[["9","10","J"],["Q","K"]],[["As","2","3"],["J","Q","K"]]]
		pos=rdm.randint(1,len(lista))				
		opcion=lista[pos-1]
		print("Title: Lanzar dados")
		print("%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos))
		val1 = rdm.randint(10,20)
		val2 = rdm.randint(5,10)
		val3 = rdm.randint(1,5)
		lista1 = opcion[0]
		print(len(lista1))
		lista2 = opcion[1]
		pregunta = "En un juego de azar, una persona saca una sola carta de una baraja ordinaria de 52 cartas. A la persona le pagan $"+str(val1)+" por sacar "
		for i in range(0,len(lista1)):
			if i==len(lista1)-1:
				pregunta += " y " + str(lista1[i])
			elif i==len(lista1)-2:
				pregunta += str(lista1[i])
			else: 
				print(lista1[i])
				pregunta += str(lista1[i]) + ", "
				
		pregunta += ", $"+str(val2)+" por sacar "
		for i in range(0,len(lista2)):
			if i==len(lista2)-1:
				pregunta += " y " + str(lista2[i])
			elif i==len(lista2)-2:
				pregunta += str(lista2[i])
			else: 
				print(lista2[i])
				pregunta += str(lista2[i]) + ", "
		
		pregunta+=", y $"+str(val3)+" por sacar cualquier otra carta. La ganancia esperada en este juego es "
		print(pregunta)
		print(" ")
		
		muReal = 0.0
		muError1 = 0.0
		muError2 = 0.0
		muError3 = 0.0
		
		muReal = (1/52)*(4*len(lista1)*val1+4*len(lista2)*val2+(52-4*len(lista1)-4*len(lista2))*val3)
		muError1 = (1/52)*(len(lista1)*val1+len(lista2)*val2+(52-len(lista1)-len(lista2))*val3)
		muError2 = (1/52)*(val1+val2+(52-4*len(lista1)-4*len(lista2))*val3)
		muError3 = (1/52)*(4*len(lista1)*val1+4*len(lista2)*val2+(52)*val3)		

		if pos%2==0:
			print("*a. $"+str(round(muReal,2)))
			print("b. $"+str(round(muError1,2)))
			print("c. $"+str(round(muError2,2)))
			print("d. $"+str(round(muError3,2)))

		else:
			print("a. $"+str(round(muError3,2)))
			print("b. $"+str(round(muError1,2)))
			print("*c. $"+str(round(muReal,2)))
			print("d. $"+str(round(muError2,2)))

	#Seccion 3.4
	elif i==3:
		#Examen Opcion Multiple : 3.41
		lista=[10,12,14,16,18,20]
		pos=rdm.randint(1,len(lista))				
		cant=lista[pos-1]
		print("Title: Examen de Opción Múltiple")
		print("%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos))
		numOpciones = rdm.randint(3,5)
		parar=False
		while parar==False:
			cantRespuestas = rdm.randint(8,16)
			if cantRespuestas < cant:
				parar=True
		print("un examen de opción múltiple tiene "+str(cant)+" preguntas, cada una con "+str(numOpciones)+" posibles respuestas, con una sola correcta. Suponga que un alumno contesta el examen con una adivinación aleatoria independiente en cada pregunta. ¿Cuál es la probabilidad de que conteste bien al menos "+str(cantRespuestas)+" preguntas correctamente?")
		print(" ")

		pReal = 1 - binom.cdf(cantRespuestas-1, cant, 1/numOpciones)
		pError1 = binom.cdf(cantRespuestas-1, cant, 1/numOpciones) 
		pError2 = 1 - binom.cdf(cantRespuestas, cant, 1/numOpciones)
		pError3 = 1 - binom.cdf(cantRespuestas-1, cant, 1/cant)
		
		cifras=7

		if pos%2==0:
			print("*a. "+str(round(pReal,cifras)))
			print("b. "+str(round(pError1,cifras)))
			print("c. "+str(round(pError2,cifras)))
			print("d. "+str(round(pError3,cifras)))

		else:
			print("a. "+str(round(pError3,cifras)))
			print("b. "+str(round(pError1,cifras)))
			print("*c. "+str(round(pReal,cifras)))
			print("d. "+str(round(pError2,cifras)))

	elif i==4:
		#Ventas con devolución: 3.59
		lista=[[5,"motores"],[7,"estéreos"],[9,"celulares"],[10,"teclados"]]
		pos=rdm.randint(1,len(lista))				
		params=lista[pos-1]
		cantProductos = params[0]
		print("Title: Venta de "+str(params[1])+" con devolución")
		print("%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos))
		precio = rdm.randint(1,5)*100
		dev = rdm.randint(10,20)/10
		#Esto se puede variar for the lulz
		p = 0.05
		print(str(params[0])+" "+str(params[1])+" se van a vender en un almacen a $"+str(precio)+" cada uno. El almacen tiene una política de devolución de "+str(dev)+" veces el valor pagado en caso que el producto esté defectuoso. Uno de los "+str(params[1])+" tiene un defecto con probabilidad "+str(p)+". La ganancia neta esperada por el almacen tras vender todos los productos es")
		print(" ")
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
			print("a. $"+str(round(gananciaError1,cifras)))
			print("b. $"+str(round(gananciaError2,cifras)))
			print("c. $"+str(round(gananciaError3,cifras)))
			print("*d. $"+str(round(gananciaReal,cifras)))

		else:
			print("*a. $"+str(round(gananciaReal,cifras)))
			print("b. $"+str(round(gananciaError3,cifras)))
			print("c. $"+str(round(gananciaError1,cifras)))
			print("d. $"+str(round(gananciaError2,cifras)))



#exercise=rdm.randint(1,2)
RandomProblemGenerator(4)













