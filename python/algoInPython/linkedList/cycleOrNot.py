import circularAtGivenNode as cirList
import singly_linked_list as sll

class CycleOrNot():
    def isCycle(self, inputList):
        if inputList is not None:
            fast = inputList.head
            slow = inputList.head
        while(slow is not None and fast is not None):
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            if slow == fast:
                print "Circular Linked List."
                break
        if slow != fast:
            print "Non Circular Linked List."



if __name__=="__main__":
    inputList = [4,1,5,2,6,7,3]
    position = 4
    circularList = cirList.CircularLinkedList()
    circularList.makeCircularAtGivenNode(inputList, position)
    circularList.printCircularList(inputList)
    c = CycleOrNot()
    c.isCycle(circularList)
    '''
    inputList = [9,3,1,4,7,8,2,5]
    s = sll.SinglyLinkedList()
    for item in inputList:
        s.addElement(item)
    s.printLinkedList()
    c = CycleOrNot()
    c.isCycle(s)
    '''
