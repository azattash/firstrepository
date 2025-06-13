import numpy
import numpy as np
m=2
n=3
X = np.zeros([m, n], "f")
q = np.zeros([n], "f")
V = np.zeros([n], "f")
VN1 = np.zeros([n], "f")

X[0][0]=0.8
X[0][1]=0.4
X[0][2]=0.7

X[1][0]=0.2
X[1][1]=0.6
X[1][2]=0.3

XT=X.transpose()
print("X",X)
print("XT",XT)

A = np.zeros([m, m], "f")
B = np.zeros([n, n], "f")
A=X@XT
B=XT@X
print("A",A)
print("B",B)
evalueA, evectorA=numpy.linalg.eig(A)
evalueB, evectorB=numpy.linalg.eig(B)
print("Собственный вектор")
print("Alamda",evalueA)
print("Avector",evectorA)

print("Blamda",evalueB)
print("Bvector",evectorB)

for i in range(n):
    V[i]=evectorB[i][0]
summ=0
for i in range(n):
    summ=summ+V[i]
for i in range(n):
    V[i]=V[i]/summ
    
print('Собственный вектор нормированный V',V)
print("В книге (0.36,0.3,0.34) ")
##
##print("Blamda",evalueB)
##print("Bvector",evectorB)
##
##arr=np.argmax(evalueB)
##print('arr',arr)
##for i in range(n):
##    VB[i]=evectorB[i][0]
##print('Собственный вектор компетентности VB',VB)
##
##summ=0
##for i in range(n):
##    summ=summ+VB[i]
##for i in range(n):
##    VB[i]=VB[i]/summ
##print('Собственный вектор компетентности нормированный VB',VB)
##
### Оценка лямбда 
##VN=B@VB
##for i in range(n):
##    VN1[i]=VN[i]/VB[i]
##summa=0
##for i in range(n):
##    summa=summa+VN1[i]
##ljmbda=  summa/n
##print("ljmbda=",ljmbda)
##
##print("Согласованность=",(ljmbda-m)/(m-1))
##
##
##    
##
##
##print("По Евланову")
##print("0.341, 0.298, 0.361 ")
##sr = np.zeros([m], "f")
##K = np.zeros([n], "f")
##for i in range(m):
##    for j in range(n):
##        sr[i]=sr[i]+E[i][j]/n
##print("sr=",sr)
##
##for j in range(n):
##    for i in range(m):
##        K[j]=K[j]+sr[i]+E[i][j]
##print("K=",K)
##summ=0
##for i in range(n):
##    summ=summ+K[i]
##for i in range(n):
##    K[i]=K[i]/summ
##print("Нормированный K=",K)
##
##print("Среднеквадратичное отклонение")
##
##for j in range(n):
##    for i in range(m):
##        K[j]=K[j]+(sr[i]-E[i][j])**2
##print("K=",K)
##summ=0
##for i in range(n):
##    summ=summ+K[i]
##for i in range(n):
##    K[i]=K[i]/summ
##print("Нормированный K=",K)
##
##print("Косинусная близость K=",K)
##
##ssr=(sr[0]**2+sr[1]**2)**0.5
##for j in range(n):
##    for i in range(m):
##        K[j]=K[j]+sr[i]*E[i][j]
##    K[j]=K[j]/(ssr*(E[0][j]**2+E[1][j]**2)**0.5)    
##print("K=",K)
##summ=0
##for i in range(n):
##    summ=summ+K[i]
##for i in range(n):
##    K[i]=K[i]/summ
##print("Нормированный  косинусная K=",K)
##
##
##
##        
##
##
##    
##
##
##    
##    
##    
##
##    
##
###*************************************
####A=numpy.multiply(E,ET)
####B=numpy.multiply(ET,E)
####for i in range(n):
####    for j in range(n):
####        s=0
####        for l in range(m):
####            s=s+ET[i][l]*E[l][j]
####        B[i][j]=s    
####print("BB",B)
##
##sum=0.9417+0.8252+1
##print('1=',0.9417/sum)
##print('2=',0.8252/sum)
##print('3=',1/sum)
##
