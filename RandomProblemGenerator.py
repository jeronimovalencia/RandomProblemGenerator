import numpy as np
import random as rdm
import math
from scipy.stats import binom
from scipy.stats import geom
from scipy.stats import poisson

from scipy.special import binom as bin_coeff

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

	elif i==3:
		#Ganancias diarias: 3.26
		#[Cantidad 1 de clientes a llamar, cantidad 2 de clientes a llamar, Probab de llamar a cada grupo de clientes, probab de hacer una venta, precio venta]
		lista=[[2,4,0.4,0.2,50000],[4,5,0.6,0.1,100000],[5,7,0.45,0.25,10000],[3,10,0.3,0.05,1000000]]
		pos=rdm.randint(1,len(lista))				
		params=lista[pos-1]
		n1 = params[0]
		n2 = params[1]
		pCliente = params[2]
		pVenta = params[3]
		precioVenta = params[4]
		stringPrecioVenta = "{:,}".format(precioVenta)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Ganancias diarias"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		
		pregunta += "Un vendedor puede llamar a "+str(n1)+" o "+str(n2)+" clientes, con probabilidad "+str(pCliente)+" y "+str(1-pCliente)+" respectivamente. En cada llamada, hay una probabilidad de "+str(pVenta)+" de realizar una venta de \$"+stringPrecioVenta+". ¿Cuál es la ganancia diaria media de este vendedor?"+"\n"

		gananciaPorLlamada = pVenta*precioVenta		

		gananciaReal = (pCliente*n1+(1-pCliente)*n2)*gananciaPorLlamada
		STRgananciaReal = "{:,}".format(int(gananciaReal))
		gananciaError1 = (n1+n2)*gananciaPorLlamada
		STRgananciaError1 = "{:,}".format(int(gananciaError1))
		gananciaError2 = (n1+n2)*gananciaPorLlamada*pCliente
		STRgananciaError2 = "{:,}".format(int(gananciaError2))
		gananciaError3 = (n1+n2)*gananciaPorLlamada*(1-pCliente)
		STRgananciaError3 = "{:,}".format(int(gananciaError3))

		if pos%2==0:
			respuestas += "a. \$"+STRgananciaError3+"\n"
			respuestas += " "+"\n"
			respuestas += "b. \$"+STRgananciaError1+"\n"
			respuestas += " "+"\n"
			respuestas += "c. \$"+STRgananciaError2+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. \$"+STRgananciaReal+"\n"

		else:
			respuestas += "a. \$"+STRgananciaError1+"\n"
			respuestas += " "+"\n"
			respuestas += "b. \$"+STRgananciaError2+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. \$"+STRgananciaReal+"\n"
			respuestas += " "+"\n"
			respuestas += "d. \$"+STRgananciaError3+"\n"

		return [titulo, version, pregunta, respuestas]
		
	#Seccion 3.4

	elif i==4:
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


	elif i==5:
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
	

	elif i==6: 
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


	elif i==7: 
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
	
	elif i==8: 
		#Preferencia de marca : 3.78
		#[probabilidad de preferencia, tipo de artículo, cantidad minima de personas que se quieren con la preferencia]		
		lista = [[70,"chocolates",5],[80,"cervezas",6],[90,"galletas",5],[85,"dulces",4]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pPreferencia = params[0]/100
		articulo = params[1]
		cantMinimaPersonas = params[2]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Encuesta de preferencia de marca"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "De una ciudad, se sabe que el "+str(params[0])+"\% de la población prefieren una cierta marca de "+articulo+". Si se hace una encuesta con ciudadanos al azar, ¿cuál es la probabilidad que al menos "+str(cantMinimaPersonas)+" personas deban ser entrevistadas para que se encuentre la primera persona con la preferencia de tal marca?"+"\n"

		pReal = 1- geom.cdf(cantMinimaPersonas-1,pPreferencia)
		pError1 = 1- geom.cdf(cantMinimaPersonas,pPreferencia)
		pError2 = geom.cdf(cantMinimaPersonas-1,pPreferencia)
		pError3 = geom.pmf(cantMinimaPersonas,pPreferencia)

		cifras=7

		if pos%2==0:
			respuestas += "a. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError1,cifras))+"\n"

		else:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError3,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	
	elif i==9: 
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


	elif i==10:
		#Artículos defectuosos: 3.92
		#[Porcentaje de falla, nombre artículo, número de articulo defectuoso, texto anterior ,número de intento, texto anterior] con numDefecto < numIntentos 
		lista = [[5,"pantalla",2,"segunda",3,"tercero"],[10,"vela",1,"primera",3,"tercero"],[2,"computadora",2,"segunda",5,"quinto"],[7,"silla",3,"tercera",4,"cuarto"],[8,"estufa",1,"primera",5,"quinto"]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pFallo = params[0]/100
		articulo = params[1]
		numNoDefectos = params[2]
		numIntentos = params[4]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Errores de producción de "+articulo+"s"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += str(params[0])+" por ciento de las "+articulo+"s fabricadas por una empresa son defectuosas. Si estos artículos se prueban al azar uno a la vez, ¿cuál es la probabilidad de que la "+params[3]+" "+articulo+" no defectuosa sea hallada en el "+params[5]+" intento?"+"\n"

		p = pFallo
		q = 1-p
		pReal = bin_coeff(numIntentos-1,numNoDefectos-1)*q**numNoDefectos*p**(numIntentos-numNoDefectos)
		pError1 = bin_coeff(numIntentos-1,numNoDefectos-1)*p**numNoDefectos*q**(numIntentos-numNoDefectos)
		pError2 = bin_coeff(numIntentos,numNoDefectos)*p**numNoDefectos*q**(numIntentos-numNoDefectos)
		pError3 = bin_coeff(numIntentos,numNoDefectos)*q**numNoDefectos*p**(numIntentos-numNoDefectos)

		cifras=7

		if pos%2==0:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"

		else:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	elif i==11:
		#Cantidad media de tréboles: 3.97
		
		lista = [[0.1,6],[0.2,5],[0.05,4],[0.15,7]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		p = params[0]
		cant = params[1]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Encontrar tréboles de 4 hojas"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "En un cierto prado, la probabilidad de encontrar un trébol de cuatro hojas es "+str(p)+". ¿Cuántos tréboles deberían buscarse para hallar "+str(cant)+" de cuatro hojas?"+"\n"

		cantReal = cant/p
		cantError1 = 1/p 
		cantError2 = cant/p**2
		cantError3 = 100*p/cant

		cifras=0
		if pos%2==0:
			respuestas += "a. "+str(int(round(cantError3,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(int(round(cantReal,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "c. "+str(int(round(cantError2,cifras)))+"\n"
			respuestas += " "+"\n"		
			respuestas += "d. "+str(int(round(cantError1,cifras)))+"\n"

		else:
			respuestas += "a. "+str(int(round(cantError3,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "b. "+str(int(round(cantError1,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(int(round(cantReal,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(int(round(cantError2,cifras)))+"\n"

		return [titulo, version, pregunta, respuestas] 	

			
	#Sección 3.7

	
	elif i==12: 
		#Canicas de colores: 3.102
		#[Número total de canicas, num canicas amarillas, num canicas azules, cantidad sacadas, cantidad deseada azul]
		lista = [[10,2,4,5,2],[15,5,5,6,3],[15,8,4,4,4],[20,10,5,10,3]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		numTotalCanicas = params[0]
		numCanicasA = params[1]
		numCanicasZ = params[2]
		numCanicasR = numTotalCanicas - numCanicasA - numCanicasZ
		cantSacadas = params[3]
		cantDeseadaZ = params[4]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Canicas de colores"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "Suponga que en una bolsa hay "+str(numTotalCanicas)+" canicas de las cuales "+str(numCanicasA)+" son amarillas, "+str(numCanicasZ)+" son azules y "+str(numCanicasR)+" son rojas. Si se sacan "+str(cantSacadas)+" canicas al azar sin reemplazo, ¿cuál es la probabilidad que "+str(cantDeseadaZ)+ " sean azules?"+"\n"

		pReal = bin_coeff(numCanicasZ,cantDeseadaZ)*bin_coeff(numTotalCanicas-numCanicasZ,cantSacadas-cantDeseadaZ)/bin_coeff(numTotalCanicas,cantSacadas)
		pError1 = 1/bin_coeff(numTotalCanicas,cantDeseadaZ)
		pError2 = bin_coeff(numCanicasZ,cantDeseadaZ)*bin_coeff(numTotalCanicas-numCanicasZ,cantSacadas)/bin_coeff(numTotalCanicas,cantSacadas)
		pError3 =  1/bin_coeff(numCanicasZ,cantDeseadaZ)
		
		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError3,cifras))+"\n"

		else:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError1,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	
	elif i==13:
		#Flores blancas y rojas : 3.114
		#[Tamaño ramo, cantidad total flores, cantidad flores rojas del total]
		lista = [[10,100,50],[25,200,150],[15,150,60],[20,300,175],[30,200,120]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		tamRamo = params[0]
		cantTotalFlores = params[1]
		numFloresR = params[2]
		numFloresB = cantTotalFlores-numFloresR
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Ramos de flores"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "Un ramo de "+str(tamRamo)+" flores se va a crear a partir de un lote con "+str(numFloresB)+" flores blancas y "+str(numFloresR)+" flores rojas. ¿Cuántas flores "+"blancas"+" esperaría ver en el ramo completo?"+"\n"

		cantReal = tamRamo*numFloresB/cantTotalFlores 
		cantError1 = tamRamo*numFloresR/cantTotalFlores
		cantError2 = numFloresB/tamRamo
		cantError3 = (tamRamo*numFloresB/cantTotalFlores)*((cantTotalFlores-numFloresB)/cantTotalFlores)

		cifras=0
		if pos%2==0:
			respuestas += "*a. "+str(int(round(cantReal,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(int(round(cantError3,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "c. "+str(int(round(cantError2,cifras)))+"\n"
			respuestas += " "+"\n"		
			respuestas += "d. "+str(int(round(cantError1,cifras)))+"\n"

		else:
			respuestas += "*a. "+str(int(round(cantReal,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "b. "+str(int(round(cantError1,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(int(round(cantError2,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(int(round(cantError3,cifras)))+"\n"

		return [titulo, version, pregunta, respuestas] 

	elif i==14:
		#Costo de reparación: 3.106
		#[Nombre artículo, cantidad total articulos, cantidad articulos defectuosos, costo reparación, tamaño del muestreo]
		lista = [["celulares",100,15,100000,10], ["computadores",20,5,150000,5], ["esferos",200,25,10000,16], ["pantalones",50,12,20000,8]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		articulos = params[0]
		cantTotalArticulos = params[1]
		cantArticulosDefectuosos = params[2]
		costoReparacionPorArticulo = params[3]
		STRcostoReparacionPorArticulo = "{:,}".format(costoReparacionPorArticulo)
		tamMuestra = params[4]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Costo medio de reparación"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "En una bodega hay "+str(cantTotalArticulos)+" "+articulos+" de los cuales "+str(cantArticulosDefectuosos)+" están defectuosos. El costo de reparar un artículo defectuoso es de \$"+ STRcostoReparacionPorArticulo +". Si se seleccionan "+ str(tamMuestra) +" artículos al azar para formar un lote, ¿cuál es el costo medio de la reparación de este lote?"+"\n"
		
		costoReal = (tamMuestra*cantArticulosDefectuosos/cantTotalArticulos)*costoReparacionPorArticulo
		STRcostoReal = "{:,}".format(int(costoReal))
		costoError1 = (tamMuestra/cantTotalArticulos)*costoReparacionPorArticulo
		STRcostoError1 = "{:,}".format(int(costoError1))
		costoError2 = (cantArticulosDefectuosos/cantTotalArticulos)*costoReparacionPorArticulo
		STRcostoError2 = "{:,}".format(int(costoError2))
		costoError3 = tamMuestra*costoReparacionPorArticulo
		STRcostoError3 = "{:,}".format(int(costoError3))

		if pos%2==0:
			respuestas += "a. \$"+STRcostoError3+"\n"
			respuestas += " "+"\n"
			respuestas += "b. \$"+STRcostoError1+"\n"
			respuestas += " "+"\n"
			respuestas += "c. \$"+STRcostoError2+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. \$"+STRcostoReal+"\n"

		else:
			respuestas += "a. \$"+STRcostoError1+"\n"
			respuestas += " "+"\n"
			respuestas += "b. \$"+STRcostoError2+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. \$"+STRcostoReal+"\n"
			respuestas += " "+"\n"
			respuestas += "d. \$"+STRcostoError3+"\n"

		return [titulo, version, pregunta, respuestas]

	elif i==15:
		#Tamaño de muestra : 3.106
		#[Articulo, cantidad total, cantidad defectuosos,probabilidad de AL MENOS 1 defectuoso]
		lista = [["celulares",100,15,0.8], ["computadores",40,10,0.9], ["esferos",200,25,0.95], ["pantalones",50,12,0.85]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		articulos = params[0]
		cantTotalArticulos = params[1]
		cantArticulosDefectuosos = params[2]
		probabilidadAlMenosUnDefecto = params[3]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Tamaño de muestra para detectar defectos"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		
		pregunta += "Una caja con "+str(cantTotalArticulos) +" " + articulos+" contiene "+str(cantArticulosDefectuosos)+ " defectuosos. ¿Cuál debe ser el tamaño de la muestra de artículos de la caja para que la probabilidad de que haya al menos uno defectuoso sea mayor o igual a "+str(probabilidadAlMenosUnDefecto)+"?"+"\n"

		parar = False
		cont = 0
		while parar == False :
			cont += 1
			#Probabilidad de cero defectos			
			prob = bin_coeff(cantArticulosDefectuosos,0)*bin_coeff(cantTotalArticulos-cantArticulosDefectuosos,cont-0)/bin_coeff(cantTotalArticulos,cont)
			if 1-prob >= probabilidadAlMenosUnDefecto:
				parar = True

		cantReal = cont
			 
		parar = False
		cont = 0
		while parar == False :
			cont += 1			
			probError1 = bin_coeff(cantArticulosDefectuosos,1)*bin_coeff(cantTotalArticulos-cantArticulosDefectuosos,cont-1)/bin_coeff(cantTotalArticulos,cont)
			prob = bin_coeff(cantArticulosDefectuosos,0)*bin_coeff(cantTotalArticulos-cantArticulosDefectuosos,cont-0)/bin_coeff(cantTotalArticulos,cont)
			if 1-probError1 -prob >= probabilidadAlMenosUnDefecto:
				parar = True		

		cantError1 = cont
	
		cantError2 = int(cantReal*4/3)

		parar = False
		cont = 0
		while parar == False :
			cont += 1			
			probError3 = bin_coeff(cantArticulosDefectuosos,1)*bin_coeff(cantTotalArticulos-cantArticulosDefectuosos,cont-1)/bin_coeff(cantTotalArticulos,cont)
			if probError3 > 1-probabilidadAlMenosUnDefecto/1.5:
				parar = True

		cantError3 = cont
			
		cifras=0
		if pos%2==0:
			respuestas += "a. "+str(int(round(cantError2,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(int(round(cantError3,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "c. "+str(int(round(cantError1,cifras)))+"\n"
			respuestas += " "+"\n"		
			respuestas += "*d. "+str(int(round(cantReal,cifras)))+"\n"

		else:
			respuestas += "*a. "+str(int(round(cantReal,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "b. "+str(int(round(cantError1,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(int(round(cantError2,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(int(round(cantError3,cifras)))+"\n"

		return [titulo, version, pregunta, respuestas] 


	#Sección 3.8


	elif i==16 : 
		#Clientes en una tienda : 3.122
		#[Tienda de, promedio por hora, cantidad limite]
		lista = [["mascotas",5,3],["juguetes",6,5],["ropa",7,6],["cobijas",4,3],["pijamas",5,7]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		articulos = params[0]
		promedioPorHora = params[1]
		cantLimitePersonas = params[2]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Clientes en una tienda"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "A una tienda de "+articulos+" llegan, de acuerdo a un proceso de Poisson, en promedio "+str(promedioPorHora)+" clientes por hora. Durante una hora cualquiera, ¿cuál es la probabilidad de que lleguen a lo sumo "+str(cantLimitePersonas)+ " clientes?"+"\n"

		pReal = poisson.cdf(cantLimitePersonas,promedioPorHora)
		pError1 = 1-poisson.cdf(cantLimitePersonas,promedioPorHora)
		pError2 = poisson.pmf(cantLimitePersonas,promedioPorHora)
		pError3 = poisson.cdf(cantLimitePersonas-1,promedioPorHora)

		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"

		else:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError1,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]
		


#TODO
#Importar un .txt que cargue las secciones de las cuales se quieren los ejercicios

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

ejercicios = [8,16]

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
















