


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def ifSumTree(root):
    if root is not None:
        left = ifSumTree(root.left)
        right = ifSumTree(root.right)

        if(((left + right == root.data) or (left==0 and right==0)) and (left != -1 and right != -1)):
            return left + right + root.data
        else:
            return -1
    return 0


if __name__=='__main__':
    root = Node(24)
    root.left = Node(5)
    root.right = Node(7)
    root.left.left = Node(4)
    root.left.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(4)
    output = ifSumTree(root)
    if output == -1:
        print("No")
    else:
        print("Yes")
