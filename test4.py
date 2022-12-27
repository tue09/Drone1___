#Input: M customers, N trucks, P drones
import numpy as np
import kc
import queue
#Nhập số các phương tiện
M=int(input("Nhập số các customres: "))
N=int(input("Nhập số các trucks: "))
P=int(input("Nhập số các drones: "))
print("________________________________________")
#Nhập dung tích của Drone và khối lượng của các hàng
capi=float(input("Nhập dung tích của Drone: "))
wei=[0]*M
for i in range(0,M):
    wei[i]=float(input("Nhập khối lượng của gói hàng %i: "%(i+1)))
print("________________________________________")
#Nhập thời gian sẵn sàng của các Hàng
time=[0]*M
for i in range(0,M):
    time[i]=float(input("Nhập thời gian sẵn sàng của gói hàng %i: "%(i+1)))
#Nhập vận tốc của các phương tiện
Vdr=float(input("Nhập vận tốc của Drone: "))
Vtr=float(input("Nhập vận tốc của Truck: "))
print("________________________________________")
#Nhập tọa độ của các điểm
u,v=map(float,input("Nhập tọa độ của Depot: ").split())
dp=complex(u,v)
td_x=[None]*M
td_y=[None]*M
td=[None]*M
for i in range(0,M):
    td_x[i],td_y[i]=map(float,input("Nhập tọa độ của khách hàng thứ %i: "%(i+1)).split())
    td[i]=complex(td_x[i],td_y[i])
print("________________________________________")
#Nhập vào các giá trị của 2 mảng ban đầu
array1 = [0]*(M+N-1)
array2 = [0]*(M+N-1)
array3=[None]*(M+N-1)
print('Nhập các phần tử của mảng thứ nhất:')
for i in range(0,M+N-1):
    array1[i]=int(input("Nhập phần tử thứ %d: " %(i+1)))
print('Nhập các phần tử của mảng thứ hai:')
for i in range(0,M+N-1):
    array2[i]=float(input("Nhập phần tử thứ %d: " %(i+1)))
#Bước 1
#______________________________________________
    a=[0]*(N)
j=0
for i in range(M+N-1):
    if array1[i]==0:
        j+=1
        a[j]=i
a[0]=0
for j in range(0,M+N-1):
    if 0<=j<a[1]:
        array3[j]=int(array2[j]*(j+2))


for i in range(1,N-1):
    for j in range(0,M+N-1):
        if a[i]<j<a[i+1]:
            array3[j]=int(array2[j]*(j+1-a[i]))
        elif array1[j]==0:
            array3[j]=None

for j in range(0,M+N-1):
    if a[N-1]<j:
        array3[j]=int(array2[j]*(j+1-a[N-1]))
    elif array1[j]==0:
        array3[j]=None

array4=[None]*(M+N-1)

for i in range(0,a[1]):
    if array3[i]==0:
        array4[i]=0
    elif array3[i]>=1:
        array4[i]=array1[array3[i]-1]

for j in range(1,N-1):
    for i in range(a[j]+1,a[j+1]):
        if array3[i]>=1:
            array4[i]=array1[array3[i]+a[j]]
        elif array3[i]==0:
            array4[i]=0

for i in range(a[N-1]+1,M+N-1):
    if array3[i]==0:
        array4[i]=0
    elif array3[i]!=0:
        array4[i]=array1[array3[i]+a[N-1]]
arr=np.array((array1,array4))
#Bước 2
#______________________________________________
q1=queue.Queue(M)
q2=queue.Queue(P)
y=[0]*(M+N)
tr=[0]*N
for i in range(0,a[1]):
    if array4[i]==0:
        y[i]=time[array1[i]]
    tr[0]=max(y)+(kc.dis(dp,td[array1[0]]))/Vtr
y=[0]*(M+N)
for j in range(1,N-1):
    for i in range(a[j]+1,a[j+1]):
        if array4[i]==0:
            y[i]=time[array1[i]]
        tr[j]=max(y)+(kc.dis(dp,td[array1[a[j]+1]]))/Vtr
y=[0]*(M+N)
for i in range(a[N-1]+1,M+N-1):
    if array4[i]==0:
        y[i]=time[array1[i]]
    tr[N-1]=max(y)+(kc.dis(dp,td[array1[a[N-1]+1]]))/Vtr
y=[0]*(M+N)

ax=[]
ax.append(0)
array5=[]
for i in range(0,M+N-1):
    array5.append(array4[i])
if array5[0]!=0 and array1[0]!=0:
    ax.append(array1[0])
for k in range(0,N):
    for i in range(0,M+N-2):
        if array5[i]==0 and array5[i+1]!=0 and array1[i+1]!=0:
            ax.append(array1[i+1])
    ax.append(0)
    for item in array1:
        if item in ax:
            for j in range(0,M+N-1):
                if array1[j]==item:
                    array5[j]=0

qa=queue.Queue()
qu=[None]*(M+N+2)
que=[9]*(M+N+2)
for i in range(0,(M+N+2)):
    que[i]=[]
qugt=[0]*(M+N+2)
for i in range(0,M+N+2):
    qu[i]=queue.Queue()
