import singly_linked_list as sll

class nthNodeFromEnd:

    def findNode(self, inputLinkedList, n):
        if inputLinkedList.head is not None:
            temp  = inputLinkedList.head

        for index in range(n-1):
            if temp is not None:
                temp = temp.next

        if temp is not None:
            temp1 = inputLinkedList.head
            while temp.next is not None :
                temp = temp.next
                temp1 = temp1.next
            print n, " value from last is : ", temp1.data
        else :
            print "Lenght of linked list is smaller then ", n

if __name__=="__main__":
    n = input("Enter the value of n : ")
    inputList = [9,3,1,4,7,8,2,5]
    s = sll.SinglyLinkedList()
    for item in inputList:
        s.addElement(item)
    s.printLinkedList()
    nnode = nthNodeFromEnd()
    nnode.findNode(s, n)
