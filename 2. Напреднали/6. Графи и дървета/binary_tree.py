import random


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def search(root, value_to_search):
    if root is None or root.val == value_to_search:
        return root

    if root.val < value_to_search:
        return search(root.right, value_to_search)
    else:
        return search(root.left, value_to_search)


def iterative_search(root, value_to_search):
    while True:
        if root is None or root.val == value_to_search:
            return root

        if root.val < value_to_search:
            root = root.right
        else:
            root = root.left


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


my_list = [random.randint(0, 10) for _ in range(10)]
print(my_list)

my_tree = Node(10)
for element in my_list:
    inorder_traversal(my_tree)
    print()
    insert(my_tree, Node(element))


result = search(my_tree, 5)

if result is not None:
    print()
    print(f'Value {result.val} found')
else:
    print()
    print('Not found')
