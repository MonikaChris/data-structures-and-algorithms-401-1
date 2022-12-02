#from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue


def get_fb_val(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


def fizz_buzz_tree(tree):

    # If tree is empty, return None
    if not tree.root:
        return None

    # Queue to hold nodes during traversal
    nodes = Queue()

    dic = {}

    # Initialize new tree
    new_tree = KaryTree()

    # Build new tree while traversing old tree
    nodes.enqueue(tree.root)

    count = 0

    while not nodes.is_empty():
        node = nodes.dequeue()
        new_node = Node(get_fb_val(node.value))
        new_node.children = node.children
        dic[count] = node
        count += 1

        for child in node.children:
            nodes.enqueue(child)

    for i in dic.keys():
        for child in dic[i].children:
            child.value = get_fb_val(child.value)

    dic[0].value = get_fb_val(dic[0].value)

    new_tree.root = dic[0]

    return new_tree














