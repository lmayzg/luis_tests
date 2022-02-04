# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 11:54:55 2022

@author: Luis
"""

import numpy as np

a=np.array([0,0,2,2,3,4,4,8,8,9,9])
#Lista de posibles numeros
numb=np.zeros(10)
numb=numb.astype(int)
result=np.zeros(11)
twice=np.zeros(10)
op=-1
m=-1
s=0



#Quantity of each number
for i in range(11):
    for j in range(10):
        if a[i]==j:
            numb[j]+=1
            if numb[j]==2:
                twice[j]=1
 
#Validation           
if numb[0]==0 or numb[4]==0 or (numb[4]==1 and numb[6]==0) or (numb[1]==0 and numb[2]==0):
    print('No posible Venezuelan mobile phone number')
    quit()
    
#Venezuelan mobile phone number construction
numb[0]-=1
numb[4]-=1
result[1]=4
aux=numb

if numb[1]!=0:
    numb[1]-=1
    result[2]=1
    aux1=numb
    
    # 1st possible area code [0412]    
    if numb[2]!=0:
        numb[2]-=1
        result[3]=2
        
        for i in range(1,10):
            if numb[i]!=0:
                #Check if prime
                prime=True
                for j in range(2,i):
                    if (i % j)==0:
                        prime=False
                        break
                #Fix at the last position
                if prime and numb[i]!=3:
                    numb[i]-=1
                    result[10]=i
                    
                    #Divisible number at the 2nd last place
                    for j in range(1,10):
                        if numb[j]!=0 and (j % i)==0:
                            result[9]=j
                            numb[j]-=1
                            
                            #Filling in reverse order
                            for k in range(8,3,-1):
                                if result[k+1]==8 and numb[8]>0:
                                    result[k]=8
                                    numb[8]-=1
                                    if result[k+2]!=8:
                                        twice[result[k+2]]-=1
                                    
                                elif result[k+1]==8 and numb[8]==0:
                                    for l in range(10):
                                        if twice[l]!=0 and numb[l]!=0 and l>m:
                                            m=l
                                    result[k]=m
                                            
                                elif result[k+1]==9:
                                    for n in range(10):
                                        if numb[l]==1 and n>op:
                                            op=n
                                    result[k]=op
                            
                            
                            
                
            
        
    # 2nd possible area code [0414]
    numb=aux1
    if numb[4]!=0:
        numb[4]-=1
        result[3]=4
    # 3rd possible area code [0416]
    numb=aux1
    if numb[6]!=0:
        numb[6]-=1
        result[3]=6
        

numb=aux
if numb[2]!=0:
    numb[2]-=1
    result[2]=2
    aux1=numb
    
    # 4th possible area code [0424]
    numb=aux1
    if numb[4]!=0:
        numb[4]-=1
        result[3]=4
    
        for i in range(1,10):
            if numb[i]!=0:
                #Check if prime
                prime=True
                for j in range(2,i):
                    if (i % j)==0:
                        prime=False
                        break
                #Fix at the last position
                if prime and numb[i]!=3:
                    numb[i]-=1
                    result[10]=i
                    
                    #Divisible number at the 2nd last place
                    for j in range(1,10):
                        if numb[j]!=0 and (j % i)==0:
                            result[9]=j
                            numb[j]-=1
                            
                            #Filling in reverse order
                            for k in range(8,3,-1):
                                if result[k+1]==8 and numb[8]>0:
                                    result[k]=8
                                    numb[8]-=1
                                    if result[k+2]!=8:
                                        twice[int(result[k+2])]-=1
                                
                                elif result[k+1]==8 and numb[8]==0:
                                    for l in range(10):
                                        if twice[l]!=0 and numb[l]!=0 and l>m:
                                            m=l
                                            break
                                    result[k]=m
                                    numb[m]-=1
                                    
                                elif result[k+1]==9:
                                    for n in range(10):
                                        if numb[l]==1 and n>op:
                                            op=n
                                    result[k]=op
                                    
                                elif k==6:
                                    for p in range(10):
                                        if s==0:
                                            for q in range(2,p+1):
                                                if numb[p]!=0 and (p % q)==0:
                                                    d=q
                                                    s+=1
                                                    
                                        else:
                                            if numb[p]!=0 and (p % d)==0:
                                                s+=1
                                    
                                    if s>1:
                                        if numb[9]>=2:
                                            result[k]=9
                                            result[k-2]=9
                                            numb[9]-=2
                                            for p in range(10):
                                                if numb[p]!=0:
                                                    result[k-1]=p
                                                    print(result)
                                                    
                                                
                                        
    
    # 5th possible area code [0426]
    numb=aux1
    if numb[6]!=0:
        numb[6]-=1
        result[3]=6