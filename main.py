import numpy as np
import matplotlib.pyplot as plt
x_=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
y_=[3.37, 3.95, 3.73, 3.59, 3.15, 3.15, 3.05, 3.86, 3.60, 3.70, 3.02]

def qubic_spline_coeff(x_nodes,y_nodes)
    n=len(x_nodes)
    matrix=np.zeros((n,n))
    h=np.zeros((n-1))
    matrix[0][0] = 1
    matrix[n - 1][n - 1] = 1
    res=np.zeros((n,1))
    for k in range(n-1)
        h[k]=x_nodes[k+1]-x_nodes[k]
    for k in range(n-2)
        matrix[k+1][k]=h[k]
        matrix[k+1][k+1]=2(h[k+1]+h[k])
        matrix[k+1][k+2]=h[k+1]
        #print(k)
        #print(matrix)
        res[k+1][0]=3((y_nodes[k+2]-y_nodes[k+1])h[k+1]-(y_nodes[k+1]-y_nodes[k])h[k])
        # 3h2(a3-a2)- 3h1(a2-a1) = 3((a3-a2)h2 - (a2-a1)h1) == 3( (a[n+2]-a[n+1])h[n+1] - (a[n+1]-a[n])h[n])
        # print(res[k+1])
    c=np.linalg.inv(matrix).dot(res)
    result=np.zeros((n-1,4))
    for i in range(n-1)
        result[i][0] = y_nodes[i]
        result[i][1] = (y_nodes[i+1]-y_nodes[i])h[i]-h[i](c[i+1]+2c[i])3
        result[i][2] = c[i]
        result[i][3] = (c[i+1]-c[i])(h[i]3)
    return result


#Функция, которая возвращает значение кубического сплайна в точке x (qs_coeff обозначает матрицу коэффициентов)
def qubic_spline(x, qs_coeff)
    j=0                         
    i=0
    while x=i
       i+=0.1
       j+=1                      
    j-=1                       
    if j = 10
        return 3.02
    a=qs_coeff[j]
    return a[0]+a[1](x-j0.1)+a[2](x-j0.1)2+a[3](x-j0.1)3
    #a[i]+b[i](x-x[i])+c[i](x-x[i])2+d[i](x-x[i])3

#Функция, которая возвращает значение производной кубического сплайна в точке x (qs_coeff обозначает матрицу коэффициентов)
def d_qubic_spline(x, qs_coeff)
    j = 0 
    i = 0.0
    while x = i
        i += 0.1
        j += 1                  
    j -= 1                     
    if j=10
       return 3.02
    a = qs_coeff[j]
    return a[1] + a[2]  (x - j  0.1)  2 + 3  a[3]   (x - j  0.1)2

if __name__=='__main__'
    qs_coeff=qubic_spline_coeff(x_,y_)
    x_massiv=np.linspace(0,1,500) 
    spisok=[]
    for x in x_massiv
        spisok.append(qubic_spline(x,qs_coeff)) 
    plt.xlabel('Значения x[0-1]')
    plt.ylabel('Значения y')
    plt.plot(x_massiv,spisok)
    plt.plot(x_,y_,'ro')
    plt.grid()
    plt.show()
