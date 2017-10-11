# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:55:23 2017

@author: GooYoung
"""

#######################################################
################ chapter 03 신경망 ####################
#######################################################

import numpy as np

##### 3.2 활성화 함수

### 3.2.2 계단함수 구현하기 

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

step_function(1)
step_function(-3)
step_function(1.0)
step_function(np.array([1.0, 2.0]))
step_function([1.0, 2.0])
 
x = np.array([-1.0, 1.0, 2.0])
x
y = x > 0
y
y = y.astype(np.int)
y

### 3.2.3 계단함수 그래프

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)

### 3.2.4 시그모이드 함수 구현하기

def sigmoid(x):
    return 1 / (1+np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
sigmoid(x)

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)

### 3.2.7 ReLU 함수

def relu(x):
    return np.maximum(0, x)

relu(5)
relu(-3)

##### 3.3 다차원 배열 계산

import numpy as np
A = np.array([1, 2, 3, 4])
print(A)
np.ndim(A)
A.shape
A.shape[0]
A.shape[1]
type(A.shape)

B = np.array([[1,2], [3,4], [5,6]])
print(B)
np.ndim(B)
B.shape

C = np.array([[[1,2], [3,4], [5,6]],[[10,20], [30,40], [50,60]]])
print(C)
np.ndim(C)
C.shape

D = np.array([[[[1,2], [3,4], [5,6]],[[10,20], [30,40], [50,60]]], [[[2,1], [4,3], [6,5]],[[100,200], [300,400], [500,600]]]])
print(D)
np.ndim(D)
D.shape

X = np.array([1,2])
W = np.array([[1,3,5],[2,4,6]])
X.shape
W.shape
print(X)
print(W)
Y = np.dot(X, W)
print(Y)

##### 3.4 3층 신경망 구현하기

### 3.4.2 신호 전달 구현

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(X)
print(W1)
print(B1)

print(X.shape)
print(W1.shape)
print(B1.shape)

A1 = np.dot(X, W1) + B1
print(A1)

def sigmoid(x):
    return 1 / (1+np.exp(-x))

Z1 = sigmoid(A1)

print(A1)
print(Z1)

W2 = np.array([[0.1, 0.4],[0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(W2)
print(B2)

print(W2.shape)
print(B2.shape)
print(Z1.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

def identity_function(x):
    return x

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)
print(Y)

### 3.4.3 구현정리

def identity_function(x):
    return x

def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    
    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot (x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot (z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot (z2, W3) + b3
    y = identity_function(a3)
    
    return y

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)

##### 3.5 출력층 설계하기

a = np.array([0.3, 2.9, 4.0])

exp_a = np.exp(a)
print(exp_a)

sum_exp_a = np.sum(exp_a)
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)

def softmax(x):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y

### 소프트맥스 함수 구현 시 주의점 : overflow

a = np.array([1010, 1000, 990])
np.exp(a) / np.sum(np.exp(a))
c = np.max(a)
a-c
np.exp(a-c) / np.sum(np.exp(a-c))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
np.sum(y)


#######################################################
###################### finish #########################
#######################################################