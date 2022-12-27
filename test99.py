#Input: M customers, N trucks, P drones
import random
#Nhập số các phương tiện
M=int(input("Nhập số các customres: "))
N=int(input("Nhập số các trucks: "))
P=int(input("Nhập số các drones: "))
print("________________________________________")

geneset1=[]
geneset2=[]
for i in range(0,N-1):
    geneset1.append(0)
    geneset2.append(0)
for i in range(1,M+1):
    geneset1.append(i)
    geneset2.append(i)
#length=M+N-1
def initialize_chromosomes(length):
    chromosomes=[]
    for i in range(0,length):
        chromosomes.append([])
    for i in range(0,length):
        x=random.sample(geneset2,1)
        chromosomes[i].extend(x)
        chromosomes[i].append(random.random())
        geneset2.remove(x[0])
    return chromosomes
"""
x=initialize_chromosomes(M+N-1)
print("Day so vua nhap la: ")
for j in range(0,2):
    for i in range(0,M+N-1):
        print("%.2f    "%x[i][j], end='')
    print()
"""
