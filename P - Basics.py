# PREAMBLE
import nltk

# INTROSPECTION
dir(), dir2()
help()

# DATA TYPES AND CONVERSION
float(3)
int(3.0)
str(3)
type()
isinstance('foo',str)

# LISTS
l=[3, 4.1, "test"]
l.append("new")
l.sort()
l[::-1] # reverse
l_1 + l_2 # concatenate
# CHECK LIST
x in l # membership
len(l) # length
[x for x in l if x>3] # keep elts meet condition
[x for x in range(len(l)) if l[x]>3] # indices of elts meet condition

# SETS
y=set([2,2,3,3,3,4])
x|y  # set union
x&y  # set intersection
x^y  # set symm difference
x-y  # set diff

# DICTIONARIES
d = {"a": 1, "b": 2, "c": "c"}
d["a"]
d.keys()
d.values()
d={"key1":{"key1a":14, "key1b":15}, "key2":{"key2a":19, "key2b":21}}
d["key1"]["key1a"]

# TUPLES
tuple=(2, "foo", 3.7)
tuple.index("test")

# BOOLEAN
x==3 and y>2
x==3 or y>2
3 != 2
not (y > 2)
all([True, True, False, False])
any([True, True, False, False])

# STRINGS
str[:3]       # substring
"asd" in str  # check substring
len(str)      # 4
str.upper()   # ASDF
str.lower()
str.lstrip()  # remove leading spaces
str.rstrip()  # remove trailing spaces
str.startswith('foo') # true/false
"%s is %d" % ("Elliot",3)
"{x} hi {y} is {z}".format(x="a", y="b", z="c")

# REGEXP
import re
bool(re.search('[wW]','word'))      # True

# MATRICES
matrix=[list,list2]
matrix[0][1]
[i[0] for i in matrix]

# FUNCTIONS
def function_name(a,b=2):
    return(a+b, a*b)
sum, prod = function_name(3,2)
function2 = lambda a: a+5

# IF LOOP SYNTAX
if x == 3:
    code
elif x == 2:
    code
else:
    code

# FOR LOOP SYNTAX
for i in range(1,10):   # range(3) = range(0,3) = [0,1,2]
    code
for (x,y) in zip([1,2,3],[4,5,6]):
    code
for i, item in enumerate([5, 7, 9]):
    code

# WHILE LOOP SYNTAX
while index<=10:
    code
    if condition==TRUE:
        break

# LIST COMPREHENSIONS
[ f(x) for x in range(11) if x%2==0 ]       # map
[ n for n in vector if n%2==3 ]            # filter
[ n for n in vector if (all( n[i]==0 for i in range(5) )) ] # filter many conditions
[ x+2 for x in [x**2 for x in range(5)] ]  # nested
[ x+y for x,y in zip([1,2,3],[4,5,6]) ]  # 2 args paired
[ x+y for x in [1,2,3] for y in [4,5,6] ] # 2 args all combinations
[ x for x in list1 if x not in list2 ] # set minus









# REDUCE
from functools import reduce
reduce( (lambda x,y: x*y) , [1,2,3,4] )

# CLASSES
class Circle(object):
    pi = 3.14 # define global attributes
    def __init__(self,radius=1, shape="round"):
        # define attributes and default attribute
        # __init__ is just code that will run right when an
        # instance is created!
        self.radius=radius
    def area(self): # define methods
        return self.radius**2 * Circle.pi
c=Circle(radius=4) # create instance
c.radius # call attribute
c.area() # call method
c.__dict__ # see all attributes of an instance

# Try Except and Finally
try:
    2+"s"
except:
    print("There was a type error")
else:
    print("There was no error")
finally:
    print("This statement always prints")

#functions inside functions. when you want 1 function to do 2 different things depending on input
def outerfunction(input):
    def func1:
        code
    def func2:
        code
    if input==1:
        return func1
    if input==2:
        return func2



