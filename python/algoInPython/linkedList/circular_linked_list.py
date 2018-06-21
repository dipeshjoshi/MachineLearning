# Implemeting Circular Linked List only with head pointer.
'''

     head ->3  -->  1  --> 4  --> 7  -->  6
            ^                             |
            |_____________________________|
'''

class Node :
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList :
    head = None

    def insertAtEnd(self, node_value):
        newNode = Node(node_value)
        if self.head is None :
            self.head = newNode
        else:
            curr_node = self.head
            while curr_node.next != self.head :
                curr_node = curr_node.next
            curr_node.next = newNode
        newNode.next = self.head


    def insertAtBeginning(self, node_value):
        newNode = Node(node_value)
        if self.head is None :
            self.head = newNode
        else:
            curr_node = self.head
            while curr_node.next != self.head :
                curr_node = curr_node.next
            curr_node.next = newNode
            newNode.next = self.head
            self.head = newNode


    def insertOnGivenPosition(self, node_value, pos):
        newNode = Node(node_value)
        if self.head is not None :
            curr_node = self.head
            prev_node = None
            while(pos):
                if curr_node.next == self.head:
                    print "Linked list is small to the given number."
                    break;
                pos -= 1
                prev_node = curr_node
                curr_node = curr_node.next

            if pos == 0:
                prev_node.next = newNode
                newNode.next = curr_node


    def printList(self):
        curr_node = self.head;
        if curr_node is None:
            print "Empty List"
        else:
            while curr_node.next != self.head:
                print curr_node.data, " --> ",
                curr_node = curr_node.next
            print curr_node.data



c = CircularLinkedList()
c.insertAtEnd(2)
c.insertAtEnd(1)
c.insertAtEnd(4)
c.insertAtEnd(3)
c.insertAtEnd(6)
c.insertAtEnd(5)
c.printList()
c.insertAtBeginning(7)
c.printList()
c.insertAtEnd(0)
c.printList()
c.insertOnGivenPosition(8, 7)
c.printList()
