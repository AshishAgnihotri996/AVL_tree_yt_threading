import queue


class AVLTree:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1
        
def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    preOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    preOrderTraversal(rootNode.rightchild)
    
def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)
    
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customQueue = queue.Queue()
    customQueue.enqueue = rootNode
    while not customQueue.isEmpty():
        root = customQueue.enqueue()
        print(root.value.data)
        if rootNode.value.leftchild is not None:
            customQueue.enqueue(rootNode.value.leftchild)
        if rootNode.value.rightchild is not None:
            customQueue.enqueue(root.value.rightchild)

def searchNode(rootNode,nodeValue):
    if rootNode.data == nodeValue:
        print('node found')
    elif nodeValue < rootNode.data:
        if rootNode.leftchild.data == nodeValue:
            print('found')
        else:
            searchNode(rootNode.leftchild, nodeValue)
    else:
        if nodeValue > rootNode.data:
            if rootNode.rightchild.data == nodeValue:
                print('found')
            else:
                searchNode(rootNode.rightchild,nodeValue)

def getHieght(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftchild
    disbalanceNode.leftchild = disbalanceNode.leftchild.rightchild
    newRoot.right = disbalanceNode
    disbalanceNode.height = 1 + max(getHieght(newRoot.leftchild),getHieght(newRoot.righchild))
    newRoot.height = 1 + max(getHieght(newRoot.leftchild),getHieght(newRoot.rightchild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightchild
    disbalanceNode.rightchild  = disbalanceNode.rightchild.leftchild
    newRoot.leftchild = disbalanceNode
    disbalanceNode.height = 1 + max(getHieght(newRoot.leftchild),getHieght(newRoot.rightchild))
    newRoot.height = 1 + max(getHieght(newRoot.leftchild), getHieght(newRoot.rightchild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHieght(rootNode.leftchild) - getHieght(rootNode.rightchild)

def insertNode(rootNode,nodeValue):
    if not rootNode:
        return  AVLTree(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftchild = insertNode(rootNode.leftchild, nodeValue)
    else:
        rootNode.rightchild = insertNode(rootNode.rightchild, nodeValue)
    rootNode.height =  1 + max(getHieght(rootNode.leftchild),getHieght(rootNode.rightchild))
    balance = getBalance(rootNode)

    if balance > 1 and nodeValue < rootNode.leftchild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftchild.data:
        rootNode.leftchild = leftRotate(rootNode.leftchild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightchild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightchild.data:
        rootNode.rightchild = rightRotate(rootNode.rightchild)
        leftRotate(rootNode)
    return rootNode







newAVL  = AVLTree(10)

