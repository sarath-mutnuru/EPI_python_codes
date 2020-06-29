class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_sum(root):

    def get_sum_util(node):
        if not(node.left or node.right):
            return [(node.data, 1), ]
        left_arr = [] if not node.left else get_sum_util(node.left)
        right_arr = [] if not node.right else get_sum_util(node.right)
        arr = left_arr + right_arr
        ans = [(num + (p_2*2)*node.data, p_2*2) for (num, p_2) in arr]
        return ans
    res = get_sum_util(root)
    return sum([r[0] for r in res])


def main():
    t1 = TreeNode(1, TreeNode(0), TreeNode(1))
    t2 = TreeNode(1, None, TreeNode(1, TreeNode(0), None))
    t3 = TreeNode(0, TreeNode(1), None)
    root = TreeNode(1, t1, TreeNode(1, t2, t3))

    ans = get_sum(root)
    print(ans)


if __name__ == '__main__':
    main()


