a = 7
b = 9
c = a + b
print(a, b, c)##7 9 16
z1 = 3 + 2j
z1##(3+2j)
z1.real##3.0
z1.imag##2.0
#everything is an object; lots of built-in methods
dir(3.7)
3.7.__trunc__()##3
exp(a)#need math
from math import exp
exp(a)##1096.6331584284585
a/2.0##3.5
a//2.0##3.0
a%2##1
aStr = 'This is a string'
bStr = "This is also a string\n"
aStr*3##'This is a stringThis is a stringThis is a string'
foo = True
bar = False
foo and bar##False
foo and not bar##True
aBool = not None
type(aBool)##bool
#LISTS AND OTHER ITERABLES
aList = [1, 'zebra', 3]
aList[1]; aList[-1]; aList[-2]##'zebra'
bList = aList
bList == aList##True
aList.append('hippopotamus')
print(aList)##[1, 'zebra', 3, 'hippopotamus']
print(bList)##[1, 'zebra', 3, 'hippopotamus']
aList[1:3]##['zebra', 3]
aList[1:]##['zebra', 3, 'hippopotamus']
aList[:2]##[1, 'zebra']
aList##[1, 'zebra', 3, 'hippopotamus']
stoogesList = ['Moe', 'Larry', 'Curly']
marxBrosList = ['Chico', 'Groucho', 'Harpo']
stoogesList and marxBrosList ##['Chico', 'Groucho', 'Harpo']
#manual:  The expression x and y first evaluates x; 
#if x is false, its value is returned; otherwise, y is evaluated 
# and the resulting value is returned.
bork = None and stoogesList; krob = False and stoogesList
bork##
krob##False
aNestedList = []
aNestedList = [[4], 5, aList]
len(aNestedList)##3
len(aNestedList[0])##1
aNestedList.append([4, 5])
aNestedList##[[4], 5, [1, 'zebra', 3, 'hippopotamus'], [4, 5]]
foo = [1, 2]; bar = [3, 4]
foo + bar##[1, 2, 3, 4]
foo.extend(bar)
foo##[1, 2, 3, 4]
aList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bList = aList
aList = aList[-3:] + aList[:-3]
aList##[7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
bList##[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
aList.sort()
aList##[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bList.sort(reverse=True)
bList##[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
shortList = [0, 1, 2, 3]
def alphaKey(n):
    numList = ['zero', 'one', 'two', 'three']
	return numList[n]
shortList.sort(key=alphaKey)
shortList##[1, 3, 2, 0]
3 in shortList##True
shortList.insert(2,'hippopotamus')##[1, 3, 'hippopotamus', 2, 0]
shortList.remove('hippopotamus')##[1, 3, 2, 0] # removes FIRST instance only; ValueError if not found
del(aList[2]) # removes 3rd item in list, whatever it is
aList##[0, 1, 3, 4, 5, 6, 7, 8, 9]
bList##[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
min(shortList)##0
max(shortList)##3
sum(shortList)##6
shortList = shortList*2
shortList##[1, 3, 2, 0, 1, 3, 2, 0]
shortList.count(2)##2 #returns 0 if item not in list
shortList.index(2)##2 #returns ValueError if item not in list
'''
Quick Check, pg. 60
'''
# see https://docs.python.org/3.7/tutorial/datastructures.html
import copy
from copy import deepcopy
bList = copy.deepcopy(aList)
aList.insert(2, 2)
aList##[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bList##[0, 1, 3, 4, 5, 6, 7, 8, 9]
bList = sorted(aList) # sorted list is deepcopy
aList##[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bList##[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bList = aList[:] # this is also deep copy
'''
What happens if you do
matrix = [[1, 2, 3], [4, 5, 6]]
anotherMatrix = matrix
anotherMatrix.append(deepcopy(matrix[0]))
'''
stack = [3, 4, 5]
stack.append(6)
stack##[3, 4, 5, 6]
stack.pop() # pops from end; stack.pop([i]) for middle.pop() method takes a single argument (index) and removes the item present at that index.
stack##[3, 4, 5]
from collections import deque
queue = deque(['Groucho', 'Chico', 'Harpo'])
queue.append('Zeppo')
firstBro = queue.popleft()
nextBro = queue.popleft()
queue##deque(['Harpo', 'Zeppo'])
#####   TUPLES ######
aTuple = (1, 2, 3) # similar to list
aTuple[2]
aTuple[1] = 7 # causes error 
aTuple[1:3]##(2, 3)
tupleList = list(aTuple)
tupleList[1] = 7
aTuple##(1, 2, 3)
tupleList##[1, 7, 3]
# How to sort a tuple?
oneElementTuple = (3)
type(oneElementTuple)##int
oneElementTuple = (3, )
oneElementList = [3, ]
a, b, c = aTuple
a##1
b##2
c##3
anotherTuple = 4, 5, 6
anotherTuple##(4, 5, 6)
1 in aTuple##True
max(aTuple)##3
####  SETS #####
#Elements must be immutable! 
emptySet = set() # NOT {}, as that would create a dictionary!
emptySet##set()
stoogesList.append('Curly')
stoogesList##['Moe', 'Larry', 'Curly', 'Curly']
setOfStooges = set(stoogesList)
setOfStooges##{'Curly', 'Larry', 'Moe'}
'Curly' in setOfStooges##True
setOfMarxBros = set(marxBrosList)
setOfStooges and setOfMarxBros ##{'Chico', 'Groucho', 'Harpo'}
setOfStooges & setOfMarxBros##set()
setOfStooges | setOfMarxBros##{'Chico', 'Curly', 'Groucho', 'Harpo', 'Larry', 'Moe'}
setOfMarxBros or setOfStooges##{'Chico', 'Groucho', 'Harpo'}
setOfMarxBros.add('Ed')
setOfStooges.add('Ed')
setOfMarxBros & setOfStooges##{'Ed'}
setOfMarxBros - setOfStooges##'Chico', 'Groucho', 'Harpo'}
setOfMarxBros ^ setOfStooges##{'Chico', 'Curly', 'Groucho', 'Harpo', 'Larry', 'Moe'}
setOfMarxBros[1]#'set' object does not support indexing
aSet = set(aTuple)
aSet##{1, 2, 3}
bigBadSet = setOfStooges.add(aSet)# unhashable type: 'set'
aset = frozenset(aSet)
aset##frozenset({1, 2, 3})
bigBadSet = setOfStooges.add(aSet)





