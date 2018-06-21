class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList :
    head = None
    tail = None

    def addElement(self, node_value):
        newNode = Node(node_value)
        newNode.data = node_value
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            newNode.next = None
            self.tail = newNode


    def printLinkedList(self):
        current_node = self.head
        while current_node is not None:
            print current_node.data , ' --> ',
            current_node = current_node.next

        print None


    def printLinkedListReversed(self):
        current_node = self.tail
        while current_node is not None:
            print current_node.data , ' --> ',
            current_node = current_node.prev

        print None


    def search(self, node_value):
        curr_node = self.head
        counter = 1
        while curr_node.data != node_value and curr_node.next is not None:
            counter += 1
            curr_node = curr_node.next

        if curr_node.data == node_value :
            print node_value, " found at ", counter , " Position. "

        else :
            print node_value, " not found."


    def remove(self, node_value):
        curr_node = self.head
        while curr_node.data != node_value and curr_node.next is not None:
            curr_node = curr_node.next

        if curr_node.data == node_value:            # Data Found In List.
            if curr_node == self.head :
                if self.head.next is not None:
                    self.head = curr_node.next
                    self.head.prev = None
                else:
                    self.head = None
                    self.tail = None
            elif curr_node == self.tail :
                self.tail = curr_node.prev
                self.tail.next = None
            else :
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev

        else :
            print node_value, "Not Found."




d = DoublyLinkedList()
d.addElement(2)
d.addElement(1)
d.addElement(5)
d.addElement(3)
d.addElement(6)
d.addElement(8)
d.printLinkedList()
d.printLinkedListReversed()
d.search(8)
d.remove(2)
d.printLinkedList()
d.printLinkedListReversed()
