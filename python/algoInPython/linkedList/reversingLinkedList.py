import singly_linked_list as sll

class ReverseLinkedList:

    def reverseIterative(self, linkedList):
        if linkedList.head is not None:
            ptr1 = linkedList.head;
            ptr2 = ptr1.next;

            while ptr2 is not None:
                if(ptr1 == linkedList.head):
                    ptr1.next = None
                temp = ptr2.next
                ptr2.next = ptr1

                ptr1 = ptr2
                ptr2 = temp

            linkedList.head = ptr1


    def reverse(self):







if __name__=='__main__':
    inputList = [9,2,3,4]
    lList = sll.SinglyLinkedList()
    for item in inputList:
        lList.addElement(item)
    lList.printLinkedList()
    rev = ReverseLinkedList()
    #rev.reverseIterative(lList)
    #lList.printLinkedList()

    rev.recursiveReverse(lList.head)
