# -*- coding: utf-8 -*-
"""
Created on Wed May 24 06:29:47 2017

@author: Sridharan Kamalakannan
"""

import numpy as np

a=np.arange(15)
print(a)

a=a.reshape(3,5)
print(a)

print(a.shape)

print(a.size)

print(a.ndim)

print(a.dtype)

print(a.itemsize)

print(type(a))


a=np.array([2,3,4])
print(a)
print(a.dtype)

a=np.array([2.1,3.1,4.1])
print(a)
print(a.dtype)

a=np.array([1,2],dtype=complex)
print(a)


a=np.zeros((2,3))
print(a)
print(a.dtype)

a=np.zeros((2,3),dtype=int)
print(a)
print(a.dtype)


a=np.zeros((2,3),dtype=bool)
print(a)
print(a.dtype)


a=np.ones((2,3),dtype=bool)
print(a)
print(a.dtype)


a=np.empty((2,3),dtype=bool)
print(a)
print(a.dtype)


a=np.empty((2,3))
print(a)
print(a.dtype)

a=np.empty((2,3),dtype=int)
print(a)
print(a.dtype)

a=np.arange(10,30,4)
print(a)
print(a.dtype)

a=np.arange(.3,.5,.05)
print(a)
print(a.dtype)


a=np.linspace(1,10,100)
print(a)
print(a.dtype)

np.set_printoptions(threshold=np.nan)
print(a)












