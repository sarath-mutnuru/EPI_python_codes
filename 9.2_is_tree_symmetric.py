class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_symmetric(root):
    if not root:
        return False
    if not (root.left and root.right):
        if root.left or root.right:
            return False
        return True
    q_left = [root.left]
    q_right = [root.right]

    while q_left and q_right:

        left_data = [node.data if node != 'null' else 'null' for node in q_left]
        right_data = [node.data if node != 'null' else 'null' for node in q_right]
        if left_data != right_data:
            return False
        q_left = [node for node in q_left if node != 'null']
        q_right = [node for node in q_right if node != 'null']
        l = []
        for node in q_left:
            l.append(node.left if node.left else 'null')
            l.append(node.right if node.right else 'null')
        q_left = l

        r = []
        for node in q_right:
            r.append(node.right if node.right else 'null')
            r.append(node.left if node.left else 'null')
        q_right = r

    return not (q_left or q_right)


def is_symmetric_rec(root):
    def is_mirror(tree1, tree2):
        if not (tree1 or tree2):
            return True
        if tree1 and tree2:
            return tree1.data == tree2.data and is_mirror(tree1.left, tree2.right) and is_mirror(tree1.right, tree2.left)
        return False
          
    return not root or is_mirror(root.left, root.right)


def main():

    t1 = TreeNode(2, None, TreeNode(3))
    t2 = TreeNode(2, TreeNode(3), None)
    t3 = TreeNode(6, None, t1)
    t4 = TreeNode(6, t2, None)
    root = TreeNode(314, t3, t4)

    is_symm = is_symmetric_rec(root)

    print("is_symmetric : {}".format(is_symm))


if __name__ == '__main__':
    main()