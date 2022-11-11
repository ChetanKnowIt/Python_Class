Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
a = np.arange(0,11)
print(a)
[ 0  1  2  3  4  5  6  7  8  9 10]
b = np.arange(0,11).reshape(3,3)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b = np.arange(0,11).reshape(3,3)
ValueError: cannot reshape array of size 11 into shape (3,3)
b = a.reshape(3,3)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b = a.reshape(3,3)
ValueError: cannot reshape array of size 11 into shape (3,3)
b = np.random.randint(0,10).reshape(3,3)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b = np.random.randint(0,10).reshape(3,3)
AttributeError: 'int' object has no attribute 'reshape'
b = np.random.randint(0,10,(2,2))
print(b)
[[6 3]
 [0 9]]
c = np.random.randint(0,10,(3,3))
print(c)
[[2 1 4]
 [9 5 2]
 [7 0 2]]
c = np.random.randint(0,28,(3,3,3))
print(c)
[[[ 5 18 17]
  [ 0  7  1]
  [26 13  5]]

 [[12 10  5]
  [13 17  7]
  [ 7 24  3]]

 [[ 9  3 25]
  [12 17 10]
  [ 3 16 17]]]
print(a.ndim, a.size, a.shape, a.dtype, a.itemsize)
1 11 (11,) int32 4
print(b.ndim, b.size, b.shape, b.dtype, b.itemsize)
2 4 (2, 2) int32 4
print(c.ndim, c.size, c.shape, c.dtype, c.itemsize)
3 27 (3, 3, 3) int32 4
c = np.random.randint(0,46,(5,3,3))
print(c)
[[[37  5 33]
  [ 1 12  7]
  [44 40 30]]

 [[19 31 12]
  [42 31 45]
  [32 10  4]]

 [[23 22 45]
  [10  7 17]
  [38  0 15]]

 [[35 13 45]
  [ 0 19 13]
  [11 18 35]]

 [[19 38 32]
  [18 42 42]
  [28 28 10]]]
# creating 3*5 array using empty and full numpy, filled all zeros, filled all ones
a2 = np.empty(15)
print(a2)
[6.23042070e-307 3.56043053e-307 1.37961641e-306 8.90071135e-308
 8.01097889e-307 1.78020169e-306 7.56601165e-307 1.02359984e-306
 1.33510679e-306 2.22522597e-306 1.33511018e-306 6.23057689e-307
 1.33511562e-306 6.89805151e-307 2.56765117e-312]
a2 = np.empty([3,5], dtype = int)
print(a2)
[[      0       0       0       0       0]
 [      0       0       0       0       0]
 [    696       0       0 7077989       0]]
a2.shape
(3, 5)
a2.size
15
a2 = np.full([3,5], 3, dtype = int)
print(a2)
[[3 3 3 3 3]
 [3 3 3 3 3]
 [3 3 3 3 3]]
a2 = np.ones([3,5])
print(a2)
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
a2 = np.ones(3,5)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a2 = np.ones(3,5)
  File "C:\Python310\lib\site-packages\numpy\core\numeric.py", line 204, in ones
    a = empty(shape, dtype, order)
TypeError: Cannot interpret '5' as a data type
a2 = np.ones((3,5))
print(a2)
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
a2 = np.zeros((3,5))
print(a2)
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
# create numpy array with values ranging from 14 to 40
a3 = np.random.randint(14,40)
print(a3)
30
a3 = np.random.randint(14,40,1)
print(a3)
[26]
a3 = np.random.randint(14,40,(26,1))
print(a3)
[[35]
 [25]
 [20]
 [24]
 [39]
 [27]
 [33]
 [24]
 [15]
 [20]
 [25]
 [34]
 [37]
 [19]
 [16]
 [29]
 [26]
 [31]
 [37]
 [14]
 [19]
 [29]
 [30]
 [33]
 [35]
 [34]]
a3 = np.random.randint(14,40,(5,5))
print(a3)
[[28 26 21 22 35]
 [27 17 23 25 17]
 [14 25 33 23 24]
 [27 32 37 26 25]
 [39 14 39 22 37]]
a3 = np.random.randint(14,40,(5,2,2))
print(a3)
[[[38 39]
  [21 34]]

 [[16 14]
  [14 28]]

 [[15 36]
  [22 23]]

 [[18 16]
  [18 21]]

 [[25 36]
  [33 19]]]
a3 = np.random.randint(0,41,(8,5))
print(a3)
[[28 23 31 33 25]
 [ 0  6 38  6  2]
 [20 35 26 24  2]
 [26 26 19  3 37]
 [ 3 30 11  5 34]
 [21 37 30 22 13]
 [27  0 27 35 33]
 [ 6 22 30 32  1]]
a3 = np.random.randint((8,5))
print(a3)
[6 3]
a3 = np.random.randint(8,5)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a3 = np.random.randint(8,5)
  File "mtrand.pyx", line 746, in numpy.random.mtrand.RandomState.randint
  File "_bounded_integers.pyx", line 1338, in numpy.random._bounded_integers._rand_int32
