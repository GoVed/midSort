# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:51:35 2021

@author: vedhs
"""
import random
import time

def midSort(arr,start=0,end=-1,steps=0):
    if end==-1:
        end=len(arr)
    
    minv=min(arr[start:end])
    maxv=max(arr[start:end])
    mid=int((minv+maxv)/2)
    temp=[0]*(end-start)
    a=0
    b=1
    i=start
    while i<end:
        val=arr[i]
        
        if val<=mid:
            temp[a]=val
            a+=1
        else:
            temp[-b]=val
            b+=1
        i+=1    
        steps+=1
        
    arr[start:end]=temp
    
    if a>0 and mid>minv+1:
        steps=midSort(arr,start,a+start,steps)
    if b>1 and mid<maxv-1:
        steps=midSort(arr,a+start,end,steps)
        
    return steps


#from geeks for geeks
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        #
        if arr[j] <= pivot:
  
            
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

  
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
  
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        
        
def benchmark():
    times=[]
    
    for i in range(20):
        times.append(2**(i+1))
    
    for n in times:
        a=[]
        for i in range(n):
            a.append(random.randint(0,1000))
        b=a[:]
        
        start = time.time()
        midSort(a)
        print('|',n,'|mid|',time.time()-start,'|')
        
        start = time.time()
        quickSort(b,0,n-1)
        print('|',n,'|quick|',time.time()-start,'|')
        
        
    
    
        

