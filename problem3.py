'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"{self.val}"
string = "{0}({1})({2})"

root_str = []
left_str = []
right_str = []
def serialize(root):
    if isinstance(root, Node):
        root_str.append(root.val)
        # print(root.val)
        if isinstance(root.left, Node) and isinstance(root.right, Node):
            left_str.append(root.left.val)
            # print(root.left.val)
            serialize(root.left)
            right_str.append(root.right.val)
            # print(root.right.val)
            serialize(root.right)
    else:
        return f"{root_str}({left_str})({right_str})"
    return f"{root_str}({left_str})({right_str})"
    
if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    # print(node)
    print(serialize(node))