#!/usr/bin/env python3
#coding:utf-8

# Script name: codec
# Description: programme avec Clé de chiffrement matricielle
# Made by: Ezeqielle & Batmine3
# Begin: 14/12/2019
# End: 11/01/2020

# /!\ ne pas oublier d'enlever les print() de debug a la fin /!\
#Add creation de matrice
import os
import numpy as np
import easygui
import tkinter as tk

#main
def main():
    ui = tk.Tk()
    ui.geometry('300x100')
    ui.title('Secu Codec')

    row = tk.Frame(ui)
    tk.Button(row, text='Encode', command=encodeFile, fg='green', bg='black', width="40", height="6").pack(side=tk.LEFT)
    tk.Button(row, text='Decode', command=decodeFile, fg='red', bg='black', width="40", height="6").pack(side=tk.LEFT)
    row.pack()

    ui.mainloop()

#get matrix
def getMatrix():
    filename = easygui.fileopenbox('','','*.*')
    filename = os.path.realpath(filename)
    matrix = open(filename, 'r').read()
    matrix = matrix.split('[')[1].split(']')[0]
    matrix = matrix.replace(' ','')

    matrixArray = []
    matrixArray.append(list(matrix[:8]))
    matrixArray[0] = [int(count) for count in matrixArray[0]]
    matrixArray.append(list(matrix[8:16]))
    matrixArray[1] = [int(count) for count in matrixArray[0]]
    matrixArray.append(list(matrix[16:24]))
    matrixArray[2] = [int(count) for count in matrixArray[0]]
    matrixArray.append(list(matrix[24:32]))
    matrixArray[3] = [int(count) for count in matrixArray[0]]
    
    return matrixArray

#encode
def encodeFile():
    easygui.msgbox("Select matrix: ")
    matrix = np.array(getMatrix())
    easygui.msgbox("Select file: ")
    filename = easygui.fileopenbox('','','*.*')
    filename = os.path.relpath(filename)

    file = open(filename, "r")
    fileContent = file.read()
    fileContent = [bin(ord(x))[2:].zfill(8) for x in fileContent]

    for contents in fileContent:
        contents = list(contents)
        contents = [int(i) for i in contents]
        u1 = np.array(contents[:4])
        x1 = str(np.array(1 * np.dot(u1, matrix))).strip('[]').replace(' ','')
        u2 = np.array(contents[4:])
        x2 = str(np.array(1 * np.dot(u2, matrix))).strip('[]').replace(' ','')

        with open(filename+'c', 'a') as encoded:
            encoded.write(x1)
            encoded.write(x2)        

#matrix ID
def matrixID(matrix):
    matrix = np.array(matrix, dtype = int)
    one = two = tree = four = 0
    i = 0
    while i < 7:
        if matrix[0][i] == 1 and matrix[1][i] == 0 and matrix[2][i] == 0 and matrix[3][i] == 0:
            one = i
        if matrix[0][i] == 0 and matrix[1][i] == 1 and matrix[2][i] == 0 and matrix[3][i] == 0:
            two = i
        if matrix[0][i] == 0 and matrix[1][i] == 0 and matrix[2][i] == 1 and matrix[3][i] == 0:
            tree = i
        if matrix[0][i] == 0 and matrix[1][i] == 0 and matrix[2][i] == 0 and matrix[3][i] == 1:
            four = i
        i += 1
    return  [one,two,tree,four]

#decode
def decodeFile():
    easygui.msgbox("Select matrix: ")
    matrix = np.array(getMatrix())
    easygui.msgbox("Select file: ")
    filename = easygui.fileopenbox('','','*.*')
    filename = os.path.relpath(filename)

    filename += "d"

    file = open(filename, "r")
    fileContent = file.read()

    fileContent = [fileContent[i:i + 16] for i in range(0, len(fileContent), 16)]
    idMatrix = matrixID(matrix)
    decoded = ""
    
    for contents in fileContent:
        x1 = contents[:8]
        x2 = contents[8:]

        for i in range(4):
            decoded += x1[(idMatrix[i])]
        for i in range(4):
            decoded += x2[(idMatrix[i])]
    with open(filename, 'a') as decode:
        decode.write(bits_strings(decoded))

#convert
def bits_strings(bitsContent):
    msg = ""
    while bitsContent != "":
        i = chr(int(bitsContent[:8],2))
        msg = msg + i
        bitsContent = bitsContent[8:]
    return msg

if __name__ == "__main__":
    main()