ValueError: low >= high
a3 = np.random.random(8,5)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a3 = np.random.random(8,5)
  File "mtrand.pyx", line 427, in numpy.random.mtrand.RandomState.random
TypeError: random() takes at most 1 positional argument (2 given)
a3 = np.random.randint(0,41,(8,5)).reshape(4,10)
print(a3)
[[36 24 24 28 18  3 20 38 28 17]
 [21 37 12 11 36 40 10  6 11 21]
 [28 12 36  3  5  2 25  9 40 26]
 [ 1 13 28 14 30  4 30 33 15 37]]
a[2,3]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a[2,3]
IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed
a3[2,3]
3
a3[2:,3:]
array([[ 3,  5,  2, 25,  9, 40, 26],
       [14, 30,  4, 30, 33, 15, 37]])
a3[:,3:]
array([[28, 18,  3, 20, 38, 28, 17],
       [11, 36, 40, 10,  6, 11, 21],
       [ 3,  5,  2, 25,  9, 40, 26],
       [14, 30,  4, 30, 33, 15, 37]])
a3[:3,3:]
array([[28, 18,  3, 20, 38, 28, 17],
       [11, 36, 40, 10,  6, 11, 21],
       [ 3,  5,  2, 25,  9, 40, 26]])
a3[:3,3:]
array([[28, 18,  3, 20, 38, 28, 17],
       [11, 36, 40, 10,  6, 11, 21],
       [ 3,  5,  2, 25,  9, 40, 26]])
a3
array([[36, 24, 24, 28, 18,  3, 20, 38, 28, 17],
       [21, 37, 12, 11, 36, 40, 10,  6, 11, 21],
       [28, 12, 36,  3,  5,  2, 25,  9, 40, 26],
       [ 1, 13, 28, 14, 30,  4, 30, 33, 15, 37]])
a3[:3,:3]
array([[36, 24, 24],
       [21, 37, 12],
       [28, 12, 36]])
a3[:3,:4]
array([[36, 24, 24, 28],
       [21, 37, 12, 11],
       [28, 12, 36,  3]])
a3[:3]
array([[36, 24, 24, 28, 18,  3, 20, 38, 28, 17],
       [21, 37, 12, 11, 36, 40, 10,  6, 11, 21],
       [28, 12, 36,  3,  5,  2, 25,  9, 40, 26]])
a3[:3,5]
array([ 3, 40,  2])
a3[:,3:]
array([[28, 18,  3, 20, 38, 28, 17],
       [11, 36, 40, 10,  6, 11, 21],
       [ 3,  5,  2, 25,  9, 40, 26],
       [14, 30,  4, 30, 33, 15, 37]])
a3
array([[36, 24, 24, 28, 18,  3, 20, 38, 28, 17],
       [21, 37, 12, 11, 36, 40, 10,  6, 11, 21],
       [28, 12, 36,  3,  5,  2, 25,  9, 40, 26],
       [ 1, 13, 28, 14, 30,  4, 30, 33, 15, 37]])
a3[:,2:]
array([[24, 28, 18,  3, 20, 38, 28, 17],
       [12, 11, 36, 40, 10,  6, 11, 21],
       [36,  3,  5,  2, 25,  9, 40, 26],
       [28, 14, 30,  4, 30, 33, 15, 37]])
a3[:,2:6]
array([[24, 28, 18,  3],
       [12, 11, 36, 40],
       [36,  3,  5,  2],
       [28, 14, 30,  4]])
a3[:,2:5]
array([[24, 28, 18],
       [12, 11, 36],
       [36,  3,  5],
       [28, 14, 30]])
print(a3)
[[36 24 24 28 18  3 20 38 28 17]
 [21 37 12 11 36 40 10  6 11 21]
 [28 12 36  3  5  2 25  9 40 26]
 [ 1 13 28 14 30  4 30 33 15 37]]
a3[a3%2==1]
array([ 3, 17, 21, 37, 11, 11, 21,  3,  5, 25,  9,  1, 13, 33, 15, 37])
print(a3)
[[36 24 24 28 18  3 20 38 28 17]
 [21 37 12 11 36 40 10  6 11 21]
 [28 12 36  3  5  2 25  9 40 26]
 [ 1 13 28 14 30  4 30 33 15 37]]
a3[a3%2==0]=-1
print(a3)
[[-1 -1 -1 -1 -1  3 -1 -1 -1 17]
 [21 37 -1 11 -1 -1 -1 -1 11 21]
 [-1 -1 -1  3  5 -1 25  9 -1 -1]
 [ 1 13 -1 -1 -1 -1 -1 33 15 37]]
b1=np.arange(0,7)
b2=np.arange(11,19)
print(b1,b2)
[0 1 2 3 4 5 6] [11 12 13 14 15 16 17 18]
b3=np.append(b1,b2)
print(b3)
[ 0  1  2  3  4  5  6 11 12 13 14 15 16 17 18]
b4=sort(b3)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    b4=sort(b3)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
