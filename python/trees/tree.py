

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
    
    # def preOrder(self,node,output = []):
    #     output.append(node.value)
    #     if node.left:
    #         self.preOrder(node.left,output)
    #     if node.right:
    #          self.preOrder(node.right,output)
    #     return output

    # def inOrder(self,node,output = []):
    #     if node.left:
    #         self.inOrder(node.left)
    #     output.append(node.value)
    #     if node.right:
    #         self.inOrder(node.right)
    #     return output
    
    # def postOrder(self,node,output = []):
    #     if node.left:
    #         self.postOrder(node.left)
    #     if node.right:
    #         self.postOrder(node.right)
    #     output.append(node.value)
    #     return output

class SearchTree(Trees):

    def add(self,value):
        if not self.root:
            self.root = Node(value)
        else:
            def _travers(current):
                if value < current.value:
                    if not current.left:
                        current.left = Node(value)
                        return
                    else:
                        _travers(current.left)
                else:
                    if not current.right:
                        current.right = Node(value)
                        return
                    else:
                        _travers(current.right)
            _travers(self.root)

    def contains(self, value):
        if not self.root:
            raise ValueError("This tree is empty")
        def _travers(current):
            if value == current.value:
                # print(True)
                return True
            elif value < current.value:
                if current.left:
                  return  _travers(current.left)
                else:
                    return False
            else:
                if current.right:
                  return  _travers(current.right)
                else:
                    return False
        return _travers(self.root)

    # def add(self,value):
    #     if not self.root:
    #         self.root = Node(value)
    #     else:
    #         current = self.root
    #         while current:
    #             if value < current.value:
    #                 if not current.left:
    #                     current.left = Node(value)
    #                     break
    #                 else:
    #                     current = current.left
    #                     continue
    #             else:
    #                 if not current.right:
    #                     current.right = Node(value)
    #                     break
    #                 else:
    #                     current = current.right
    #                     continue
    # def contains(self, value):
    #     if not self.root:
    #         raise ValueError("This tree is empty")
    #     current = self.root
    #     while current:
    #         if value == current.value:
    #             return True
    #         elif value < current.value:
    #             if current.left:
    #                 current = current.left
    #                 continue
    #             else:
    #                 return False
    #         else:
    #             if current.right:
    #                 current = current.right
    #                 continue
    #             else:
    #                 return False


if __name__ == "__main__":
    tree = SearchTree()
    tree.root = Node(8)
    tree.add(7)
    tree.add(9)
    tree.add(5)
    tree.add(14)

    # tree.root.left = Node(4)
    # tree.root.right = Node(6)
    # tree.root.left.left = Node(3)
    # tree.root.left.right = Node(4)
    travers = tree.preOrder()
    travers2 = tree.inOrder()
    travers3 = tree.postOrder()

    print(travers(tree.root))
    print(travers2(tree.root))
    print(travers3(tree.root))
    # print(tree.inOrder(tree.root))
    # print(tree.postOrder(tree.root))
    print(tree.contains(5))
    print(tree.contains(10))
