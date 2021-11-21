class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

class Trees:
    def __init__(self):
        self.root = None

    def preOrder(self):
        output=[]
        def _travers(node):
            output.append(node.value)
            if node.left:
                _travers(node.left)
            if node.right:
                _travers(node.right)
            return output
        return _travers

    def inOrder(self):
        output=[]
        def _travers(node):
            if node.left:
                _travers(node.left)
            output.append(node.value)
            if node.right:
                _travers(node.right)
            return output
        return _travers
    
    def postOrder(self):
        output=[]
        def _travers(node):
            if node.left:
                _travers(node.left)
            if node.right:
                _travers(node.right)
            output.append(node.value)
            return output
        return _travers

    # def maxValue(self):
    #     travers = self.preOrder()
    #     arr = travers(self.root)
    #     output = 0
    #     for i in arr:
    #         if i > output:
    #             output = i
    #     return output

    def maxValue(self):
        if self.root:
            self.max_value = 0
            def _travers(node):
                if node.value > self.max_value:
                    self.max_value = node.value
                if node.left:
                    _travers(node.left)
                if node.right:
                    _travers(node.right)
                return self.max_value
            return _travers(self.root)
        else:
            raise ValueError('This tree is empty')
    
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

    print(tree.maxValue())



