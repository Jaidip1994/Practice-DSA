def findClosestValueInBst(tree, target):
    # Write your code here.
    actual_value = tree.value

    def closest_val(node, target):
        nonlocal actual_value
        if not node:
            return
        if abs(target - actual_value) > abs(target - node.value):
            actual_value = node.value
        if node.value < target:
            closest_val(node.right, target)
        else:
            closest_val(node.left, target)

    closest_val(tree, target)
    return actual_value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
