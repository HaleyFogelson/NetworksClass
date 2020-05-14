import socket
import sys
import random
import re
import hashlib
#Matching the global variables
ipAddr = 'localhost'
defaultPort = 12001
bufferMax=4096

def getSolution(sentence):
        if '+' in sentence:
                spot=sentence.find('+')
                return int(sentence[0,spot]) + int(sentence[spot+1, len(sentence)])
        if '*' in sentence:
                spot=sentence.find('*')
                return int(sentence[0,spot]) * int(sentence[spot+1, len(sentence)])
        if '-' in sentence:
                spot=sentence.find('-')
                return int(sentence[0,spot]) - int(sentence[spot+1, len(sentence)])
        if '/' in sentence:
                spot=sentence.find('/')
                return int(sentence[0,spot]) / int(sentence[spot+1, len(sentence)])

if __name__ == '__main__':
        clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientSocket.connect((ipAddr,defaultPort))
        inputData="ece2540 HELLO 001458412" #makes the input
        clientSocket.send(inputData.encode()) #sends the message and encodes it
        a=""
        while 1:
                expr=clientSocket.recv(bufferMax)
                x=expr.decode() #decodes the expression
                if "BYE" in x:
                        break
                solution=getSolution(x)
                print(getSolution(x))
                clientSocket.send(str(solution.encode()))# sends solutio to server


        secretmessage=x #gets the secret code
        y=secretmessage.decode()
        print(y)#print secret flag
        s.close() #closes the connection