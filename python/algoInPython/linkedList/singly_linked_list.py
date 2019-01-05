class Node :
    def __init__(self, data, next):
        self.data = data
        self.next = next


class SinglyLinkedList :

    def __init__(self):
        self.head = None
        self.mid = None


    def addElement(self, data):
        newNode = Node(data, None)
        if self.head is None:
            self.head =  newNode
        else :
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode


    def printLinkedList(self):
        if self.head is not None:
            current_node = self.head

            while current_node is not None:
                print current_node.data, ' --> ',
                current_node = current_node.next
            print None
        else:
            print('Empty Linked List')


    def printUsingHead(self, head):
        if head is not None:
            current_node = head

            while current_node is not None:
                print current_node.data, ' --> ',
                current_node = current_node.next
            print None
        else:
            print('Empty Linked List')


    def search(self, node_value):
        print('Searching Element..............')
        if self.head is not None:
            current_node = self.head
            pos = 1
            while current_node.data != node_value and current_node.next is not None:
                pos += 1
                current_node = current_node.next

                if current_node.data == node_value :
                    print "Data : ", node_value , " is present on ", pos , " Position."
                else :
                    print node_value, " not found in the list."
        else:
            print("Empty Linked List.")


    def deleteNode(self, value):
        print('Deleting Node..................')
        curr_node = self.head
        prev_node = None
        while curr_node is not None:
            if curr_node.data == value:
                if curr_node == self.head:
                    self.head = curr_node.next
                else :
                    prev_node.next = curr_node.next
                break

            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None :
            print value, " Not Found."


    def reverseIterative(self):
        print('Iteratively Reversing Linked List.................')
        if self.head is not None:
            ptr1 = self.head;
            ptr2 = ptr1.next;

            while ptr2 is not None:
                if(ptr1 == self.head):
                    ptr1.next = None
                temp = ptr2.next
                ptr2.next = ptr1

                ptr1 = ptr2
                ptr2 = temp

            self.head = ptr1


    def reverseRecursive(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return

        nextval = curr.next
        curr.next = prev
        self.reverseRecursive(nextval, curr)


    def reversePart(self, curr, prev):
        if curr.next is None:
            self.mid = curr
            curr.next = prev
            return

        nextval = curr.next
        curr.next = prev
        self.reversePart(nextval, curr)


    def reverse(self):
        print('Reversing Linked List Recursively....................')
        if self.head is None:
            return
        self.reverseRecursive(self.head, None)


    def findLenghtRecusively(self, llHead):
        len = 0
        if llHead.next is None:
            return 1

        val = self.findLenghtRecusively(llHead.next)
        len = val + 1
        return len


    def findLenght(self):
        print('Finding Lenght of Linked List........................')
        if self.head is None:
            return 0
        result = self.findLenghtRecusively(self.head)
        print result



    def findMiddle(self):
        print('Finding Middle of Linked List......................')
        if self.head is None:
            return

        if self.head.next is not None:
            slowptr = self.head
            fastptr = self.head

            while fastptr.next is not None and fastptr.next.next is not None:
                slowptr = slowptr.next
                fastptr = fastptr.next.next
            return slowptr
        else:
            return self.head



    def findPalindrome(self):
        print('Finding If Linked List is Palindrome or Not?..............')
        if self.head is None:
            return

        mdl = self.findMiddle()
        temp = mdl.next
        mdl.next = None
        self.reversePart(temp, None)
        mdl.next = self.mid
        self.printLinkedList()
        ptr1 = self.head
        ptr2 = self.mid
        while ptr2.next is not None:
            if(ptr1.data != ptr2.data):
                return 'No'
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return 'Yes'


    def swapNodes(self):
        if self.head is not None:
            x = input("Enter the value of X: ")
            y = input("Enter the value of Y: ")
            print x,y
            prevX = None
            currX = self.head
            prevY = None
            currY = self.head
            while currX is not None:
                if(currX.data == x ):
                    break
                prevX = currX
                currX = currX.next


            while currY is not None:
                if(currY.data == y ):
                    break
                prevY = currY
                currY = currY.next

            # If either x or y is not present, nothing to do
            if currX == None or currY == None:
                return
            # If x is not head of linked list
            if prevX != None:
                prevX.next = currY
            else: #make y the new head
                self.head = currY

            # If y is not head of linked list
            if prevY != None:
                prevY.next = currX
            else: # make x the new head
                self.head = currX

            temp = currX.next
            currX.next = currY.next
            currY.next = temp






if __name__=="__main__":
    inputList = [8,5,1,4,7,4,1,5,8,0]
    s = SinglyLinkedList()
    for item in inputList :
        s.addElement(item)

    s.printLinkedList()
    #s.search(3)
    #s.deleteNode(1)
    #s.printLinkedList()
    #s.deleteNode(2)
    #s.printLinkedList()
    #s.deleteNode(13)
    #s.deleteNode(7)
    #s.printLinkedList()
    #s.reverseIterative()
    #s.reverse()
    #s.printLinkedList()
    #s.findLenght()
    #result = s.findPalindrome()
    #print result
    a = s.findMiddle()  
    print(a.data)
    '''
    s.swapNodes()
    s.printLinkedList()
    inputList2 = [3,1,6,2,9,6,4,7]
    t = SinglyLinkedList()
    for item in inputList2 :
        t.addElement(item)
    t.printLinkedList()
    '''
