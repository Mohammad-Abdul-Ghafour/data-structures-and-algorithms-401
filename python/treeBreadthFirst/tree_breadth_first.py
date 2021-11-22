from python.trees.tree import Node,Trees
from python.stacksAndQueues.stack_and_queues import Queue

def breadthFirst(tree):
    if tree.root:
        arr = []
        que = Queue()
        que.enqueue(tree.root)
        while que.front:
            treeRoot = que.front.value
            if treeRoot.left:
                que.enqueue(treeRoot.left)
            if treeRoot.right:
                que.enqueue(treeRoot.right)
            arr.append(que.front.value.value)
            que.dequeue()
        return arr
    else:
        raise ValueError("This tree is empty")
        
    
if __name__ == "__main__":
    tree = Trees()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)

    print(breadthFirst(tree))