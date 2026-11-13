"""Assessment 3.4 - Program for Diagram 1: Binary Tree (BFS and DFS)

The tree is built level by level (left to right) from the letters of
your Last Name. Change LAST_NAME to your own.
"""
from collections import deque

LAST_NAME = "SEGUNDINO"   # <-- change to your last name


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(name):
    """Algorithm A: build the binary tree from the letters of the name."""
    letters = list(name.upper())
    if not letters:
        return None
    root = Node(letters[0])
    queue = deque([root])
    i = 1
    while i < len(letters):
        parent = queue.popleft()
        parent.left = Node(letters[i])
        queue.append(parent.left)
        i += 1
        if i < len(letters):
            parent.right = Node(letters[i])
            queue.append(parent.right)
            i += 1
    return root


def bfs(root):
    """Algorithm B: Breadth-First Search (queue)."""
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def dfs(node, result=None):
    """Algorithm C: Depth-First Search (pre-order, recursion)."""
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.data)
    dfs(node.left, result)
    dfs(node.right, result)
    return result


def print_tree(root):
    """Print the tree level by level so it matches the diagram."""
    if root is None:
        return
    level = [root]
    n = 0
    while level:
        print(f"level {n}: " + "  ".join(x.data for x in level))
        level = [c for x in level for c in (x.left, x.right) if c]
        n += 1


if __name__ == "__main__":
    root = build_tree(LAST_NAME)
    print("Binary Tree of:", LAST_NAME.upper())
    print_tree(root)
    print("BFS:", " - ".join(bfs(root)))
    print("DFS:", " - ".join(dfs(root)))