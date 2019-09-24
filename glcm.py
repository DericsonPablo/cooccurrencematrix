# -*- coding: UTF-8 -*-
from skimage.feature import greycomatrix, greycoprops #funcao do pacote skimage para calcular a matriz GLCM e os atributos da matriz
from skimage.io import imread #importando a funcao imread para leitura da imagem
from skimage.color import rgb2grey #importando funcao rgb2grey que converte a imagem para cinza
import numpy as np
from skimage import img_as_uint
import os.path

image_path = "/home/dericson/Downloads/ic/homem1.tiff" #endereco da imagem
image = imread(image_path) #leitura da imagem
image_gray = rgb2grey(image) #transformar de RGB para nivel de cinza
#distancia escolhida entre os pixels para fazer a relação da GLCM é 1
print image_gray
matrix = greycomatrix(image_gray,[1],[0]) #calculo da matriz em 0 graus
props = np.zeros((6)) # vetor para armazenar atributos (no caso o vetor que identifica os dados do usuario)
props[0] = greycoprops(matrix, 'contrast') #calcula constraste
print props[0]
props[1] = greycoprops(matrix, 'dissimilarity') #calcula a dissimilaridade
print props[1]
props[2] = greycoprops(matrix, 'homogeneity') #calcula homogeneidade
print props[2]
props[3] = greycoprops(matrix, 'energy') #calcula energia
print props[3]
props[4] = greycoprops(matrix, 'correlation') #calcula correlacao
print props[4]
props[5] = greycoprops(matrix, 'ASM') #calcula o segundo momento angular
print props[5]

#for i in range(6): #imprimindo vetor com os resultados de cada função, sendo o vetor a identificação do usuário
#	print props[i]

#with open("/home/dericson/Downloads/ic/resultado.txt", "w") as stream:
 #   for x in string_save.split():
  #      print(props, file="/home/dericson/Downloads/ic/resultado.txt")


#if os.path.isfile('/home/dericson/Downloads/ic/Resultado.txt'): #se já existe o arquivo
#	arquivo = open('/home/dericson/Downloads/ic/Resultado.txt', 'r') # Abra o arquivo (leitura)
#	conteudo = arquivo.readlines()
#	conteudo.append(props)   # inserindo o vetor
#	arquivo = open('/home/dericson/Downloads/ic/Resultado.txt', 'w') # Abre novamente o arquivo (escrita)
#	arquivo.writelines(props)    # escreva o conteúdo criado anteriormente nele.
#	arquivo.close()
#else:
#	arquivo = open('/home/dericson/Downloads/ic/Resultado.txt', 'w') #cria um arquivo vazio
#	arquivo.close()
