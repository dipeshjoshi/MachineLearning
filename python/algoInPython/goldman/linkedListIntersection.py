
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(head):
    temp =head
    while temp is not None:
        print temp.data
        temp = temp.next


def findLength(head):
    temp = head
    length = 0
    while temp is not None:
        length += 1
        temp = temp.next
    return length


def findIntersection(head1, head2):
    if head1 is not None and head2 is not None:
        l1 = findLength(head1)
        l2 = findLength(head2)
        temp1 = head1
        temp2 = head2
        if(l1 > l2):
            for index in range(l1-l2):
                temp1 = temp1.next
            while temp1 is not None:
                if(temp1 == temp2):
                    print temp1.data
                    break
                temp1 = temp1.next
                temp2 = temp2.next
        else :
            for index in range(l2-l1):
                temp2 = temp2.next
            while temp2 is not None:
                if(temp1 == temp2):
                    print temp1.data
                    break
                temp1 = temp1.next
                temp2 = temp2.next







l1head  = Node(2)
l1head.next = Node(4)
l1head.next.next = Node(3)
l1head.next.next.next = Node(7)
l1head.next.next.next.next = Node(5)
l1head.next.next.next.next.next = Node(6)

l2head  = Node(9)
l2head.next = l1head.next.next.next.next


findIntersection(l1head, l2head)
