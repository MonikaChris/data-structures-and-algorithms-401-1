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

    # Queue for breadth first traversal
    queue = Queue()

    # Store each node from tree in list, store number of children for each node in dictionary
    new_nodes = []
    num_of_children = {}

    # Initialize queue with root node
    queue.enqueue(tree.root)

    # Initialize counter for dictionary keys
    count = 0

    # Traverse tree, for each node, create new FizzBuzzed node and store in list, update dictionary
    while not queue.is_empty():
        # Get current node, create new FizzBuzz node
        node = queue.dequeue()
        new_node = Node(get_fb_val(node.value))

        # Store number of children in dictionary for nth new node
        if node.children:
            num_of_children[count] = len(node.children)
        else:
            num_of_children[count] = 0

        count += 1

        # Append nth new node to nodes list
        new_nodes.append(new_node)

        # Enqueue child nodes
        if len(node.children) > 0:
            for child in node.children:
                queue.enqueue(child)

    # Assign child nodes - group_idx is starting index for group of child nodes for current node
    group_idx = 1
    for i in range(len(new_nodes)):
        node = new_nodes[i]
        node_children = []

        if num_of_children[i] > 0:
            for j in range(group_idx, group_idx + num_of_children[i]):
                node_children.append(new_nodes[j])
            node.children = node_children
            node_children = []
            group_idx += num_of_children[i]

    new_tree = KaryTree(new_nodes[0])

    return new_tree


