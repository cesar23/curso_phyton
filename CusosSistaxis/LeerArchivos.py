#!C:/Users/user/AppData/Local/Programs/Python/Python36-32/python.exe
#-*- coding: utf-8 -*-


#-----------------FUENTES
#https://programacion.net/articulo/como_leer_archivos_de_texto_extremadamente_grandes_utilizando_python_1492


import codecs
from itertools import islice
#para el sleep
import time
#---------------LEER LOS 500 PRIMERAS LINEAS
# input_file = open('hg38.txt', 'r')
# output_file = codecs.open('output.txt', 'w', "utf-8")
#
# for lines in range(500):
#     line = input_file.readline()
#     #lo guardo en otro archivo
#     output_file.write(line)

#-----------------PARA LEER UN ARCHIVO POR PARTES
# input_file = open('C:\\Users\\user\\Downloads\\Compressed\\padron_reducido_ruc.txt', errors='ignore')
# #input_file = codecs.open('C:\\Users\\user\\Downloads\\Compressed\\padron_reducido_ruc.txt', 'r')
# #input_file = open('archivos/demo.txt', 'r')
# output_file = codecs.open('output.txt', 'w', "utf-8")
#
# while(1):
#     for lines in range(50):
#         print (input_file.readline())
#     user_input = input('Type STOP to quit, otherwise press the Enter/Return key ')
#     if user_input == 'STOP':
#         break
#
#
# print(len(input_file.readlines()))  # devolvera 3
#
# input_file.close()

#-------------para leer un archivo desde un numero de linea
# f=open('C:\\Users\\user\\Downloads\\Compressed\\padron_reducido_ruc.txt','r')
# it=islice(f,5,None)
# for linea in it:
#   time.sleep(5)
#   print (linea)

#   ------------- LEER LINEA EN CONCRETO
with open('C:\\Users\\user\\Downloads\\Compressed\\padron_reducido_ruc.txt', "r", errors="surrogateescape") as f:
    print(len(f.readlines()))
    # lines = f.readlines()
    # print (lines[1])
    # print (lines[3] )#Linea 4