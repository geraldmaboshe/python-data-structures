class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size1(self):
        return self.size

    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        currentNode = self.head
        while currentNode.nextNode is not None:
            actualNode = currentNode.nextNode
        currentNode.nextNode = newNode

    def remove(self, data):
        if self.head is None:
            return

        self.size = self.size - 1
        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    def traverseList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode


linkedList = LinkedList()
linkedList.insertStart(3)
linkedList.insertStart(30)
linkedList.insertEnd(6)
linkedList.insertStart(90)
linkedList.insertEnd(20)
linkedList.traverseList()
