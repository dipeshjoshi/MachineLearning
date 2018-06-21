class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class CircularLinkedList:
    head = None

    def makeCircularAtGivenNode(self, nodeList, position):
        counter = 0
        temp = None
        temp1 = None
        for item in nodeList:
            newNode = Node(item, None)
            counter += 1
            if self.head is None:
                self.head = newNode
                temp = self.head
            else:
                temp.next = newNode
                temp = temp.next

            if counter == position:
                temp1 = newNode

        temp.next = temp1


    def printCircularList(self, nodeList):
        temp = self.head
        for index in range(len(nodeList)):
            print temp.data , " ---> ", temp.next.data
            temp = temp.next


if __name__=="__main__":
    inputList = [4,1,5,2,6,7,3]
    position = 4
    c = CircularLinkedList()
    c.makeCircularAtGivenNode(inputList, position)
    c.printCircularList(inputList)
