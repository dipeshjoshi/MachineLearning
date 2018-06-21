


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(head):
    temp = head
    while temp is not None:
        print temp.data
        temp = temp.next

def lenght(head):
    lenght = 0
    temp = head
    while temp is not None:
        lenght += 1
        temp = temp.next
    return lenght



def nthNodeFromEnd(head, n):

    l = lenght(head)
    if n > l:
        print "invalid n......"
        return 0
    temp1 = head
    temp2 = head
    for index in range(n):
        temp1 = temp1.next
    while temp1 is not None:
        temp1 = temp1.next
        temp2 = temp2.next
    print temp2.data


def cycleOrNot(head):
    slow = head
    fast = head
    cycleFlag = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            cycleFlag = 1
            break
    if cycleFlag == 0:
        print "No cycle."
    else:
        print "cycle"


def cycleStart(head):
    slow = head
    fast = head
    cycleFlag = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            cycleFlag = 1
            #Now finding start of cycle.
            slow = head
            while(slow != fast):
                slow = slow.next
                fast = fast.next
            print slow.data
            break
    if cycleFlag == 0:
        print "No cycle."
    else:
        print "cycle"



def cycleLenght(head):
    slow = head
    fast = head
    cycleFlag = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            cycleFlag = 1
            lenght = 1
            slow = slow.next
            while slow!=fast:
                lenght += 1
                slow = slow.next
            print lenght
            break
    if cycleFlag == 0:
        print "No cycle."
    else:
        print "cycle"



def printReverse(head):
    if head is not None:
        printReverse(head.next)
        print head.data
    return 0


#With 3 pointers
def reverseIterative(head):
    prev = None
    curr = head
    nextptr = None
    while curr is not None:
        nextptr = curr.next
        curr.next = prev

        prev = curr
        curr = nextptr
    head = prev
    return head


#WIth 2 pointers
def reverseRecursive(curr, prev):
    if curr is not None:
        reverseRecursive(curr.next, curr)
        curr.next = prev




head = LLNode(3)
head.next = LLNode(1)
head.next.next = LLNode(4)
head.next.next.next = LLNode(5)
head.next.next.next.next = LLNode(9)
head.next.next.next.next.next = LLNode(6)
head.next.next.next.next.next.next = LLNode(8)
head.next.next.next.next.next.next.next = LLNode(2)

head = reverseRecursive(head, None)
printLL(head)
