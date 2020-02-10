#!/usr/bin/env python3
# coding:utf-8

# Script name: codec
# Description: programme avec Clé de chiffrement matricielle
# Made by: Ezeqielle
# Begin: 14/12/2019
# End: 11/01/2020

# /!\ ne pas oublier d'enlever les print() de debug a la fin /!\
# Add creation de matrice
import os
import numpy as np
import easygui
import tkinter as tk


# main
def main():
    ui = tk.Tk()
    ui.geometry('300x100')
    ui.title('Secu Codec')

    row = tk.Frame(ui)
    tk.Button(row, text='Encode', command=encodeFile, fg='green', bg='black', width="40", height="6").pack(side=tk.LEFT)
    tk.Button(row, text='Decode', command=decodeFile, fg='red', bg='black', width="40", height="6").pack(side=tk.LEFT)
    row.pack()

    ui.mainloop()


# get matrix
def getMatrix():
    filename = easygui.fileopenbox('', '', '*.*')
    filename = os.path.realpath(filename)
    matrix = open(filename, 'r').read()
    matrix = matrix.split('[')[1].split(']')[0]
    matrix = matrix.replace(' ', '')

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


# encode
def encodeFile():
    easygui.msgbox("Select matrix: ")
    matrix = np.array(getMatrix())
    easygui.msgbox("Select file: ")
    filename = easygui.fileopenbox('', '', '*.*')
    filename = os.path.relpath(filename)

    file = open(filename, "r")
    fileContent = file.read()
    fileContent = [bin(ord(x))[2:].zfill(8) for x in fileContent]

    for contents in fileContent:
        contents = list(contents)
        contents = [int(i) for i in contents]
        u1 = np.array(contents[:4])
        x1 = str(np.array(1 * np.dot(u1, matrix))).strip('[]').replace(' ', '')
        u2 = np.array(contents[4:])
        x2 = str(np.array(1 * np.dot(u2, matrix))).strip('[]').replace(' ', '')

        with open(filename + 'c', 'a') as encoded:
            encoded.write(x1)
            encoded.write(x2)

        # matrix ID


def matrixID(matrix):
    matrix = np.array(matrix, dtype=int)
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
    return [one, two, tree, four]


# decode
def decodeFile():
    easygui.msgbox("Select matrix: ")
    matrix = np.array(getMatrix())
    easygui.msgbox("Select file: ")
    filename = easygui.fileopenbox('', '', '*.*')
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


# convert
def bits_strings(bitsContent):
    msg = ""
    while bitsContent != "":
        i = chr(int(bitsContent[:8], 2))
        msg = msg + i
        bitsContent = bitsContent[8:]
    return msg


if __name__ == "__main__":
    main()