import numpy as np
np.set_printoptions(linewidth=320, precision=2)
import matplotlib.pyplot as plt

# Creation
np.array([[1,2],[3,4]])
np.linspace(1,10,5) #5 evenly spaced values between 1 and 10
np.asarray(x)
np.ones((3,2))
np.zeros((3,2))
np.eye(3)

# Slicing
a[0,1]
a[:,:2]
b=a.copy()
a[a>2] #vs  #returns a filtered
a>2      #returns array of booleans

# Check properties
type(a)
a.dtype #int or float
a.shape #dims

# Manipulation
hstack(a,b) #concatenation
vstack(a,b) #concatenation
a.transpose()
a.reshape((2,3))

for (x,y) in a: #for loops iterate over 1st axis as a list
    print(x*y)

# Logical (checks elementwise, returns array of booleans)
a>b
np.logical_and(a>0, a<3)
np.logical_not(a==b)
np.logical_or(a>0, a<3)
np.where(a>2, b, c) #wherever a>2, choose corresp item in b, wherever false, choose in c

# Linear Algebra
np.linalg.det(a)
vals, vecs = np.linalg.eig(a)
np.linalg.inv(a)
a*b #element wise
a@b #matrix mult
np.dot(a,b) #dot product

# Random numbers
np.random.seed(12345)
np.random.randint(5,10, size=(3,2)) #random int between [5,10)
np.random.normal(1.5, 4.0) #random gaussian mean stdev
np.random.rand(3,2)

#Statistics
a.mean()
a.var()
a.std()
a.min()
a.max()
a.argmin()
a.argmax()

#Calculus
np.poly([-1,1,1,10]) #roots to coeffs
np.roots([1,4,-2,3]) #coeffs to roots
np.polyint([1,1,1,1]) #symbolic integration of coeffs
np.polyder([1./4., 1./3., 1./2., 1., 0.]) #symbolic deriv of coeffs
np.polyfit(x,y,2) #ordered pairs to coeffs of best fit order 2 poly