from python.trees.tree import Trees
from python.stacksAndQueues.stack_and_queues import Queue

class Node:
    def __init__(self,value=None):
        self.value = value
        self.childs = []

def getKTreeChild(tree):
    if tree.root:
        output = Queue()
        que = Queue()
        que.enqueue(tree.root)
        while que.front:
            treeRoot = que.front.value
            if treeRoot.childs != []:
                for i,val in enumerate(treeRoot.childs):
                    que.enqueue(treeRoot.childs[i])
            output.enqueue(que.front.value)
            que.dequeue()
        return output
    else:
        raise ValueError("This tree is empty")
        

def fizzBuzzTree(tree):
    if tree.root:
        k_tree = tree
        # treeRoot = k_tree.root
        que = getKTreeChild(k_tree)
        def _travers(node):
            if node.value%3 == 0 and node.value%5 == 0:
                node.value = "FizzBuzz"
            elif node.value%3 == 0 :
                node.value = "Fizz"
            elif node.value%5 == 0 :
                node.value = "Buzz"
            else:
                node.value = str(node.value)
        while que.front:
            _travers(que.front.value)
            que.dequeue()
        return k_tree
    else:
        raise ValueError("This tree is empty")
        # i = 0
        # while que.front:
        #     if que.front.value%3 == 0 and que.front.value%5 == 0:
        #         treeRoot = Node("FizzBuzz")
        #     elif que.front.value%3 == 0 :
        #         treeRoot = Node("Fizz")
        #     elif que.front.value%5 == 0 :
        #         treeRoot = Node("Buzz")
        #     else:
        #         treeRoot = Node(str(que.front.value.value))
        #     treeRoot.childs += que.front.value.childs
        #     if i > len(que.front.value.childs):
        #         i +=1
        #         que.dequeue()

if __name__ == "__main__":
    tree = Trees()
    tree.root = Node(3)
    tree.root.childs = [Node(10),Node(8),Node(9)]
    tree.root.childs[0].childs = [Node(2),Node(5),Node(10)]
    tree.root.childs[1].childs = [Node(3),Node(4),Node(1)]
    tree.root.childs[2].childs = [Node(5),Node(8),Node(6)]
    print(getKTreeChild(tree))
    tree2 = fizzBuzzTree(tree)
    print(tree2.root.value)
    # tree2 = Trees()
    # tree2.root = Node(5)
    # # tree2.root.childs.append(tree.root.childs[0])
    # tree2.root.childs += tree.root.childs
    # tree2.root.childs[0]=Node(41)
    # print(tree2.root.childs)
    # print(tree.root.childs)