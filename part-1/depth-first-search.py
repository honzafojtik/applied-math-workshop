import time
from colorama import init, Fore, Style

init(autoreset=True)

# 
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.visited = False

# define a connect function to avoid silent typos
def connect(parent, left=None, right=None):
    parent.left = left
    parent.right = right

# firstNode is also the root node, named firstNode here for clarity

firstNode = Node(1)
secondNode = Node(7)
thirdNode = Node(9)
fourthNode = Node(2)
fifthNode = Node(6)
sixthNode = Node(9)
seventhNode = Node(5)
eightNode = Node(11)
ninthNode = Node(5)

connect(firstNode, secondNode, thirdNode)
connect(secondNode, fourthNode, fifthNode)
connect(thirdNode, sixthNode)
# fourthNode (2) has no child nodes
connect(fifthNode, seventhNode, eightNode)
connect(sixthNode, ninthNode)
# seventh, eight and ninth are leaf nodes, hence no child nodes

# depth first search for a specific value in a binary tree
def depth_first_search(root, value, depth=0):
    # indent and depth are only used for visual formatting only
    indent = "  " * depth
    # reached the end of a branch
    if root is None:
        print(f"{indent}{Fore.RED}Hit a leaf node, going back.")
        return False
    
    # visiting a valid node
    print(f"{indent}{Fore.YELLOW}Visiting node {root.data}")
    # marks the node as visited
    root.visited = True

    # found the value that we were looking for
    if root.data == value:
        print(f"{indent}{Fore.GREEN}Found the value: {value}!")
        # bubbles True up the call stack
        return True

    print(f"{indent}{Fore.CYAN}Going left from {root.data}")
    # recursively call the function and dig into the left child of currently looked at node if it exists
    left_result = depth_first_search(root.left, value, depth + 1)

    print(f"{indent}{Fore.MAGENTA}Going right from {root.data}")
    # recursively call the function and dig into the right child of currently looked at node if it exists
    right_result = depth_first_search(root.right, value, depth + 1)

    # if a node has no children, i.e. is a leaf node, backtrack
    if not (left_result or right_result):
        print(f"{indent}{Style.DIM}{Fore.RED}Backtracking from node {root.data}")

    # if a node has at least one child, return true
    return left_result or right_result


if __name__ == "__main__":
    # specify value that we're looking for
    value = 11
    if depth_first_search(firstNode, value):
        print(f"{value} is found in the binary tree")
    else:
        print(f"{value} is not found in the binary tree")