'''
def matrixEncodeSize(matrixUsed):
    keyOpen = open("key/"+matrixUsed+".txt", "r")
    workKey = keyOpen.read()
    keyOpen.close()
    begin = workKey.index("[")
    end = workKey.index("]")
    key = workKey[begin+1:end]
    key = key.split(" ")
    matrixSize = len(key)
    return matrixSize

def matrixEncode(matrixUsed):
    keyOpen = open("key/"+matrixUsed+".txt", "r")
    workKey = keyOpen.read()
    keyOpen.close()
    begin = workKey.index("[")
    end = workKey.index("]")
    key = workKey[begin+1:end]
    key = key.split(" ")
    return key

#matrix decode
def matrixDecode(matrixUsed):
    keyOpen = open("key/"+matrixUsed+".txt", "r")
    workKey = keyOpen.read()
    keyOpen.close()
    print(workKey)
    begin = workKey.index("[")
    end = workKey.index("]")
    key = workKey[begin+1:end]
    key = key.split(" ")
    matrixSize = len(key)
    print(matrixSize)
    matrixID(matrixSize)

#file_encode
def fileEncode(fileUsed, matrixSize, key):
    fileOpen = open("file_encode/"+fileUsed, "rb")  #ouverture du fichier
    workFile = fileOpen.read()                      #passage des data dans une variable
    contenerFile = list(workFile)                   #conversion en list
    bits = map(bytes, contenerFile)                 #conversion en bytes

    fileExtension = fileUsed.split(".")             #recuperation de l'extension
    fileExtension = fileExtension[1]                #
    workFileLength = len(workFile)
    fileOpen.close()
    bits = []
    for i in range(workFileLength):
        contenerFile[i] = bin(contenerFile[i])
        bits = bits + list(contenerFile[i])
    
    
    deleteBinary(bits)
    
    size = len(bits)
    
    ourDict = {}
    iteration = size / matrixSize

    if iteration > round(iteration):
        iteration = round(iteration) + 1
    else:
        iteration = round(iteration)
    
    for i in range( int(iteration) ):
        ourDict["X" + str(i)] = getValues( size, matrixSize, i, bits) # 3 4 {0, 1, 2}


    fileOpen = open("file_encode/"+fileUsed+"c", "w+")
    fileContent = ""
    for x in ourDict:
        for value in ourDict[x]:
            for result in value:
                for matrix in key:
                    for multiplier in matrix:
                        fileContentTmp = fileContent + str(int(multiplier) ^ int(result))
    fileContent = ""
    lenght = len(fileContentTmp)

    while 0 <= lenght - 1:
        convert = ""
        j = 0
        for j in range(4):
            if lenght + j < lenght:
                convert = convert + str(fileContentTmp[lenght - j])

        fileContent = fileContent + str(binascii.a2b_uu(convert))
        lenght = lenght - j
    
    print(fileContent)
    fileOpen.write(fileContent)
    fileOpen.close()

#decouper le fichier par segment binaire de taille Gx trouver au dessus
#compter la taille de la liste pour la longueur de la boucle


def deleteBinary(bits):                                             #fonction pour supprimer les identifiants binaires ('0b')
    i = 0
    size = len(bits)
    while i + 1 < size:
        delete = "" + str(bits[i]) + str(bits[i + 1])
        if delete == '0b':
            bits.pop(i)
            bits.pop(i)
            size -= 2
        else:
            i += 1

def getValues(size, matrixSize, endValue, contenerFile):                      
    if endValue != 0:
        startValue = endValue * matrixSize
        endValue = matrixSize * (endValue + 1)
    elif endValue == 0:
        startValue = 0
        endValue = matrixSize                                                           
    result = ""
    while (startValue < endValue and startValue < size):
        if result == "":
            result = result + "" + str(contenerFile[startValue])
        else:
            result = result + str(contenerFile[startValue])
        startValue += 1
    return result



#file_decode
def fileDecode(fileUsed):
    fileOpen = open("file_decode/"+fileUsed, "rb")
    workFile = fileOpen.read()
    fileExtension = fileUsed.split(".")
    fileExtension = fileExtension[1]
    print(fileExtension)
    
#matrix ID
def matrixID(matrixSize):
    print(" Entrez la cle d'encodage de la matrice : ")
    c = 0
    i = 0
    encodeKey = [0] * matrixSize
    while (i < matrixSize):
        c += 1
        G = input("column "+str(c)+" : ")
        encodeKey[i] = G
        i += 1
    print(encodeKey)
#recuperation de la matrice identitee

#matrix calculation
def matrixMul():
    ""

#key creation
def keyCreation():
    ""

q = 0
while (q == 0):
    x = input(" Select you option : \n 1 - Encode file \n 2 - Decode file \n 3 - Create matrix \n 4 - Quit \n\n Your option : ")
    if (x == "1"):
        print("\n encode file : \n")
        matrix = input(" Entrez le nom de la matrice a selectionner : ")
        matrixKey = matrixEncode(matrix)
        matrixSize = matrixEncodeSize(matrix)
        file = input(" Entrez le nom du fichier avec son extension: ")
        fileEncode(file, matrixSize, matrixKey)
    elif (x == "2"):
        print("\n decode files : \n")
        matrix = input(" Entrez le nom de la matrice a selectionner : ")
        matrixDecode(matrix)
        file = input(" Entrez le nom du fichier avec son extension: ")
        fileDecode(file)
    elif (x == "3"):
        print("\n creation matrix : \n")
    elif (x == "4"): 
        a = input(" Are you sure want exit ? (y/n) : ")
        if(a == "y" or a == "Y" or a == "yes" or a == "Yes" or a == "YES"):
            q = 1
        else:
            q = 0
    else:
        print(" invalid choice")
'''