import time
import os
from colorama import init, Fore, Style

init(autoreset=True)

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.visited = False

# safer tree connection helper
def connect(parent, left=None, right=None):
    parent.left = left
    parent.right = right

# build the tree
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
connect(fifthNode, seventhNode, eightNode)
connect(sixthNode, ninthNode)

# visual tree printer
def print_tree(node, current=None, indent="", is_left=True):
    if node is None:
        return

    print_tree(node.right, current, indent + ("│   " if is_left else "    "), False)

    prefix = indent + ("└── " if is_left else "┌── ")
    color = Fore.YELLOW if node == current else Fore.WHITE
    print(f"{prefix}{color}{node.data}{Style.RESET_ALL}")

    print_tree(node.left, current, indent + ("    " if is_left else "│   "), True)

# DFS with visual updates
def depth_first_search(root, value, depth=0, delay=0.8):
    if root is None:
        os.system("cls" if os.name == "nt" else "clear")
        print_tree(firstNode)
        print(f"{Fore.RED}Hit a leaf node, going back.")
        time.sleep(delay)
        return False

    os.system("cls" if os.name == "nt" else "clear")
    print_tree(firstNode, current=root)
    print(f"{Fore.YELLOW}Visiting node {root.data}")
    time.sleep(delay)

    root.visited = True

    if root.data == value:
        print(f"{Fore.GREEN}Found the value: {value}!")
        return True

    print(f"{Fore.CYAN}Going left from {root.data}")
    left_res = depth_first_search(root.left, value, depth + 1, delay)

    if left_res:
        return True

    print(f"{Fore.MAGENTA}Going right from {root.data}")
    right_res = depth_first_search(root.right, value, depth + 1, delay)

    if not right_res:
        print(f"{Style.DIM}{Fore.RED}Backtracking from node {root.data}")
        time.sleep(delay)

    return right_res

if __name__ == "__main__":
    value = 11
    if depth_first_search(firstNode, value):
        print(f"{Fore.GREEN}{value} is found in the binary tree")
    else:
        print(f"{Fore.RED}{value} is not found in the binary tree")
