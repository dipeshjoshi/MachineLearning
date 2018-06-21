from collections import deque

queue = deque([])
stack = []
global preIndex = 0

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



def findMaxElement(root):
    if root is not None:
        left = findMaxElement(root.left)
        right = findMaxElement(root.right)
        return max(left,right,root.data)
    return 0

def findMaxElementNonrecursive(root):
    max = -10000000
    if root is not None:
        queue.append(root)

    while queue:
        root = queue.popleft()
        if root.data > max:
            max = root.data

        if root.left is not None:
            queue.append(root.left)

        if root.right is not None:
            queue.append(root.right)

    return max



def searchingElement(root, number):
    if root is not None:
        if root.data == number:
            print("Data found in tree.......")
            return 0
        searchingElement(root.left, number)
        searchingElement(root.right, number)


def searchingElementNonrecursive(root, number):
    if root is not None:
        queue.append(root)
    while queue:
        root = queue.popleft()
        if root.data == number:
            print("Data found in tree.......")
            break

        if root.left is not None:
            queue.append(root.left)

        if root.right is not None:
            queue.append(root.right)


def binaryTreeSize(root):
    if root is not None:
        left = binaryTreeSize(root.left)
        right = binaryTreeSize(root.right)
        return left + right + 1
    return 0


def binaryTreeSizeNonrecursive(root):
    size = 0
    if root is not None:
        queue.append(root)

    while queue:
        root = queue.popleft()
        size += 1
        if root.left is not None :
            queue.append(root.left)
        if root.right is not None :
            queue.append(root.right)

    return size



def levelorderReverseOrder(root):
    if root is not None:
        queue.append(root)

    while queue:
        root = queue.popleft()
        if root.right is not None:
            queue.append(root.right)
        if root.left is not None:
            queue.append(root.left)
        stack.append(root.data)

    stack.reverse()
    print stack


def binartTreeHeight(root):
    if root is not None:
        left = binartTreeHeight(root.left)
        right = binartTreeHeight(root.right)
        return max(left,right)+1

    return 0


def binaryTreeHeightNonrecursive(root):
    height = 0
    if root is not None:
        queue.append(root)
        queue.append('$')

    while queue:
        root = queue.popleft()
        if root == '$':
            height += 1
            if queue:
                queue.append('$')
        else:
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)

    return height


def findLeaveNodes(root):
    if root is not None:
        queue.append(root)
    while queue:
        root = queue.popleft()
        if root.left is None and root.right is None:
            print root.data
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)
    return 0


def findFullNodes(root):
    if root is not None:
        queue.append(root)
    while queue:
        root = queue.popleft()
        if root.left is  not None and root.right is not None:
            print root.data
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)
    return 0


def findHalfNodes(root):
    if root is not None:
        queue.append(root)
    while queue:
        root = queue.popleft()
        if (root.left is not None and root.right is  None) or (root.left is None and root.right is not None):
            print root.data
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)
    return 0


def diameterOfBinaryTree(root, max_dia):
    if root is not None:
        left, dia= diameterOfBinaryTree(root.left, max_dia)
        right, dia = diameterOfBinaryTree(root.right, max_dia)
        if((left + right + 1) > max_dia):
            max_dia = left + right + 1
        return max(left,right)+1, max_dia
    return 0, 0



def levelWithMaxSumBinaryTree(root):
    lvl_sum = 0
    max_sum = 0
    if root is not None:
        queue.append(root)
        queue.append('$')
    while queue:
        root = queue.popleft()
        if root == '$':
            if max_sum < lvl_sum:
                max_sum = lvl_sum
                lvl_sum = 0
            if queue:
                queue.append("$")
        else:
            lvl_sum += root.data
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
    return max_sum


def sumOfAllElementsRecursive(root):
    if root is not None:
        left = sumOfAllElementsBinaryTree(root.left)
        right = sumOfAllElementsBinaryTree(root.right)
        return left + right + root.data
    return 0



def sumOfAllElementsNonrecursive(root):
    sum = 0
    if root is not None:
        queue.append(root)
    while queue:
        root = queue.popleft()
        sum += root.data

        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)

    return sum


#PLEASE COMPLETE THIS ONE.
def existingPathWithGivenSum(root, sum):
    if root is not None and sum < root.data:
        if sum == 0 :
            print("PAth exist")
        left = existingPathWithGivenSum(root.left,sum-root.data)
        right = existingPathWithGivenSum(root.right,sum-root.data)



def leastCommonAncestorBinaryTree(root, node1, node2):

    if root is not None:
        left = leastCommonAncestorBinaryTree(root.left, node1, node2)
        right = leastCommonAncestorBinaryTree(root.right, node1, node2)
        if ((left and right) or ((root.data==node1 or root.data==node2) and left) or ((root.data==node1 or root.data==node2) and right)):
            print root.data
        if root.data == node1 or root.data == node2 or left==1 or right==1:
            return 1
        else:
            return 0
    return 0


def convertMirrorOfBinaryTree(root):
    if root is not None:
        convertMirrorOfBinaryTree(root.left)
        convertMirrorOfBinaryTree(root.right)

        #Swap left and right node
        temp = root.left
        root.left = root.right
        root.right = temp



def searchInorderIndex(inorder, inStrt, inEnd, root):
    index = inStrt

    while inEnd:
        if(inorder[index] == root):
            return index
        else:
            index += 1
    return 0



def ifSumTree(root):
    if root is not None:
        left = ifSumTree(root.left)
        right = ifSumTree(root.right)

        if(((left + right == root.data) or (left==0 and right==0)) and (left != -1 and right != -1)):
            return left + right + root.data
        else:
            print root.data
            return -1
    return 0




#COMPLETE THIS FUNCTION
def constructTreeByInorderPreorder(inorder , preorder, inStrt, inEnd):
    root = preorder[preIndex]
    curr_node = Node(root)
    preIndex += 1

    index = searchInorderIndex(inorder, inStrt, inEnd, root)

    curr_node.left = constructTreeByInorderPreorder(inorder, preorder, inStrt, index-1)
    curr_node.right = constructTreeByInorderPreorder(inorder, preorder, index+1, inEnd)

    return curr_node



if __name__=='__main__':
    root = Node(1)
    root.left = Node(32)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(19)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.left = Node(71)
    root.right.right.left.right = Node(31)
    inorder = 'DBEAFC'
    preorder = 'ABDECF'
    constructTreeByInorderPreorder(inorder, preorder, 0, 5)
