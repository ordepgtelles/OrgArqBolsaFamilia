import struct
import hashlib
import os
import csv

hashSize = 17035841
CompararName = "bolsa-jan-2019.csv"
HashName = "bolsa-hash.dat"
DiferencaName = "bolsa-diferenca.dat"
indexFormat = "11sLL"
keyColumnIndex = 5

indexStruct = struct.Struct(indexFormat)


def h(key):
    global hashSize
    return int(hashlib.sha1(key).hexdigest(), 16) % hashSize


arqComparar = open(CompararName,"r")


arqHash = open(HashName, "r+b")


saida = open(DiferencaName, "a+")

#adiciona a primeira linha como cabecalho
cabecalho = arqComparar.readline()
saida.write(cabecalho)

while True:
    #le a linha do arq que sera percorrido sequencialmente
    linha = arqComparar.readline()

    if linha == "": # EOF
        break
    record = linha.split(";")
    #vai pegar a posicao que deveria ficar no arquivo hash
    nisComparar = record[keyColumnIndex].replace('"','')
    p = h(nisComparar)
    offset = p * indexStruct.size
    a = 1
    while True:
        #posiciona o ponteiro onde este nis deveria #estar no arq Hash
        arqHash.seek(offset, os.SEEK_SET)
        indexRecord = indexStruct.unpack(arqHash.read(indexStruct.size))
        #verifica se o nis do arqComparar igual ao nis do arqHash
        if indexRecord[0] == str(nisComparar):
            break
        offset = indexRecord[2]
        if offset == 0:
            saida.write(linha)
            break
        a += 1

arqComparar.close()
arqHash.close()
saida.close()
