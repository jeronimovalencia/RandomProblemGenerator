# RandomProblemGenerator

Este repositorio se compone de archivos para la creación de documentos de Word que son aceptados por Respondus para cargar preguntas de selección múltiple con única respuesta a SicuaPlus. Los temas de tales preguntas son **distribuciones de probabilidad discretas** y se basan en probabilidad de eventos, probabilidades acumuladas y condicionales, y valores esperados y varianzas. El principio del proyecto es generar ejercicios de un mismo estilo pero con distintas respuestas numéricas. Todas las variaciones de los problemas pueden ser ajustadas en la *lista* que se presenta al inicio de cada ejercicio. Asimismo, es posible variar el orden de las respuestas y la posición de la correcta. 

### RandomProblemGenerator.py

Es el archivo de Python que imprime, en formato .tex, las preguntas deseadas. En él se encuentra una lista de las distintas distriubuciones tratadas, y en un arreglo de números se eligen los ejercicios a generar. 

### generator.mk

Este archivo Makefile compila el programa anterior con **python3**, su resultado lo envía a un archivo de texto que se compila con **pandoc** para generar el archivo .docx deseado. 

### Tarea_.docx

Son ejemplos de tipos de archivo que genera el programa. 
