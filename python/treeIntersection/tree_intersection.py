from python.hashtable.hash_table import HashTable
from python.trees.tree import Trees , Node

def tree_intersection(tree1 , tree2):
    if tree1.root == None:
        return "First tree in the arguments are empty"
    elif tree2.root == None:
        return "Second tree in the arguments are empty"
    else:
        travers1 = tree1.preOrder()
        arr1 = travers1(tree1.root)
        travers2 = tree2.preOrder()
        arr2 = travers2(tree2.root)
        # hash_map = HashTable()
        output = ""
        for i in arr1:
            if i in arr2:
                output += f"{i} , "
        #     hash_map.add(i,i)
        # for i in arr2:
        #     is_contain = hash_map.contains(i)
        #     if is_contain:
        #         output += f"{i} , "
        if output == "":
            output = "There are no common values"
        return output


if __name__ == "__main__":
    tree1 = Trees()
    tree1.root = Node(150)
    tree1.root.right = Node(250)
    tree1.root.left = Node(100)

    tree1.root.right.left = Node(200)
    tree1.root.right.right = Node(350)

    tree1.root.right.right.right = Node(500)
    tree1.root.right.right.left = Node(300)

    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(160)

    tree1.root.left.right.right = Node(175)
    tree1.root.left.right.left = Node(125)


    tree2 = Trees()
    tree2.root = Node(42)
    tree2.root.right = Node(600)
    tree2.root.left = Node(100)

    tree2.root.right.left = Node(200)
    tree2.root.right.right = Node(350)

    tree2.root.right.right.right = Node(500)
    tree2.root.right.right.left = Node(4)

    tree2.root.left.left = Node(15)
    tree2.root.left.right = Node(160)

    tree2.root.left.right.right = Node(175)
    tree2.root.left.right.left = Node(125)

    print(tree_intersection(tree1,tree2))