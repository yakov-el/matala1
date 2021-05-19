# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:40:01 2021

@author: יעקב
"""

def Factorial(i:float):
    sum=i
    while(i>1):
        sum=sum*(i-1)
        i=i-1
    return(sum)
        

def Pow(x:float,i:float):
    if i==0:
        return(1)
    elif x==0:
        return(0)
    else:
        j=0
        sum=1
        while j<i:
            sum=sum*x
            j=j+1
        return (sum)
  

    

def exponent(x:float):
    i=1
    sum=0
    while(i<100):
        sum = sum + ((Pow(x,i) / Factorial(i)))
        i=i+1
    result = float('%0.6f' % sum)
    return(result + 1)
  
 
    
def Ln(x):
    i=0
    sum=0
    if x<=0:
        return(0.0)
    while i<100:
        sum= sum+ 2*((x-exponent(sum))/(x+exponent(sum)))   
        i=i+1
    result = float('%0.6f' % sum)
    return(result)
  

    
def XtimesY(x,y):
    if(x<=0):
        return(0.0)
    z1=Ln(x)
    z2=y*z1
    a = exponent(z2)
    result = float('%0.6f' % a)
    return(result)
  
    
def sqrt(y,x):
    try:
        return(XtimesY(x,1/y))
    except:
        return(0.0)
    
        
def calculate(x:(float))->float:
    if(x==0):
        return(0.0)
    ex=(exponent(x))*(exponent(x*Ln(7)))*(1/x)*(sqrt(x, x))
    result = float('%0.6f' % ex)
    return(result)