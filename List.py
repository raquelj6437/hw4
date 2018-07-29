from Node import node


class List:
    def __init__(self, name=None, data=None):
        self.data = data
        self.size = 0
        self.back = None
        self.front = None
        self.name = name
        self.root = ''  # creates an empty node ab initio
        self.allNodes = []  # a temporary fudge to hold all the tree's nodes

    def print_back(self):
        print(str(self.getBack()))

    def print_front(self):
        print(str(self.getFront()))

    def startFind(self, thing):
        ''' returns BSTnode if found, else returns None -- this is the helper function '''
        if self.isEmpty():
            return None
        else:
            return self.find(thing, self.data)

    def find(self, thing, node):
        ''' this is the recursive function '''
        print('working')
        if node.get_data() == thing:
            print("found it")
            return node

    def showTree(self):
        if self.isEmpty():
            return "Sorry, this tree is empty"
        else:
            tempInfo = "My tree has:"
            for node in self.allNodes:
                print(node)
            return str(self.allNodes)

    def getFront(self): return self.front

    def getBack(self): return self.back

    def setData(self, data): self.data = data

    def getData(self): return self.data

    # this will test if the list is empty
    def isEmpty(self): return self.size == 0

    def append(self, data):
        ''' puts data at the end of a list'''
        if self.isEmpty():
            self.front = data
            self.back = self.front
            self.size += 1
            self.allNodes.append(self.data)
        else:
            # create a node with data in it and call it 'temp'
            temp = node(data)
            temp.set_prev(self.back)
            # the new node's (temp) prev becomes the last element in the list
            # the back node's next becomes the newly created node
            self.front.set_next(temp)
            self.front = temp  # updating the back to temp
            self.size += 1
            self.allNodes.append(self.data)

    def prepend(self, data):
        '''puts data at the end of a list'''
        if self.isEmpty():
            self.append(data)
        else:
            # create a node with data in it and call it 'temp'
            temp = node(data)
            temp.setNext(self.front)
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
