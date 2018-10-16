class Sorting :
    def __init__(self):
        self.arr = [1,6,2,7,4,8,0,9,3]
        
    def printArr(self):
        for index in range(len(self.arr)):
            print(self.arr[index])
     
    def bubbleSort(self):
        for i in range(len(self.arr)):
            for j in range(i,len(self.arr)):
                if(self.arr[i] > self.arr[j]):
                    tmp = self.arr[i]
                    self.arr[i] = self.arr[j]
                    self.arr[j] = tmp
                    
    def selectionSort(self):
        for i in range(len(self.arr)):
            min = self.arr[i]
            for j in range(i,len(self.arr)):
                if(min > self.arr[j]):
                    self.arr[i] = self.arr[j]
                    self.arr[j] = min
                    min = self.arr[i]
        
        
    def insertionSort(self):
        for i in range(len(self.arr)):
            for j in range(i, 0, -1):
                if(self.arr[j] < self.arr[i]):
                    tmp = self.arr[i]
                    self.arr[i] = self.arr[j]
                    self.arr[j] = tmp
                else:
                    break
        
    def quickSortPartition(self, first, last, pivot):
        while(first <= last):
            while(self.arr[first] < pivot):
                first += 1
                
            while(self.arr[last] >= pivot):
                last -= 1
            
            #swap elements
            tmp = self.arr[first]
            self.arr[first] = self.arr[last]
            self.arr[last] = tmp
                
            
                
            
    def quickSort(self):
        
        
        
            
                
     

if __name__=='__main__':
    s = Sorting()
    s.printArr()
    s.bubbleSort()
    print("After Bubble Sorting.....")
    s.printArr()
    s.selectionSort()
    print("After Selection Sorting.....")
    s.printArr()
    s.insertionSort()
    print("After Insertion Sorting.....")
    s.printArr()
    