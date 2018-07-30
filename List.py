from Node import node


class List:
    def __init__(self, name=None, data=None):
        self.data = data
        self.size = 0
        self.back = None
        self.front = None
        self.name = name

    def print_back(self):
        print(str(self.getBack()))

    def print_front(self):
        print(str(self.getFront()))

    def startFind(self, thing):
        ''' returns BSTnode if found, else returns None -- this is the helper function '''
        if self.isEmpty():
            return None
        else:
            return self.find(thing, self.front)

    def find(self, thing, node):
        ''' this is the recursive function '''
        while node.get_next() is not None:
            if node.get_data().getData() == thing:
                return node
            else:
                return self.find(thing, node.get_next())
        if node.get_data().getData() == thing:
            return node
        else:
            return False

    def remove(self, thing):
        '''Removes item from list'''
        if self.isEmpty() is True:
            return None
        else:
            N = self.startFind(thing)
            if self.size == 1:
                self.front = None
                self.back = None
                self.size -= 1
            elif N.get_next() is None:
                N.get_prev().set_next(None)
                self.setBack(N.getPrev())
                N.prev(None)
                self.size -= 1
            elif N.get_prev() is None:
                N.get_next().set_prev(None)
                self.setFront(N.get_next())
                N.next = None
                self.size -= 1
            else:
                N.get_next().set_prev(N.get_prev())
                N.get_prev().set_next(N.get_next())
                N.set_next(None)
                N.set_prev(None)
                self.size -= 1

    def setFront(self, front): self.front = front

    def getFront(self): return self.front

    def setBack(self, front): self.back = back

    def getBack(self): return self.back

    def setData(self, data): self.data = data

    def getData(self): return self.data

    # this will test if the list is empty
    def isEmpty(self): return self.size == 0

    def append(self, data):
        ''' puts data at the end of a list'''
        if self.isEmpty():
            self.front = node(data)
            self.back = self.front
            self.size += 1
        else:
            # create a node with data in it and call it 'temp'
            temp = node(data)
            temp.set_prev(self.front)
            # the new node's (temp) prev becomes the last element in the list
            # the back node's next becomes the newly created node
            self.back.set_next(temp)
            self.back = temp  # updating the back to temp
            self.size += 1

    def prepend(self, data):
        '''puts data at the end of a list'''
        if self.isEmpty():
            self.append(data)
        else:
            # create a node with data in it and call it 'temp'
            temp = node(data)
            temp.setNext(self.back)
            # the new node's (temp) next becomes the first element in the list
            # teh front node's prev becomes the newly created node
            self.front.setPrev(temp)
            self.front = temp  # updating the back to temp
            self.size += 1

    def insert(self, data, old_node):
        '''inserts a node between two other nodes in a list'''
        if self.isEmpty():
            self.append(data)
        else:
            if old_node == None:
                return None
            else:
                # create a node with data in it and call it 'temp
                temp = node(data)
                # set that node (temp) prev to the node already in the list
                temp.setPRev(old_node)
                temp.setNext(old_node.getNext())
                # set 'temp's next to the next of teh node already in the lsit
                old_node.setNext(temp)  # set 'temp' as the old node's next
                temp.getNext().setPrevious(temp)
                # set the original node after the old node to have 'temp as its new prev

    def delete(self, data, node):
        '''deletes a node frm a lsit, no matter its location'''
        if self.isEmpty():
            return None
        else:
            node.getPrev().setNext(node.getNext())
            node.getNext().setPrev(node.getPrev())
            self.size -= 1

    # def mergeSort(self, L1, L2):
    #     pointL1 = L1.getFront()
    #     pointL2 = L2.getFront()
    #     result = List()
    #     while (pointL1 != None) and (pointL2 != None):
    #         a = pointL1.getData()
    #         b = pointL2.getData()
    #         if
