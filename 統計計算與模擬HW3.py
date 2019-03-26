# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:57:19 2019

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd
#1
# MC method
MC=[]


#Let h(x)be 2*I(-20,20) , f(x) be Laplace(0,1)
for i in range(500000) :
    h_x=[]
    for j in range(1000) :
        u=np.random.laplace(0,1)
        if (-20<= u)& (u<= 20):
            h_x.append(2)
    I=sum(h_x)/1000
    MC.append(I)
    
Ans_MC=np.mean(MC)
Var_MC=np.var(MC)

#importance sampling : use N(0,1)as proposal distribution
N01=[]
#f(x)=1/2 * exp(-|x|)  laplace distribution
def f(x):
    if x>= 0:
        z=x
    else:
        z=-x
    y=(1/2)*np.exp(-z)
    return y
#g1(x):  N(0,1) distribution
def g1(x):
    y=np.sqrt(1/(2*np.pi))*np.exp(-(x**2)/2)
    return y

for i in range(5000) :
    h_x=[]
    for j in range(1000) :
        u=np.random.normal(0,1)
        if (-20<= u)& (u<= 20):
            h_x.append((2*f(u))/g1(u))
    I=sum(h_x)/1000
    N01.append(I)

Mean_N01=np.mean(N01)
Var_N01=np.var(N01)


#importance sampling : use N(0,5)as proposal distribution
N05=[]
#g2(x) : N(0,5) distribution

def g2(x):
    y=np.sqrt(1/(10*np.pi))*np.exp(-(x**2)/10)
    return y

for i in range(5000) :
    h_x=[]
    for j in range(1000) :
        u=np.random.normal(0,np.sqrt(5))
        if (-20<= u)& (u<= 20):
            h_x.append(2*f(u)*(1/g2(u)))
    I=sum(h_x)/1000
    N05.append(I)

Mean_N05=np.mean(N05)
Var_N05=np.var(N05)

#2 Compute P(X>3)，X~N(0,1)
MC_2=[]
for j in range(100000):
    h_x=[]
    for i in range(100) :
        u=np.random.normal(0,1)
        if u>3:
            h_x.append(1)
    I=sum(h_x)/100
    MC_2.append(I)
        
    
Mean_MC_2=np.mean(MC_2)
Var_MC_2=np.var(MC_2)

#g3(x) :  N(4,1) distribution
def g3(x):
    y=np.sqrt(1/(2*np.pi))*np.exp(-(((x-4)**2)/2))
    return y

N41=[]
for j in range(100000):
    h_x=[]
    for i in range(100) :
        u=np.random.normal(4,1)
        if u>3:
            h_x.append(g1(u)*(1/g3(u)))
    I=sum(h_x)/100
    N41.append(I)

Mean_N41=np.mean(N41)
Var_N41=np.var(N41)

# Compare confidence interval
CI_MC_2=(Mean_MC_2-(1.96*np.sqrt(Var_MC_2)),Mean_MC_2+(1.96*np.sqrt(Var_MC_2)))
CI_N41=(Mean_N41-(1.96*np.sqrt(Var_N41)),Mean_N41+(1.96**np.sqrt(Var_N41)))


