from BinaryTree import *
from random import randint

myHeapMax = Heap(Heap.HEAPMAX)
myHeapMin = Heap(Heap.HEAPMIN)

myList1 = [] 
myList2 = [13, 16, 16, 15, 11, 7, 11, 14, 11]
#erroneous output that is generated for a HEAPMIN: [7, 16, 11, 11, 11, 16, 13, 14, 15]
print "Generating random list..." 
for i in range(1,10):
    myList1.append(randint(1,20))
    #myList2.append(randint(1,20))

print "Heapifying..." 
#myHeapMax.heapify(myList1)
myHeapMin.heapify(myList2)

print "Testing HeapSort for HeapMax..."
var = myHeapMax.extractRoot()
while (myHeapMax.getSize()>0):
    aux = myHeapMax.extractRoot()
    if aux > var:
        print "Test Unsuccessful! Extracted %i first and %i next" % (var,aux)
        break
    else:
        var = aux

if myHeapMax.getSize() == 0:
    print "HeapSort test succeed!"

print "Testing HeapSort for HeapMin..."
var = myHeapMin.extractRoot()
while (myHeapMin.getSize()>0):
    aux = myHeapMin.extractRoot()
    if aux < var:
        print "Test Unsuccessful! Extracted %i first and %i next" % (var,aux)
        break
    else:
        var = aux
    
if myHeapMin.getSize() == 0:
    print "HeapSort test succeed!"