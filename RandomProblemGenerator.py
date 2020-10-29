import numpy as np
import random as rdm
import math
from scipy.stats import binom
from scipy.stats import nbinom
from scipy.stats import geom
from scipy.stats import hypergeom
from scipy.stats import poisson
from scipy.special import binom as bin_coeff

def RandomProblemGenerator(i):
	#Seccion 3.3

	if i==1:
		#Dados: 3.22
		lista=[4,6,8,10,12,16,18,20,22,24,28,32,40,50,52,60,70,80,100]
		pos=rdm.randint(1,len(lista))	
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
		lista=[[["J","Q"],["K","As"]],[["9","10","J"],["Q","K"]],[["As","2","3"],["J","Q","K"]],[["As","3"],["Q","K"]],[["5","7","9"],["J","K","As"]]]
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
		n1 = rdm.randint(2,25)
		n2 = rdm.randint(5,30)
		pCliente = rdm.randint(15,95)/100.0
		pVenta = rdm.randint(5,80)/100.0
		precioVenta = rdm.randint(50,500)*100
		stringPrecioVenta = "{:,}".format(precioVenta)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Ganancias diarias"+"\n"
		#version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		
		pregunta += "Un vendedor puede llamar a "+str(n1)+" o "+str(n2)+" clientes, con probabilidad "+str(round(pCliente,3))+" y "+str(round(1-pCliente,3))+" respectivamente. En cada llamada, hay una probabilidad de "+str(pVenta)+" de realizar una venta de \$"+stringPrecioVenta+". ¿Cuál es la ganancia diaria media de este vendedor?"+"\n"

		gananciaPorLlamada = pVenta*precioVenta		

		gananciaReal = (pCliente*n1+(1-pCliente)*n2)*gananciaPorLlamada
		STRgananciaReal = "{:,}".format(int(gananciaReal))
		gananciaError1 = (n1+n2)*gananciaPorLlamada
		STRgananciaError1 = "{:,}".format(int(gananciaError1))
		gananciaError2 = (n1+n2)*gananciaPorLlamada*pCliente
		STRgananciaError2 = "{:,}".format(int(gananciaError2))
		gananciaError3 = (n1+n2)*gananciaPorLlamada*(1-pCliente)
		STRgananciaError3 = "{:,}".format(int(gananciaError3))
		
		pos = rdm.randint(1,1000)

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
		lista=[8,10,12,14,16,18,20,22,24]
		pos=rdm.randint(1,len(lista))				
		cant=lista[pos-1]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Examen de Opción Múltiple"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		numOpciones = rdm.randint(3,6)
		parar=False
		while parar==False:
			cantRespuestas = rdm.randint(5,int(cant/2))
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
		lista=[["motores"],["estéreos"],["celulares"],["teclados"],["balones"],["portavasos"],["audífonos"]]
		pos=rdm.randint(1,len(lista))				
		params=lista[pos-1]
		cantProductos = rdm.randint(5,25)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Venta de "+str(params[0])+" con devolución"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"
		precio = rdm.randint(1,5)*100
		dev = rdm.randint(10,20)/10
		#Esto podría variarse
		p = 0.05
		pregunta += str(cantProductos)+" "+str(params[0])+" se van a vender en un almacen a \$"+str(precio)+" cada uno. El almacen tiene una política de devolución de "+str(dev)+" veces el valor pagado en caso que el producto esté defectuoso. Uno de los "+str(params[0])+" tiene un defecto con probabilidad "+str(p)+". La ganancia neta esperada por el almacen tras vender todos los productos es"+"\n"

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
	
	elif i==6:
		#Binomial acumulada : 3.40
		#[Probabilidad de recuperación, cantidad muestra pacientes, lim inferior pacientes, lim superior pacientes]
		lista=[[0.8,20,12,15],[0.6,40,25,30],[0.7,12,8,10],[0.5,30,5,25]]
		pos=rdm.randint(1,len(lista))				
		params=lista[pos-1]
		pRecuperacion = rdm.randint(10,80)/100
		tamMuestra = rdm.randint(40,60)
		limInfPacientes = rdm.randint(10,20)
		limSupPacientes = rdm.randint(20,30)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Recuperación de pacientes"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "La probabilidad de que un paciente se recupere de una cierta enfermedad es "+str(pRecuperacion)+". De un grupo de "+str(tamMuestra)+" pacientes que sufren de tal enfermedad, ¿cuál es la probabilidad que se recuperen más de "+str(limInfPacientes)+" pero no más de "+str(limSupPacientes)+"?"+"\n"
		
		pReal = binom.cdf(limSupPacientes,tamMuestra,pRecuperacion)-binom.cdf(limInfPacientes,tamMuestra,pRecuperacion) 
		pError1 = binom.cdf(limSupPacientes-1,tamMuestra,pRecuperacion)-binom.cdf(limInfPacientes-1,tamMuestra,pRecuperacion) 
		pError2 = binom.cdf(limSupPacientes,tamMuestra,pRecuperacion)
		pError3 = binom.cdf(limSupPacientes-1,tamMuestra,pRecuperacion)-binom.cdf(limInfPacientes,tamMuestra,pRecuperacion) 

		cifras=7

		if pos%2==0:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError1,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]



	#Sección 3.5
	

	elif i==7: 
		#Geométrica sin memoria: 3.72
		lista = [0.1,0.2,0.3,0.4,0.5,0.6]
		pos=rdm.randint(1,len(lista))				
		p=rdm.randint(15,85)/100
	
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


	elif i==8: 
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
	
	elif i==9: 
		#Preferencia de marca : 3.78
		#[tipo de artículo]		
		lista = [["chocolates"],["cervezas"],["galletas"],["dulces"]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pPreferencia = rdm.randint(30,50)/100
		articulo = params[0]
		cantMinimaPersonas = rdm.randint(5,10)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Encuesta de preferencia de marca"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "De una ciudad, se sabe que el "+str(pPreferencia*100)+"\% de la población prefieren una cierta marca de "+articulo+". Si se hace una encuesta con ciudadanos al azar, ¿cuál es la probabilidad que al menos "+str(cantMinimaPersonas)+" personas deban ser entrevistadas para que se encuentre la primera persona con la preferencia de tal marca?"+"\n"

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

	
	elif i==10: 
		#Moneda no justa: 3.81
		lista = [0.05,0.1,0.4,0.6]
		pos=rdm.randint(1,len(lista))			
		p = rdm.randint(5,40)/100
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


	elif i==11:
		#Artículos defectuosos: 3.92
		#[Porcentaje de falla, nombre artículo, número de articulo defectuoso, texto anterior ,número de intento, texto anterior] con numDefecto < numIntentos 
		lista = [[5,"pantalla",2,"segunda",5,"quinto"],[10,"vela",1,"primera",3,"tercero"],[2,"computadora",3,"tercera",5,"quinto"],[7,"silla",3,"tercera",6,"sexto"],[8,"estufa",1,"primera",3,"tercero"],[8,"cámara",2,"segunda",4,"cuarto"],[8,"lámpara",1,"primera",3,"tercero"],[8,"maleta",3,"tercera",5,"quinto"]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pFallo = rdm.randint(1,15)/100
		articulo = params[1]
		numNoDefectos = params[2]
		numIntentos = params[4]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Title: Errores de producción de "+articulo+"s"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += str(round(pFallo*100,0))+" por ciento de las "+articulo+"s fabricadas por una empresa son defectuosas. Si estos artículos se prueban al azar uno a la vez, ¿cuál es la probabilidad de que la "+params[3]+" "+articulo+" no defectuosa sea hallada en el "+params[5]+" intento?"+"\n"

		p = pFallo
		q = 1-p
		pReal = bin_coeff(numIntentos-1,numNoDefectos-1)*q**numNoDefectos*p**(numIntentos-numNoDefectos)
		pError1 = bin_coeff(numIntentos-1,numNoDefectos-1)*p**numIntentos*q**(numIntentos-numNoDefectos)
		pError2 = bin_coeff(numIntentos,numNoDefectos)*p**numNoDefectos*q**(numIntentos)
		pError3 = bin_coeff(numIntentos,numNoDefectos)*q**numNoDefectos*p**(numIntentos)

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

	elif i==12:
		#Cantidad media de tréboles: 3.97
		
		lista = [[0.1,6],[0.2,5],[0.05,4],[0.15,7]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		p = rdm.randint(5,11)/100
		cant = rdm.randint(5,15)
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
		cantError3 = p*cant

		cifras=0
		if pos%2==0:
			respuestas += "a. "+str(int(math.ceil(cantError3)))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(int(math.ceil(cantReal)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "c. "+str(int(math.ceil(cantError2)))+"\n"
			respuestas += " "+"\n"		
			respuestas += "d. "+str(int(math.ceil(cantError1)))+"\n"

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

	
	elif i==13: 
		#Canicas de colores: 3.102
		#[Número total de canicas, num canicas amarillas, num canicas azules, cantidad sacadas, cantidad deseada azul]
		lista = [[10,2,4,5,2],[15,5,5,6,3],[15,8,4,4,4],[20,10,5,10,3]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		numTotalCanicas = rdm.randint(15,25)
		numCanicasA = rdm.randint(2,8)
		numCanicasZ = rdm.randint(6,10)
		numCanicasR = numTotalCanicas - numCanicasA - numCanicasZ
		cantSacadas = rdm.randint(5,9)
		cantDeseadaZ = rdm.randint(3,6)
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

	
	elif i==14:
		#Flores blancas y rojas : 3.114
		#[Tamaño ramo, cantidad total flores, cantidad flores rojas del total]
		lista = [[10,100,50],[25,200,150],[15,140,60],[20,300,175],[30,200,120]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		tamRamo = rdm.randint(15,50)
		cantTotalFlores = rdm.randint(10,25)*10
		numFloresR = rdm.randint(5,12)*10
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

	elif i==15:
		#Costo de reparación: 3.106
		#[Nombre artículo, cantidad total articulos, cantidad articulos defectuosos, costo reparación, tamaño del muestreo]
		#tamMuestra != cantArticulosDefectuosos
		lista = [["celulares",100,15,100000,10], ["computadores",20,7,150000,5], ["esferos",200,25,10000,16], ["pantalones",50,12,20000,8]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		articulos = params[0]
		cantTotalArticulos = rdm.randint(10,25)*10
		cantArticulosDefectuosos = rdm.randint(10,30)
		costoReparacionPorArticulo = rdm.randint(10,100)*1000
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

	elif i==16:
		#Tamaño de muestra : 3.106
		#[Articulo, cantidad total, cantidad defectuosos,probabilidad de AL MENOS 1 defectuoso]
		lista = [["celulares",100,15,0.8], ["computadores",40,10,0.9], ["esferos",200,25,0.95], ["pantalones",50,12,0.85]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		articulos = params[0]
		cantTotalArticulos = rdm.randint(10,25)*10
		cantArticulosDefectuosos = rdm.randint(10,30)
		probabilidadAlMenosUnDefecto = rdm.randint(80,95)/100
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
		cont = 1
		while parar == False :
			cont += 1			
			probError3 = bin_coeff(cantArticulosDefectuosos,1)*bin_coeff(cantTotalArticulos-cantArticulosDefectuosos,cont-1)/bin_coeff(cantTotalArticulos,cont)
			if probError3 <= 1-probabilidadAlMenosUnDefecto/1.5:
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


	elif i==41:
		#Apostador : 3.194
		#[Probabilidad de ganar, costo entrada, ganancia, dinero inicial, cantidad de veces ganadas, dinero final]

		# (cantGanadas*ganancia+dineroInicial-dineroFinal)/costoEntrada debe ser un entero

		lista = [[0.1,10,50,30,4,100],[0.2,4,12,20,3,36],[0.3,10,50,30,5,150],[0.2,6,30,60,4,150]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pGanar = rdm.randint(15,25)/100
		costoEntrada = params[1]
		ganancia = params[2]
		dineroInicial = params[3]
		cantGanadas = params[4]
		dineroFinal = params[5]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Apostador"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "Un apostador tiene una probabilidad de "+str(pGanar)+" de ganar en cierto juego de casino. Para entrar al juego debe pagar \$"+str(costoEntrada)+" y en caso de ganar recibe \$"+str(ganancia)+". Si el apostador inicia con \$"+str(dineroInicial)+", ¿cuál es la probabilidad que, tras ganar "+str(cantGanadas)+" veces en este juego, salga con \$"+str(dineroFinal)+" del casino?"+"\n"

		fallos = (cantGanadas*(ganancia-costoEntrada)+dineroInicial-dineroFinal)/costoEntrada

		pReal = nbinom.pmf(int(fallos),cantGanadas,pGanar)
		pError1 = nbinom.pmf(int((cantGanadas*ganancia)/costoEntrada), cantGanadas, pGanar)
		pError2 = nbinom.pmf(int((cantGanadas*ganancia+dineroInicial-dineroFinal)/costoEntrada),cantGanadas,pGanar)
		pError3 = nbinom.cdf(int(fallos), cantGanadas, pGanar)

		cifras=6

		if pos%2==0:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError1,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	elif i==42:
		#Apostador (Variación): 3.194
		#[Probabilidad de ganar, costo entrada, ganancia, dinero inicial, cantidad de veces ganadas, dinero final]

		# (dineroFinal-dineroInicial)/ganancia debe ser un entero

		lista = [[0.1,10,40,20,4,100],[0.2,4,8,20,3,36],[0.3,10,40,30,5,150],[0.2,6,30,20,4,140]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pGanar = rdm.randint(5,15)/100
		costoEntrada = params[1]
		ganancia = params[2]
		dineroInicial = params[3]
		cantGanadas = params[4]
		dineroFinal = params[5]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Apostador"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "Un apostador tiene una probabilidad de "+str(pGanar)+" de ganar en cierto juego de casino y en caso de hacerlo recibe \$"+str(ganancia)+". Si el apostador inicia con \$"+str(dineroInicial)+", ¿cuál es el mínimo de rondas que debe jugar para esperar salir con \$"+str(dineroFinal)+" del casino?"+"\n"


		cantReal = (int((dineroFinal-dineroInicial)/ganancia))/pGanar
		cantError1 = int((dineroFinal-dineroInicial)/ganancia)
		cantError2 = (cantGanadas*ganancia-dineroFinal+dineroInicial)
		cantError3 = (int((dineroFinal-dineroInicial)))/(1-pGanar)

		cifras=2
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


	elif i==17 : 
		#Clientes en una tienda : 3.122
		#[Tienda de, promedio por hora, cantidad limite]
		lista = [["mascotas",5,3],["juguetes",6,5],["ropa",7,6],["cobijas",4,3],["pijamas",5,7]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		articulos = params[0]
		promedioPorHora = rdm.randint(3,15)
		cantLimitePersonas = rdm.randint(2,10)
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

	elif i==18:
		#Entradas a una tienda: 3.130
		#[promedio entrada 1, promedio entrada 2, cantidad personas]
		lista = [[2,3,5],[4,3,5],[2,3,6],[1,2,4],[3,1,5]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		promEntrada1 = rdm.randint(10,20)
		promEntrada2 = rdm.randint(15,25)
		cantPersonas = rdm.randint(20,30)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Entradas de una tienda"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"	
		
		pregunta += "Una tienda tiene dos entradas. La primera tiene un promedio de uso de "+str(promEntrada1)+" personas por hora y la segunda un promedio de "+str(promEntrada2)+" personas por hora. Si la cantidad de personas que entran por cada puerta sigue una distribución de Poisson, ¿cuál es la probabilidad que "+str(cantPersonas)+ " entren a la tienda en una hora determinada? (Asuma que las distribuciones de cada entrada son independientes)"+"\n"


		pReal = poisson.pmf(cantPersonas,promEntrada1+promEntrada2)
		pError1 = poisson.cdf(cantPersonas,promEntrada1)
		pError2 = poisson.pmf(cantPersonas,promEntrada1)*poisson.pmf(cantPersonas,promEntrada2)
		pError3 = poisson.cdf(cantPersonas,promEntrada2)
			
		cifras=6

		if pos%2==0:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError3,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	elif i==19:
		#Parqueadero : 3.126a
		#[promedio entrada por hora, hora inicio, hora final]
		lista = [[2,3,5,6],[4,3,5,7],[2,3,6,8],[5,2,4,5],[3,1,5,10]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		promEntrada = rdm.randint(5,10)
		horaInicial = rdm.randint(4,6)
		horaFinal = rdm.randint(7,9)
		cantAutos = rdm.randint(15,22)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Entradas de un parqueadero"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"	

		pregunta += "A un parqueadero entran "+str(promEntrada)+" autos por hora según un proceso de Poisson. ¿Cuál es la probabilidad de que lleguen al menos "+str(cantAutos)+" entre las "+str(horaInicial)+":00 pm y las "+str(horaFinal)+":00 pm?"+"\n"

		pReal = 1-poisson.cdf(cantAutos-1,promEntrada*(horaFinal-horaInicial)) 
		pError1 = 1-poisson.cdf(cantAutos,promEntrada*(horaFinal-horaInicial)) 
		pError2 = 1-poisson.cdf(cantAutos-1,promEntrada) 
		pError3 = 1-poisson.pmf(cantAutos,promEntrada*(horaFinal-horaInicial)) 

		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError3,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	elif i==20:
		#Cambio de intervalo : 3.128
		#[promedio por hora, duración de de llamada en minutos,string para pregunta]
		lista = [[20,3,"minutos"],[30,2,"minutos"],[25,1,"minuto"],[40,1,"minuto"],[25,2,"minutos"]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		promPersonas = rdm.randint(20,45)
		duracionLlamada = params[1]
		strTiempo = params[2]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Interrupción de llamada"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"	

		pregunta += "Un empleado de una tienda realiza una llamada de "+str(duracionLlamada)+" "+strTiempo+". Si a la tienda llegan clientes con una distribución de Poisson con promedio de "+str(promPersonas)+" por hora, ¿cuál es la probabilidad de que la llamada del empleado sea interrumpida?"+"\n"

		pReal = 1-poisson.pmf(0,promPersonas/(60.0/duracionLlamada)) 
		pError1 = poisson.pmf(1,promPersonas/(60.0/duracionLlamada))
		pError2 = 1-poisson.pmf(0,promPersonas/60.0) 
		pError3 = poisson.cdf(1,promPersonas/60.0) 

		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError1,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]


	#Seccion 3.9


	elif i==45: 
		#Función generadora de momentos de una binomial
		#[n,p,N]
		lista = [[20,0.4,15],[30,0.2,23],[25,0.45,8],[50,0.25,12],[15,0.73,4],[75,0.19,20]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		n = rdm.randint(10,15)
		p = rdm.randint(3,8)/10
		N = rdm.randint(5,10)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "MGF"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"	

		pregunta += "Suponga que $X$ es una variable aleatoria con función generadora de momentos dada por "
		
		mgf = "$\left("+str(round(p,3))+"e^t+"+str(round(1-p,3))+"\ "+"right)^{"+str(n)+"}$" 
		mgf = mgf.replace(" ","")

		pregunta += mgf+". ¿Cuánto vale Pr$(X\geq"+str(N)+")$?"+"\n"
		
		pReal = 1-binom.cdf(N-1,n,p)
		pError1 = 1-binom.cdf(N,n,p)
		pError2 = 1-binom.cdf(N-1,n,1-p)
		pError3 = 1-geom.cdf(n,p)

		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError3,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	elif i==46:
		#Función generadora de momentos de una binomial (variacion)
		#[n,p,N]
		lista = [[20,0.4,15],[30,0.2,23],[25,0.05,17],[100,0.05,69],[47,0.73,23],[123,0.19,100]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		n = rdm.randint(10,25)
		p = rdm.randint(3,9)/10
		N = rdm.randint(5,10)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "MGF"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"	

		pregunta += "Suponga que $X$ es una variable aleatoria con función generadora de momentos dada por "
		
		mgf = "$\left("+str(round(p,3))+"e^t+"+str(round(1-p,3))+"\ "+"right)^{"+str(n)+"}$" 
		mgf = mgf.replace(" ","")

		pregunta += mgf+". ¿Cuáles son el valor esperado y la varianza de X?"+"\n"	
	
		muReal = n*p
		muError = 1/p
		sigmaReal = n*p*(1-p)
		sigmaError = (1-p)/p**2

		cifras = 3
		if pos%2==0:
			respuestas += "*a. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

		elif pos%2==1:
			respuestas += "a. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas +="*b. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas +="c. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

		return [titulo, version, pregunta, respuestas]

	
	elif i==47:
		#Función generadora de momentos geométrica
		#[p,N]
		lista = [[0.6,10],[0.2,8],[0.1,5],[0.3,12],[0.73,4],[0.19,9]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		p = rdm.randint(20,50)/100
		N = rdm.randint(1,5)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "MGF"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"	

		pregunta += "Suponga que $X$ es una variable aleatoria con función generadora de momentos dada por "

		mgf = "$\ "+"frac{"+str(round(p,3))+"e^t}{1-"+str(round(1-p,3))+"e^t}$" 
		mgf = mgf.replace(" ","")

		pregunta += mgf+". ¿Cuánto vale Pr$(X\leq"+str(N)+")$?"+"\n"

		pReal = geom.cdf(N,p)
		pError1 = geom.pmf(N,p)
		pError2 = geom.cdf(N,1-p)
		pError3 = 1-pReal

		cifras=5

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
			respuestas += "b. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	elif i==48:
		#Función generadora de momentos geométrica
		#[p,N]
		lista = [[0.6,15],[0.2,28],[0.1,100],[0.3,69],[0.73,27],[0.19,45]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		p = rdm.randint(20,50)/100
		N = rdm.randint(1,5)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "MGF"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"	

		pregunta += "Suponga que $X$ es una variable aleatoria con función generadora de momentos dada por "

		mgf = "$\ "+"frac{"+str(round(p,3))+"e^t}{1-"+str(round(1-p,3))+"e^t}$" 
		mgf = mgf.replace(" ","")

		pregunta += mgf+". ¿Cuáles son la media y la varianza de X?"+"\n"

		muReal = 1/p
		muError = N*p
		sigmaReal = (1-p)/p**2
		sigmaError = 1/p**2
		
		cifras = 3
		if pos%2==0:
			respuestas += "a. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"

		elif pos%2==1:
			respuestas += "a. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas +="*b. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas +="c. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

		return [titulo, version, pregunta, respuestas]


	elif i==49: 
		#Función generadora de momentos Poisson
		#[lambda, N]
		lista = [[10,5],[5,7],[7,6],[0.11,1],[0.75,2],[0.19,1]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		l = rdm.randint(2,6)
		N = rdm.randint(2,5)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "MGF"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"	

		pregunta += "Suponga que $X$ es una variable aleatoria con función generadora de momentos dada por "

		mgf = "$e^{"+str(l)+"(e^t-1)}$" 
		mgf = mgf.replace(" ","")

		pregunta += mgf+". ¿Cuánto vale Pr$(X>"+str(N)+")$?"+"\n"

		pReal = 1-poisson.cdf(N-1,l)
		pError1 = 1-poisson.cdf(N,l)
		pError2 = 1-poisson.cdf(N,1/l)
		pError3 = 1-poisson.pmf(N-1,l)

		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError3,cifras))+"\n"

		else:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]


	elif i==50:
		#Función generadora de momentos hipergeométrica
		#[p,r,N]
		lista = [[0.6,10,5],[0.2,4,6],[0.1,7,7],[0.3,10,5],[0.73,4,4],[0.19,7,3]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		p = rdm.randint(10,40)/100
		r = rdm.randint(2,5)
		N = rdm.randint(1,10)
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "MGF"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"	

		pregunta += "Suponga que $X$ es una variable aleatoria con función generadora de momentos dada por "

		mgf = "$\ "+"left("+"\ "+"frac{"+str(round(p,3))+"}{1-"+str(round(1-p,3))+"e^t}"+"\ "+"right)^"+str(r)+"$" 
		mgf = mgf.replace(" ","")

		pregunta += mgf+". ¿Cuánto vale Pr$(X<"+str(N)+")$?"+"\n"

		pReal = nbinom.cdf(N-1,r,p)
		pError1 = geom.cdf(N-1,p)
		pError2 = nbinom.cdf(N,r,1-p)
		pError3 = binom.cdf(r,N-1,p)

		cifras=5

		if pos%2==0:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError3,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	#DeGroot & Schervish

	#Section 5.2

	elif i==21:
		#Más caras que sellos: 5.2.3
		#[probabilidad cara, cantidad de tiros]
		lista = [[0.5,7],[0.4,8],[0.6,10],[0.7,7],[0.3,8],[0.8,9]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pCara = params[0]
		cantTiros = params[1]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Más caras que sellos"+"\n"
		version += "%Jeronimo Valencia, Tipo 0"+str(i)+", ver 0"+str(pos)+"\n"	

		pregunta += "Una moneda con probabilidad de cara "+str(pCara)+" se lanza "+str(cantTiros)+" veces. ¿Cuál es la probabilidad de que salgan más caras que sellos?"+"\n"

		pReal = 0
		pError1 = 0
		pError2 = 0
		pError3 = 0
	
		for n in range(int(cantTiros/2.0)+1,cantTiros+1):
			pReal += binom.pmf(n,cantTiros,pCara)
		
		pError1 += binom.pmf(int(cantTiros/2.0),cantTiros,pCara)
	
		for n in range(int(cantTiros/2.0)+1,cantTiros+1):
			pError2 += binom.pmf(n,cantTiros,1-pCara)			

		pError3 = binom.cdf(int(cantTiros/2)+1,cantTiros-1,pCara)

		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError1,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

		
	elif i==22:
		#Disparos : 5.2.6
		#[Prob. acierto 1, Cantidad tiros 1, Prob. acierto 2, Cantidad tiros 2, Prob. acierto 3, Cantidad tiros 3]
		lista = [[0.3,10,0.4,5,0.6,3],[0.5,10,0.6,2,0.9,10],[0.6,4,0.3,10,0.7,2],[0.6,6,0.6,2,0.3,10]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pAcierto1 = params[0]
		cantTiros1 = params[1]
		pAcierto2 = params[2]
		cantTiros2 = params[3]
		pAcierto3 = params[4]
		cantTiros3 = params[5]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Disparos con probabilidad"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "Tres personas van a disparar a un objetivo. La primera persona disparará "+str(cantTiros1)+" veces y tiene probabilidad de acertar de "+str(pAcierto1)+". La segunda lo hará "+str(cantTiros2)+" veces y tiene probabilidad de acierto de "+str(pAcierto2)+"; y la tercera "+str(cantTiros3)+" veces y tiene probabilidad de dar en el blanco de "+str(pAcierto3)+". ¿Cuál es el valor esperado y la varianza del número de disparos que dan en el blanco? (Asuma que los disparos son independientes)"+"\n"

		muReal = pAcierto1*cantTiros1+pAcierto2*cantTiros2+pAcierto3*cantTiros3
		sigmaReal = pAcierto1*cantTiros1*(1-pAcierto1)+pAcierto2*cantTiros2*(1-pAcierto2)+pAcierto3*cantTiros3*(1-pAcierto3)
		muError = (pAcierto1+pAcierto2+pAcierto3)*(cantTiros1+cantTiros2+cantTiros3)
		sigmaError = pAcierto1*cantTiros1*(pAcierto1)+pAcierto2*cantTiros2*(pAcierto2)+pAcierto3*cantTiros3*(pAcierto3)
			
		cifras = 3
		if pos%2==0:
			respuestas += "a. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

		elif pos%2==1:
			respuestas += "a. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas +="b. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas +="c. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

		return [titulo, version, pregunta, respuestas]


	elif i==23:
		#Probabilidad condicional : 5.2.8
		#[Probabilidad de falla, cantidad 1, cantidad 2, Cantidad total de componentes] con cant1 < cant2
		lista = [[0.1,2,3,10],[0.15,2,4,15],[0.2,3,4,12],[0.2,2,4,8],[0.3,2,3,10]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pFalla = params[0]
		cant1 = params[1]
		cant2 = params[2]
		cantTotalComponentes = params[3]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Fallo de componentes"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "Un componente de un circuito falla con probabilidad "+str(pFalla)+". Si en total se tienen "+str(cantTotalComponentes)+" componentes independientes en un circuito en el cual se sabe que al menos "+str(cant1)+" han fallado, ¿cuál es la probabilidad de que fallen al menos "+str(cant2)+" en todo el circuito?"+"\n"

		pReal = (1-binom.cdf(cant2-1,cantTotalComponentes,pFalla))/(1-binom.cdf(cant1-1,cantTotalComponentes,pFalla)) 
		pError1 = binom.cdf(cant2-1,cantTotalComponentes,pFalla)
		pError2 = (1-binom.cdf(cant2,cantTotalComponentes,pFalla))/(1-binom.cdf(cant1,cantTotalComponentes,pFalla))
		pError3 = (1-binom.cdf(cant2-1,cantTotalComponentes,pFalla))

		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(round(pReal,cifras))+"\n"
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

	elif i==24:
		#Pacientes : 5.2.13		
		#[Probabilidad de recuperación 1, probabilidad de recuperación 2, cantidad de pacientes grupo 1, cantidad pacientes grupo 2]
		lista = [[0.4,0.3,4,3],[0.5,0.6,3,4],[0.4,0.7,3,5],[0.6,0.3,4,3],[0.5,0.2,3,4],[0.4,0.3,2,5]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pRec1 = params[0]
		pRec2 = params[1]
		cantPacientes1 = params[2]
		cantPacientes2 = params[3]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Recuperación de pacientes"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"	

		pregunta += "En un ensayo clínico hay dos grupos independientes de pacientes. En el grupo 1 hay una probabilidad de recuperación de "+str(pRec1)+" y en el grupo 2 una de "+str(pRec2)+". Si el grupo 1 consta de "+str(cantPacientes1)+" y el grupo 2 de "+str(cantPacientes2)+", ¿cuál es la probabilidad de que en el grupo 1 se recuperen más pacientes que en el grupo 2?"+"\n"

		pReal = 0
		pError3 = 0

		for i in range(0,cantPacientes1+1):
			for j in range(0,cantPacientes2+1):
				if i>j: 
					pReal += binom.pmf(i,cantPacientes1,pRec1)*binom.pmf(i,cantPacientes2,pRec2)

		for i in range(1,cantPacientes1):
			for j in range(1,cantPacientes2):
				if i>j: 
					pError3 += binom.pmf(i,cantPacientes1,pRec1)*binom.pmf(i,cantPacientes2,pRec2)

		pError1 = binom.pmf(cantPacientes1,cantPacientes1,pRec1)*binom.pmf(cantPacientes2,cantPacientes2,pRec2)
		pError2 = binom.cdf(int(cantPacientes1/2),cantPacientes1,pRec1)*binom.cdf(int(cantPacientes2/2),cantPacientes2,pRec2)

		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]	

		
	 #Section 5.3

	elif i==25: 
		#Pelotas de colores: 5.3.2
		#[Cantidad pelotas azules, cantidad pelotas rojas, cantidad muestra, cantidad limite, color pregunta]
		lista = [[5,5,7,3,"azules"],[4,6,6,3,"rojas"],[7,11,7,4,"azules"],[8,6,5,3,"rojas"],[8,4,6,4,"azules"]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		cantAzul = params[0]
		cantRoja = params[1]
		cantMuestra = params[2]
		cantLim = params[3]
		STRcolor = params[4]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Pelotas de colores"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"	
		
		pregunta += "En una caja hay "+str(cantAzul)+" pelotas azules y "+str(cantRoja)+" pelotas rojas. Si se sacan "+str(cantMuestra)+" pelotas de la caja sin reemplazo, ¿cuál es la probabilidad de que salgan al menos "+str(cantLim)+" pelotas "+STRcolor+"?"+"\n"
	
		pRealAzul = 1-hypergeom.cdf(cantLim-1,cantAzul+cantRoja,cantAzul,cantMuestra)
		pRealRoja = 1-hypergeom.cdf(cantLim-1,cantAzul+cantRoja,cantRoja,cantMuestra)
		pError1 = 1-hypergeom.cdf(cantLim,cantRoja+cantAzul,cantAzul,cantMuestra)
		pError2 = 1-hypergeom.cdf(cantLim,cantAzul+cantRoja,cantRoja,cantMuestra)
		
		cifras=5

		if STRcolor == "rojas": 
			if pos%2==0:
				respuestas += "a. "+str(round(pError1,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. "+str(round(pError2,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "c. "+str(round(pRealAzul,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*d. "+str(round(pRealRoja,cifras))+"\n"

			else:
				respuestas += "a. "+str(round(pRealAzul,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. "+str(round(pError2,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*c. "+str(round(pRealRoja,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "d. "+str(round(pError1,cifras))+"\n"

		else: 
			if pos%2==0:
				respuestas += "a. "+str(round(pError1,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. "+str(round(pError2,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*c. "+str(round(pRealAzul,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "d. "+str(round(pRealRoja,cifras))+"\n"

			else:
				respuestas += "*a. "+str(round(pRealAzul,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. "+str(round(pError2,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "c. "+str(round(pRealRoja,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "d. "+str(round(pError1,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]	

	elif i==26:
		#Proporción en muestra: 5.3.3
		#[Cantidad esferos rojos, cantidad esferos negro, tamaño muestra, texto pregunta]
		lista = [[16,14,10,"negros"],[20,10,15,"rojos"],[24,18,12,"negros"],[10,16,9,"rojos"],[7,23,13,"negros"]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		cantRojos = params[0]
		cantNegros = params[1]
		cantMuestra = params[2]
		STRcolor = params[3]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Esferos de colores"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"
		

		pregunta += "En una bolsa se tienen "+str(cantRojos)+" esferos rojos y "+str(cantNegros)+" esferos negros. Si se sacan sin reemplazo un total de "+str(cantMuestra)+" esferos y $P$ denota la proporción de esferos "+STRcolor+" en tal muestra, ¿cuáles son el valor esperado y la varianza de $P$?"+"\n"

		muRealNegro = (1.0/cantMuestra)*(cantMuestra*cantNegros/(cantNegros+cantRojos))	
		muErrorNegro = (cantMuestra*cantNegros/(cantNegros+cantRojos))
		muRealRojo = (1.0/cantMuestra)*(cantMuestra*cantRojos/(cantNegros+cantRojos))
		muErrorRojo = (cantMuestra*cantRojos/(cantNegros+cantRojos))
		sigmaReal = (1.0/cantMuestra**2)*(cantMuestra*cantRojos*cantNegros/(cantRojos+cantNegros)**2)*((cantRojos+cantNegros-cantMuestra)/(cantRojos+cantNegros-1))
		sigmaError = (cantMuestra*cantRojos*cantNegros/(cantRojos+cantNegros)**2)*((cantRojos+cantNegros-cantMuestra)/(cantRojos+cantNegros-1))
		
		if STRcolor == "rojos":
			cifras = 3
			if pos%2==0:
				respuestas += "a. El valor esperado es "+str(round(muErrorRojo,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*b. El valor esperado es "+str(round(muRealRojo,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "c. El valor esperado es "+str(round(muRealRojo,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "d. El valor esperado es "+str(round(muErrorRojo,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

			elif pos%2==1:
				respuestas += "a. El valor esperado es "+str(round(muErrorRojo,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas +="b. El valor esperado es "+str(round(muErrorRojo,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas +="c. El valor esperado es "+str(round(muRealRojo,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*d. El valor esperado es "+str(round(muRealRojo,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

		else:
			cifras = 3
			if pos%2==0:
				respuestas += "a. El valor esperado es "+str(round(muRealNegro,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. El valor esperado es "+str(round(muErrorNegro,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "c. El valor esperado es "+str(round(muErrorNegro,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*d. El valor esperado es "+str(round(muRealNegro,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

			elif pos%2==1:
				respuestas += "a. El valor esperado es "+str(round(muErrorNegro,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas +="b. El valor esperado es "+str(round(muErrorNegro,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas +="c. El valor esperado es "+str(round(muRealNegro,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*d. El valor esperado es "+str(round(muRealNegro,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

		return [titulo, version, pregunta, respuestas]

	
	#Section 5.4


	elif i==27: 
		#Imperfectos en una tela : 5.4.6
		#[Promedio errores por unidad de longitud, unidad de longitud (metros), longitud tela final (metros), cantidad máxima de errores, texto: error/errores]
		lista = [[2,10,15,2,"errores"],[4,20,15,2,"errores"],[3,20,18,1,"error"],[5,50,10,1,"error"],[8,10,12,2,"errores"]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		promErrores = params[0]
		unidadLongitud = params[1]
		longitudMuestra = params[2]
		cantMaximaErrores = params[3]
		STRerror = params[4]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Imperfectos en una tela"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"		

		pregunta += "Una empresa textil posee una máquina que causa, en promedio, "+str(promErrores)+" imperfecciones en cada "+str(unidadLongitud)+" metros de tela. Si se toma un retazo de tela de "+str(longitudMuestra)+" metros, ¿cuál es la probabilidad de que esta muestra tenga menos de "+str(cantMaximaErrores)+" "+STRerror+"?"+"\n"

		pReal = poisson.cdf(cantMaximaErrores-1,(longitudMuestra/unidadLongitud)*promErrores) 
		pError1 = poisson.cdf(cantMaximaErrores,(longitudMuestra/unidadLongitud)*promErrores)
		pError2 = poisson.cdf(cantMaximaErrores-1,promErrores)
		pError3 = 1-poisson.cdf(cantMaximaErrores,promErrores)

		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError1,cifras))+"\n"

		else:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]
	
	elif i==28:
		#Proporción de árboles: 5.4.13
		#[Proporción, tamaño muestra, cantidad limite]
		lista = [[0.1,100,5],[0.05,200,7],[0.12,100,6],[0.11,100,8],[0.13,500,6],[0.09,100,7]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		proporcion = params[0]
		tamMuestra = params[1]
		cantLimite = params[2]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Árboles con frutos azules"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"
		
		pregunta += "En un bosque, la proporción de árboles que dan un fruto azul es de "+str(proporcion)+". Si se observan los frutos de "+str(tamMuestra)+" árboles, ¿cuál es la probabilidad de que se encuentren más de "+str(cantLimite)+" árboles con este tipo de fruto?"+"\n"
	
		pReal = 1-poisson.cdf(cantLimite,proporcion*tamMuestra) 
		pError1 = poisson.cdf(cantLimite,proporcion*tamMuestra)
		pError2 = 1-poisson.cdf(cantLimite-1,proporcion*tamMuestra)
		pError3 = poisson.pmf(cantLimite,proporcion*tamMuestra)

		cifras=5

		if pos%2==0:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError1,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	elif i==29:
		#Imperfectos en una tela (variación): 5.4.6
		#[Promedio errores por unidad de longitud, unidad de longitud (metros), longitud tela final (metros)]
		lista = [[2,10,15],[4,20,15],[3,20,18],[5,50,10],[8,10,12]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		promErrores = params[0]
		unidadLongitud = params[1]
		longitudMuestra = params[2]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Promedio de imperfectos en una tela"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"		

		pregunta += "Una empresa textil posee una máquina que causa, en promedio, "+str(promErrores)+" imperfecciones en cada "+str(unidadLongitud)+" metros de tela. Si se toma un retazo de "+str(longitudMuestra)+" metros generado por esta máquina, ¿cuántas imperfecciones esperaría ver?"+"\n"

		cantReal = promErrores*(longitudMuestra/unidadLongitud)
		cantError1 = promErrores*longitudMuestra
		cantError2 = promErrores**2
		cantError3 = cantReal**2-cantReal

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

	elif i==30:
		#Personas entrando a un centro comercial: --
		#[Promedio entrada 1 por hora, promedio entrada 2 por hora, cantidad mínima por hora, cantidad limite]
		lista = [[12,10,15,25],[15,15,20,28],[10,8,12,20],[5,4,10,15],[8,10,12,19]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		promEntrada1 = params[0]
		promEntrada2 = params[1]
		cantMinimaPorHora = params[2]	
		cantLimite = params[3]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Entradas a un centro comercial"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "En un centro comercial pequeño hay dos entradas. En promedio, entran "+str(promEntrada1)+" personas por hora por la primera y "+str(promEntrada2)+" personas por hora por la segunda. Si en una hora se sabe que han entrado al menos "+str(cantMinimaPorHora)+" personas, ¿cuál es la probabilidad de que en esa misma hora entren más de "+str(cantLimite)+" personas?"+"\n"

		pReal = (1-poisson.cdf(cantLimite,promEntrada1+promEntrada2))/(1-poisson.cdf(cantMinimaPorHora-1,promEntrada1+promEntrada2))
		pError1 = (1-poisson.cdf(cantLimite,promEntrada1+promEntrada2))/(1-poisson.cdf(cantMinimaPorHora,promEntrada1+promEntrada2))
		pError2 = 1-poisson.cdf(cantLimite,promEntrada1+promEntrada2)
		pError3 = 1-poisson.cdf(cantMinimaPorHora,promEntrada1+promEntrada2)

		cifras=6

		if pos%2==0:
			respuestas += "a. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError1,cifras))+"\n"

		else:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]


	#Section 5.5

		
	elif i==31: 
		#Lanzar una moneda : 5.5.2
		#[Probabilidad cara, cantidad máxima caras]
		lista = [[0.7,5],[0.3,6],[0.6,10],[0.4,8],[0.75,10],[0.25,12]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pSello = params[0]
		cantMaximaCaras = params[1]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Lanzamiento de monedas"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "Si se hacen lanzamientos independientes de una moneda con probabilidad "+str(pSello)+" de obtener sello, ¿cuáles son el número esperado y la varianza de sellos que se obtendrán antes de obtener "+str(cantMaximaCaras)+" caras?"+"\n"
	
		p = 1-pSello
		
		muReal = cantMaximaCaras*(1-p)/p
		muError = cantMaximaCaras*(1-pSello)/pSello
		sigmaReal = cantMaximaCaras*(1-p)/p**2
		sigmaError = cantMaximaCaras*(1-pSello)/pSello**2

		cifras = 2
		if pos%2==0:
			respuestas += "a. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

		elif pos%2==1:
			respuestas += "a. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas +="b. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas +="c. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

		return [titulo, version, pregunta, respuestas]

	
	elif i==32: 
		#Lanzar una moneda (variación) : 5.5.3
		#[Probabilidad cara, cantidad máxima caras]
		lista = [[0.7,5],[0.3,6],[0.6,10],[0.4,8],[0.75,10],[0.25,12]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pSello = params[0]
		cantMaximaCaras = params[1]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Lanzamiento de monedas"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "Si se hacen lanzamientos independientes de una moneda con probabilidad "+str(pSello)+" de obtener sello, ¿cuáles son el número esperado y la varianza del número de lanzamientos necesarios para obtener "+str(cantMaximaCaras)+" caras?"+"\n"
		
		p = 1-pSello
		muReal = cantMaximaCaras*(1-p)/p + cantMaximaCaras
		muError = cantMaximaCaras*(1-p)/p
		sigmaReal = cantMaximaCaras*(1-p)/p**2
		sigmaError = cantMaximaCaras*(1-pSello)/pSello**2

		cifras = 2
		if pos%2==0:
			respuestas += "a. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"

		elif pos%2==1:
			respuestas += "*a. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas +="b. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas +="c. El valor esperado es "+str(round(muReal,cifras))+" y la varianza es "+str(round(sigmaError,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. El valor esperado es "+str(round(muError,cifras))+" y la varianza es "+str(round(sigmaReal,cifras))+"\n"

		return [titulo, version, pregunta, respuestas]

	
	elif i==33:
		#Suma de binomiales negativas: 5.5.5
		#[Probabilidad de obtener una pelota blanca, Cantidad blancas bolsa 1, cantidad blancas bolsa 2, cantidad negras antes de la suma]
		lista = [[0.4,10,15,12],[0.3,6,8,18],[0.6,10,10,13],[0.4,15,12,19],[0.7,10,8,15],[0.5,12,14,16]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pBlanca = params[0]
		cantBlancas1 = params[1]
		cantBlancas2 = params[2]
		cantFinal = params[3]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Bolsas de pelotas"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "Suponga que se tiene dos bolsas con pelotas blancas y negras. La probabilidad de sacar una bola blanca de cualquiera de las dos bolsas es "+str(pBlanca)+". Si se sacan, con reemplazo, pelotas de la primera bolsa hasta alcanzar "+str(cantBlancas1)+" blancas, y de la segunda hasta alcanzar "+str(cantBlancas2)+" blancas, ¿cuál es la probabilidad de sacar "+str(cantFinal)+" pelotas negras en todo el proceso?"+"\n"

		pReal = nbinom.pmf(cantFinal,cantBlancas1+cantBlancas2,pBlanca)
		pError1 = nbinom.pmf(cantFinal,cantBlancas1,pBlanca)*nbinom.pmf(cantFinal,cantBlancas2,pBlanca)
		pError2 = binom.pmf(cantFinal,cantBlancas1+cantBlancas2,pBlanca)
		pError3 = (binom.pmf(cantBlancas1,cantFinal,pBlanca)+binom.pmf(cantBlancas2,cantFinal,pBlanca))/2
		
		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError3,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	elif i==34:
		#Suma de binomiales negativas (variación) : 5.5.5
		#[Probabilidad de obtener una pelota blanca, Cantidad blancas bolsa 1, cantidad blancas bolsa 2]
		lista = [[0.4,10,15],[0.3,6,8],[0.6,10,10],[0.4,15,12],[0.7,10,8],[0.5,12,14]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pBlanca = params[0]
		cantBlancas1 = params[1]
		cantBlancas2 = params[2]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Bolsas de pelotas"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "Suponga que se tiene dos bolsas con pelotas blancas y negras. La probabilidad de sacar una bola blanca de cualquiera de las dos bolsas es "+str(pBlanca)+". Si se sacan, con reemplazo, pelotas de la primera bolsa hasta alcanzar "+str(cantBlancas1)+" blancas, y de la segunda hasta alcanzar "+str(cantBlancas2)+" blancas, ¿cuál es la cantidad de pelotas que esperaría sacar en total de las dos bolsas?"+"\n"

		cantReal = (cantBlancas1+cantBlancas2)*(1-pBlanca)/pBlanca + (cantBlancas1+cantBlancas2)
		cantError1 = (cantBlancas1+cantBlancas2)*pBlanca
		cantError2 = (cantBlancas1+cantBlancas2)*(1-pBlanca)/pBlanca 
		cantError3 = (cantBlancas1+cantBlancas2)

		cifras=0
		if pos%2==0:
			respuestas += "*a. "+str(int(round(cantReal,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(int(round(cantError3,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "c. "+str(int(round(cantError1,cifras)))+"\n"
			respuestas += " "+"\n"		
			respuestas += "d. "+str(int(round(cantError2,cifras)))+"\n"

		else:
			respuestas += "a. "+str(int(round(cantError3,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "b. "+str(int(round(cantError2,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(int(round(cantReal,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(int(round(cantError1,cifras)))+"\n"

		return [titulo, version, pregunta, respuestas] 


	#ADICIONALES


	elif i==35: 
		# Binomial condicional
		#[Probabilidad de fallo, cantidad minima de fallos obersvados, cantidad de fallos, tamaño muestra, objeto]	
		lista = [[0.4,2,6,10, "una impresora"],[0.3,3,8,12, "un celular"],[0.6,2,6,10, "una máquina de escribir"],[0.4,3,7,11,"una guitarra"],[0.7,2,6,8,"un portafolios"],[0.5,3,5,6,"una computadora"]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pFallo = params[0]
		cantMinimaFallos = params[1]
		cantFallos = params[2]
		tamMuestra = params[3]
		objeto = params[4]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Fallo de componentes"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"
	
		pregunta += "Un cierto componente de "+objeto+" falla con una probabilidad de "+str(pFallo)+". Si se toman "+str(tamMuestra)+" de estos objetos y se ve que hay al menos "+str(cantMinimaFallos)+" con la falla, ¿cuál es la probabilidad que "+str(cantFallos)+" objetos de la muestra tengan el fallo?"+"\n"

		pReal = binom.pmf(cantFallos, tamMuestra, pFallo) / (1-binom.cdf(cantMinimaFallos-1,tamMuestra,pFallo))
		pError1 = binom.pmf(cantFallos, tamMuestra, pFallo)
		pError2 = binom.pmf(cantFallos, tamMuestra, pFallo) / (1-binom.cdf(cantMinimaFallos,tamMuestra,pFallo))
		pError3 = binom.pmf(cantMinimaFallos, tamMuestra, pFallo) / (1-binom.cdf(cantFallos-1,tamMuestra,pFallo))

		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError3,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]


	elif i==36:
		#Proporción de fichas (binom)
		#[Proporción de fichas rojas, cantidad muestra, cantidad fichas negras]
		lista = [[0.4,20,10],[0.3,15,7],[0.5,8,3],[0.6,12,9],[0.7,15,9]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pRoja = params[0]
		cantMuestra = params[1]
		cantNegras = params[2]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Fichas de Damas Chinas"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"
		
		pregunta += "Una bolsa contiene fichas rojas y negras. La probabilidad de sacar una ficha roja de esta bolsa es de "+str(pRoja)+". Si se sacan aleatoriamente "+str(cantMuestra)+" fichas de esta bolsa, ¿cuál es la probabilidad que haya menos de "+str(cantNegras)+ " fichas negras?"+"\n"
	
		
		pReal = binom.cdf(cantNegras-1,cantMuestra,1-pRoja)
		pError1 = 1-binom.cdf(cantNegras-1,cantMuestra,pRoja)
		pError2 = binom.cdf(cantNegras,cantMuestra,1-pRoja)
		pError3 = 1-binom.cdf(cantNegras,cantMuestra,1-pRoja)
		
		cifras=5

		if pos%2==0:
			respuestas += "*a. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(pReal,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	elif i==37:
		#Proporción de fichas (hipergeom)
		#[Proporción de fichas rojas, cantidad muestra, cantidad fichas negras, cantidad total de fichas en la bolsa]
		lista = [[0.4,20,10,30],[0.3,15,7,20],[0.5,8,3,16],[0.6,12,6,15],[0.7,15,8,20]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		pRoja = params[0]
		cantMuestra = params[1]
		cantNegras = params[2]
		cantTotalFichas = params[3]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Fichas de Damas Chinas"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"
		
		pregunta += "Una bolsa contiene "+str(cantTotalFichas)+" fichas rojas y negras. La proporción de fichas rojas es de "+str(int(10*pRoja))+ " por cada 10. Si se sacan aleatoriamente "+str(cantMuestra)+" fichas de esta bolsa, ¿cuál es la probabilidad que haya menos de "+str(cantNegras)+ " fichas negras?"+"\n"
	
		
		pReal = hypergeom.cdf(cantNegras-1,cantTotalFichas,cantTotalFichas-pRoja*cantTotalFichas,cantMuestra)
		pError1 = binom.cdf(cantNegras-1,cantMuestra,pRoja)
		pError2 = hypergeom.cdf(cantNegras,cantTotalFichas,pRoja*cantTotalFichas,cantMuestra)
		pError3 = binom.cdf(cantNegras,cantMuestra,1-pRoja)
		
		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(pError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError2,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(pError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(pError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(pReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(pError1,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]
	
	elif i==38:
		#Pelotas de colores (Variación): 5.3.2
		#[Cantidad pelotas azules, cantidad pelotas rojas, cantidad muestra, cantidad limite, color pregunta]
		lista = [[5,5,7,"azules"],[4,6,6,"rojas"],[7,11,7,"azules"],[8,6,5,"rojas"],[8,4,6,"azules"]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		cantAzul = params[0]
		cantRoja = params[1]
		cantMuestra = params[2]
		STRcolor = params[3]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Pelotas de colores"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"	
		
		pregunta += "En una caja hay "+str(cantAzul)+" pelotas azules y "+str(cantRoja)+" pelotas rojas. Si se sacan "+str(cantMuestra)+" pelotas de la caja, ¿cuál es el valor esperado de pelotas "+STRcolor+" que esperaría ver?"+"\n"
	
		cantRealAzul = cantMuestra*(cantAzul/(cantAzul+cantRoja))
		cantRealRoja = cantMuestra*(cantRoja/(cantAzul+cantRoja))
		cantError1 = cantMuestra*(cantAzul/cantRoja)
		cantError2 = cantMuestra*(cantRoja/cantAzul)
		
		cifras=2

		if STRcolor == "rojas": 
			if pos%2==0:
				respuestas += "a. "+str(round(cantError1,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. "+str(round(cantError2,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*c. "+str(round(cantRealRoja,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "d. "+str(round(cantRealAzul,cifras))+"\n"

			else:
				respuestas += "*a. "+str(round(cantRealRoja,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. "+str(round(cantError2,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "c. "+str(round(cantRealAzul,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "d. "+str(round(cantError1,cifras))+"\n"

		else: 
			if pos%2==0:
				respuestas += "*a. "+str(round(cantRealAzul,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. "+str(round(cantError2,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "c. "+str(round(cantError1,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "d. "+str(round(cantRealRoja,cifras))+"\n"

			else:
				respuestas += "a. "+str(round(cantRealRoja,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. "+str(round(cantError2,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*c. "+str(round(cantRealAzul,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "d. "+str(round(cantError1,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]


	elif i==39:
		#Personas entrando a un centro comercial (Variación)
		#[Promedio entrada 1 por hora, promedio entrada 2 por hora, cantidad horas a evaluar]
		lista = [[12,10,3],[15,15,2],[10,8,4],[5,4,5],[8,10,3]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		promEntrada1 = params[0]
		promEntrada2 = params[1]
		cantHoras = params[2]	
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Entradas a un centro comercial"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "En un centro comercial pequeño hay dos entradas. En promedio, entran "+str(promEntrada1)+" personas por hora por la primera y "+str(promEntrada2)+" personas por hora por la segunda. En un periodo de "+str(cantHoras)+" horas, ¿cuántas personas esperaría que entren a tal centro comercial?"+"\n"

		cantReal = (cantHoras*promEntrada1+cantHoras*promEntrada2) 
		cantError1 = cantHoras*promEntrada1*promEntrada2
		cantError2 = promEntrada2*promEntrada1
		cantError3 = (promEntrada1+promEntrada2)

		cifras=0
		if pos%2==0:
			respuestas += "a. "+str(int(round(cantError3,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(int(round(cantReal,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "c. "+str(int(round(cantError1,cifras)))+"\n"
			respuestas += " "+"\n"		
			respuestas += "d. "+str(int(round(cantError2,cifras)))+"\n"

		else:
			respuestas += "a. "+str(int(round(cantError3,cifras)))+"\n"
			respuestas += " "+"\n"			
			respuestas += "b. "+str(int(round(cantError2,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(int(round(cantReal,cifras)))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(int(round(cantError1,cifras)))+"\n"

		return [titulo, version, pregunta, respuestas] 


	elif i==40:
		#Media de una distribución de Poisson
		#[N tal que p(N+1)=p(N), texto pregunta]
		lista = [[11,"el valor esperado"],[105,"el valor esperado"],[7,"la varianza"],[59,"la varianza"],[306,"la varianza"],[10,"el valor esperado"],[74,"el valor esperado"]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]	
		N = params[0]
		texto = params[1]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Media de una distribución"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"

		pregunta += "Suponga que $X$ es una variable aleatoria con distribución de Poisson tal que $Pr(X="+str(N)+")=Pr(X="+str(N+1)+")$. ¿Cuál es "+texto+" de esta variable aleatoria?"+"\n"

		respReal = N+1
		respError1 = N
		respError2 = 1/N
		respError3 = 1/(math.exp(1/N)-1)

		cifras=5

		if pos%2==0:
			respuestas += "a. "+str(round(respError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*b. "+str(round(respReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(respError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(respError2,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(respError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(respError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*c. "+str(round(respReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(respError1,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]

	elif i==43:
		#Pelotas de colores (variación) : 5.3.2
		#[Cantidad pelotas azules, cantidad pelotas rojas, cantidad muestra, cantidad limite, color pregunta]
		lista = [[15,26,7,3,"azules"],[14,26,6,3,"rojas"],[17,11,7,4,"azules"],[28,16,5,3,"rojas"],[18,4,6,4,"azules"]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		cantAzul = params[0]
		cantRoja = params[1]
		cantMuestra = params[2]
		cantLim = params[3]
		STRcolor = params[4]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Pelotas de colores"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"	
		
		pregunta += "En una caja hay "+str(cantAzul)+" pelotas azules y "+str(cantRoja)+" pelotas rojas. Si se sacan "+str(cantMuestra)+" pelotas de la caja sin reemplazo, ¿cuál es la cantidad esperada de pelotas "+STRcolor+"?"+"\n"
	
		cantRealAzul = cantMuestra*cantAzul/(cantRoja+cantAzul)
		cantRealRoja = cantMuestra*cantRoja/(cantRoja+cantAzul)
		cantError1 = cantMuestra*cantAzul/(cantRoja)
		cantError2 = cantMuestra*cantRoja/(cantAzul)
		
		cifras=2

		if STRcolor == "rojas": 
			if pos%2==0:
				respuestas += "a. "+str(round(cantError1,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*b. "+str(round(cantRealRoja,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "c. "+str(round(cantRealAzul,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "d. "+str(round(cantError2,cifras))+"\n"

			else:
				respuestas += "*a. "+str(round(cantRealRoja,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. "+str(round(cantRealAzul,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "c. "+str(round(cantError1,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "d. "+str(round(cantError2,cifras))+"\n"

		else: 
			if pos%2==0:
				respuestas += "a. "+str(round(cantError1,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. "+str(round(cantError2,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "c. "+str(round(cantRealRoja,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*d. "+str(round(cantRealAzul,cifras))+"\n"

			else:
				respuestas += "a. "+str(round(cantRealRoja,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "b. "+str(round(cantError2,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "*c. "+str(round(cantRealAzul,cifras))+"\n"
				respuestas += " "+"\n"
				respuestas += "d. "+str(round(cantError1,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]


	elif i==44:
		#Proporción de árboles (variacion) : 5.4.13
		#[Proporción, tamaño muestra, cantidad limite]
		lista = [[0.1,100,50],[0.05,200,70],[0.12,100,60],[0.11,100,80],[0.13,500,6],[0.09,100,70]]
		pos=rdm.randint(1,len(lista))			
		params = lista[pos-1]
		proporcion = params[0]
		tamMuestra = params[1]
		cantLimite = params[2]
		titulo = ""
		version = ""
		pregunta = ""
		respuestas = ""
		titulo += "Árboles con frutos azules"+"\n"
		version += "%Jeronimo Valencia, Tipo "+str(i)+", ver 0"+str(pos)+"\n"
		
		pregunta += "En un bosque, la proporción de árboles que dan un fruto azul es de "+str(proporcion)+". ¿Cuántos árboles hay que analizar si se quieren encontrar "+str(cantLimite)+" árboles con este tipo de fruto?"+"\n"
	
		cantReal = cantLimite/proporcion
		cantError1 = 100*cantLimite*proporcion
		cantError2 = cantLimite/((proporcion)**2)
		cantError3 = cantLimite/(1-proporcion)

		cifras=0

		if pos%2==0:
			respuestas += "*a. "+str(round(cantReal,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(cantError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(cantError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "d. "+str(round(cantError1,cifras))+"\n"

		else:
			respuestas += "a. "+str(round(cantError2,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "b. "+str(round(cantError1,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "c. "+str(round(cantError3,cifras))+"\n"
			respuestas += " "+"\n"
			respuestas += "*d. "+str(round(cantReal,cifras))+"\n"
		
		return [titulo, version, pregunta, respuestas]	



##############################################################################################################################

#Seleccionar los ejercicios a imprimir en el documento .docx según la siguiente lista: 

#Wackerly-Mendehall-Scheaffer - Estadística Matemática

#Sección 3.3 (El valor esperado de una variable aleatoria o una función de una variable aleatoria) : 1-3
#Sección 3.4 (Distribución binomial) : 4-6
#Sección 3.5 (Distribución geométrica) : 7-10
#Sección 3.6 (Distribución binomial negativa) : 11-12, 41-42
#Sección 3.7 (Distribución hipergeométrica) : 13-16
#Sección 3.8 (Distribución de Poisson) : 17-20
#Sección 3.9 (Funciones generadoras de momentos): 45-50

#DeGroot & Schervish - Probability and Statistics 

#Section 5.2 (Bernoulli and binomial distribution): 21-24, 44
#Section 5.3 (Hypergeometric distribution): 25-26, 43
#Section 5.4 (Poisson distribution) : 27-30
#Se4ction 5.5 (Negative binomial distribution): 31-34

#Adicionales: 

# Distribución binomial: 35, 36, 
# Distribución hipergeométrica: 37, 38
# Distribución de Poisson: 39,40


#LISTA
#ejercicios = list(range(31,43))


#MANUAL
ejercicios = [50]

cantidades = [30]

#cantidades = [0,0,1]

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

str4 = "\ "+"begin{enumerate}[label=\ "+"arabic"+"*]"
print(str4.replace(" ",""))

contador=0
for i in ejercicios: 
	for cont in range(1,cantidades[contador]+1):
		data = RandomProblemGenerator(i)
		#Titulo y version del problema
		#print(data[0])
		#print(data[1])
		print("\item "+data[2])
		print(data[3])
	contador += 1

print("\end{enumerate}")

print("\end{document}")
















