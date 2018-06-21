import singly_linked_list as sll



def reverse(inputLinkedList):
    if(inputLinkedList is not None):
        start = inputLinkedList
        reverse(start.next)
        print start.data


if __name__=="__main__":
    inputList = [9,3,1,4,7,8,2,5]
    lList = sll.SinglyLinkedList()
    for item in inputList:
        lList.addElement(item)
    lList.printLinkedList()
    reverse(lList.head)
