import queue as q
from collections import deque

stack = []
queue = deque([])

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorderRecursive(root):
    if root is not None:
        print(root.data)
        preorderRecursive(root.left)
        preorderRecursive(root.right)


def preorderNonrecursive(root):
    while(1):
        while(root):
            print(root.data)
            stack.append(root)
            root = root.left
        if not stack:
            break
        root = stack.pop()
        root = root.right


def postorderRecursive(root):
    if root is not None:
        postorderRecursive(root.left)
        postorderRecursive(root.right)
        print(root.data)


#  postorderNonrecursive not working
def postorderNonrecursive(root):
    while 1:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            break

        root = stack.pop()
        root = root.right
        if(root is not None):
            print root.data


def inorderRecursive(root):
    if root is not None:
        inorderRecursive(root.left)
        print(root.data)
        inorderRecursive(root.right)



def inorderNonrecursive(root):
    while 1:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            break

        root = stack.pop()
        print root.data
        root = root.right



def levelorder(root):
    if root is not None:
        queue.append(root)

    while queue:
        root = queue.popleft()
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)
        print root.data




if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("Preorder")
    preorderRecursive(root)
    print("Inorder")
    inorderRecursive(root)
    print("Postorder")
    postorderRecursive(root)
    #print("Nonrecursive preorder")
    #postorderNonrecursive(root)
    print("Levelorder")
    levelorder(root)
