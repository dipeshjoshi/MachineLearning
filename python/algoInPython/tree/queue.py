class Queue:

    def __init__(self):
        self.front = -1
        self.rear = -1
        self.maxsize = 100
        self.que = [None] * self.maxsize


    def insert(self, data):
        if(self.front == -1 and self.rear == -1):
            self.front += 1
            self.rear += 1
            self.que[self.rear] = data

        elif(self.rear != self.maxsize-1):
            self.rear += 1
            self.que[self.rear] = data

        else:
            print("Queue full.")


    def deleteFromEnd(self):
        if(self.rear==-1):
            print('Empty Queue.')
        else:
            self.que[self.rear] = None
            if(self.front!=self.rear):
                self.rear -= 1
            else:
                self.front = -1
                self.rear = -1


    def deleteFromBeginning(self):
        if(self.front==-1):
            print('Empty Queue.')
        else:
            self.que[self.front] = None
            if(self.front!=self.rear):
                self.front += 1
            else:
                self.front = -1
                self.rear = -1

    def printQueue(self):
        print('PRINTING QUEUE.............')
        if(self.front == -1 and self.rear == -1):
            print('Empty Queue.')
        else:
            for index in range(self.front, self.rear+1):
                print(self.que[index])


if __name__ == '__main__':
    l = [2,1,6,7,5,9,3,4]
    q = Queue()
    for item in l:
        q.insert(item)
    q.printQueue()
    q.deleteFromEnd()
    q.deleteFromBeginning()
    q.printQueue()
