from math import log

class BinaryTree(object):
    
    _treeKeys = []

    def __init__(self):
        self._treeKeys = []
        
    def _getParentPos(self,pos):
        if pos < 0:
            return None
        elif pos == 0:
            return 0
        else:
            return int((pos-1)/2)
        
    def _getLeftChildPos(self,pos):
        return 2*pos+1
        
    def _getRightChildPos(self,pos):
        return 2*pos+2
    
    def _swapKeys(self,pos1,pos2):
        aux = self._treeKeys[pos1]
        self._treeKeys[pos1] = self._treeKeys[pos2]
        self._treeKeys[pos2] = aux


class Heap(BinaryTree):
    
    (HEAPMIN,HEAPMAX) = (1,2)
    _heapType = None
    
    def __init__(self,heapType=HEAPMIN):
        super(Heap,self).__init__()
        self._heapType = heapType
        
    def getSize(self):
        return len(self._treeKeys)
    
    def getHeight(self):
        return int(log(self.getSize(),2))
    
    def readRoot(self):
        if len(self._treeKeys) > 0:
            return self._treeKeys[0] 
        else:
            return None
        
    def insert(self,key):
        self._treeKeys.append(key)
        self.__bubbleUp(len(self._treeKeys)-1)
        
    def extractRoot(self):
        key = self.readRoot()
        self._treeKeys[0] = self._treeKeys.pop()
        self.__bubbleDown(0)
        return key
    
    def heapify(self,arrayList):
        self._treeKeys = arrayList
        print "Starting binary tree:"
        print self._treeKeys
        for i in range(int(self.getSize()/2)-1,-1,-1):
        #for i in range(0,int(self.getSize()/2)):
            print "Bubbling down node %i, being A[%i] = %i" % (i,i,self._treeKeys[i])
            self.__bubbleDown(i)
            print "Result of this bubbledown: "
            print self._treeKeys
    
    def __bubbleUp(self,pos):
        parentPos = self._getParentPos(pos)
        if self._heapType == self.HEAPMIN:
            if self._treeKeys[pos] < self._treeKeys[parentPos]:
                self._swapKeys(pos, parentPos)
                self.__bubbleUp(parentPos)
        else:
            if self._treeKeys[pos] > self._treeKeys[parentPos]:
                self._swapKeys(pos, parentPos)
                self.__bubbleUp(parentPos)
                
    def __bubbleDown(self,pos):
        f = lambda x: None if x > self.getSize()-1 else self._treeKeys[x]
        noChildren = lambda x,y: True if x>self.getSize()-1 and y>self.getSize()-1 else False
        lcPos = self._getLeftChildPos(pos)
        rcPos = self._getRightChildPos(pos)        
        lcKey = f(lcPos)
        rcKey = f(rcPos)
        pKey = self._treeKeys[pos]
        if self._heapType == self.HEAPMIN:
            if not noChildren(lcPos,rcPos):
                if (rcPos > self.getSize()-1 and lcKey < pKey) or (lcKey < rcKey and lcKey < pKey):
                    self._swapKeys(pos, lcPos)
                    self.__bubbleDown(lcPos)
                elif (rcKey < lcKey) and (rcKey < pKey):
                    self._swapKeys(pos, rcPos)
                    self.__bubbleDown(rcPos)
        else:
            if not noChildren(lcPos,rcPos):
                if (rcPos > self.getSize()-1 and lcKey > pKey) or (lcKey > rcKey and lcKey > pKey):
                    self._swapKeys(pos, lcPos)
                    self.__bubbleDown(lcPos)
                elif (rcKey > lcKey) and (rcKey > pKey):
                    self._swapKeys(pos, rcPos)
                    self.__bubbleDown(rcPos)
            
class BinarySearchTree(BinaryTree):
    
    def __init__(self):
        super(BinaryTree,self).__init__()
        
class RedBlackTree(BinaryTree):
    
    def __init__(self):
        super(BinaryTree,self).__init__()