for i in range(0,len(ax)):
    qa.put(ax[i])

qy=queue.Queue()
qz=queue.Queue()
j=0
p=[0]*(N+1)
for i in range(0,len(ax)):
    if ax[i]==0:
        p[j]=i
        j+=1
l=0
for i in range(0,(M+N+2)):
    if qugt[i]<=capi:
        while qugt[i]<=capi:
            if qa.empty():
                break
            w=qa.get()
            if w==0:
                break
            else:
                while not qa.empty():
                    qy.put(qa.get())
                qa.put(w)
                while not qy.empty():
                    qa.put(qy.get())
                z=qa.get()
                qugt[i]=qugt[i]+wei[z-1]
                qu[i].put(z)
    if qa.empty():
        break
    if qugt[i]>capi:
        while qu[i].qsize()!=1:
            qy.put(qu[i].get())
        while not qa.empty():
            qz.put(qa.get())
        qa.put(qu[i].get())
        while not qz.empty():
            qa.put(qz.get())
        while not qy.empty():
            qu[i].put(qy.get())

for i in range(0,len(que)):
    while not qu[i].empty():
        que[i].append(qu[i].get())
for j in range(0,(M+N+2)):
    for i in range(0,len(que)):
        if len(que[i])==0:
            que.pop(i)
            break
#Bước 3
#______________________________________________
t=[0]*(M+1)
for i in range(1,M+1):
    for j in range(0,M+N-1):
        if array1[j]==i:
            t[i]=j
t.pop(0)
n=[0]*(M+1)
for i in range(0,M+N-1):
    if a[0]<i<a[1]:
        n[array1[i]]=0
    for j in range(1,N-1):
        if a[j]<i<a[j+1]:
            n[array1[i]]=j
    if i>a[N-1]:
        n[array1[i]]=N-1
m=[0]*(M+1)
for i in range(0,M+N-1):
    if array1[i]!=0:
        m[array1[i]]=array4[i]
queu=[0]*N
for i in range(0,N):
    queu[i]=[]
at=[]
for i in range(0,len(ax)):
    if ax[i]==0:
        at.append(i)
for i in range(0,len(que)):
    for j in range(0,N):
        for k in range(0,len(ax)):
            if ax[k]==que[i][0]:
                if at[j]<k<at[j+1]:
                    queu[j].append(que[i])
tp=[0]*(M+1)
for i in range(0,len(que)):
    tp[m[que[i][0]]]=(kc.dis(dp,m[que[i][0]]))/Vdr
    for j in range(1,len(que[i])):
        tp[m[que[i][j]]]=tp[m[que[i][j-1]]]+(kc.dis(m[que[i][j]],m[que[i][j-1]]))/Vdr
dr=[0]*P
time1=[0]*len(queu)
for i in range(0,len(queu)):
    time1[i]=[0]*len(queu[i])
    for j in range(0,len(queu[i])):
        time1[i][j]=[0]*len(queu[i][j])
        for k in range(0,len(queu[i][j])):
            time1[i][j][k]=time[m[queu[i][j][k]]]
tr1=[0]*len(queu)
for i in range(0,len(queu)):
    tr1[i]=[0]*len(queu[i])
    for j in range(0,len(queu[i])):
        tr1[i][j]=[0]*len(queu[i][j])
        for k in range(0,len(queu[i][j])):
            tr1[i][j][k]=n[m[queu[i][j][k]]]

while len(queu)!=0:
    while len(queu[0])!=0:
        for i in range(0,len(queu[0])):
            for j in range(0,P):
                if dr[j]==min(dr):
                    for k in range(0,len(queu[0][0])):
                        if t[m[queu[0][0][k]]]==M+N-2:
                            r=max(time1[0][0])
                            q=max(tr1[0][0])
                            tr[n[m[queu[0][0][k]]]]=max(r,q,dr[j],tr[n[m[queu[0][0][k]]]])+tp[m[queu[0][0][k]]]+(kc.dis(td[m[queu[0][0][k]]],dp))/Vtr
                        elif  (array1[t[m[queu[0][0][k]]]+1]==0):
                            r=max(time1[0][0])
                            q=max(tr1[0][0])
                            tr[n[m[queu[0][0][k]]]]=max(r,q,dr[j],tr[n[m[queu[0][0][k]]]])+tp[m[queu[0][0][k]]]+(kc.dis(td[m[queu[0][0][k]]],dp))/Vtr
                        else:
                            r=max(time1[0][0])
                            q=max(tr1[0][0])
                            tr[n[m[queu[0][0][k]]]]=max(r,q,dr[j],tr[n[m[queu[0][0][k]]]])+tp[m[queu[0][0][k]]]+(kc.dis(td[m[queu[0][0][k]]],td[array1[t[m[queu[0][0][k]]]+1]]))/Vtr
                r=max(time1[0][i])
                q=max(tr1[0][i])
                dr[j]=max(r,q,dr[j])+tp[m[queu[0][i][len(queu[0][i])-1]]]+(kc.dis(td[m[queu[0][i][len(queu[0][i])-1]]],dp))/Vdr
        queu[0].pop(0)
    queu.pop(0)
X=max(tr)
print(X)
