
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


def get_lowest_common_ancestor(root, node1, node2):

    def get_lca_util(node, n1, n2, ans):
        if not node:
            return []
        l = get_lca_util(node.left, n1, n2, ans)
        r = get_lca_util(node.right, n1, n2, ans)
        desc = [p for p in [node.left] + l + [node.right] + r if p]
        if n1 in desc and n2 in desc and not ans:
            ans.append(node)
        return desc
    ans = []
    _ = get_lca_util(root, node1, node2, ans)
    return ans[0]


def main():
    t_11 = TreeNode(11)
    t_14 = TreeNode(14)

    t1 = TreeNode(1, TreeNode(3, TreeNode(7), TreeNode(8)), TreeNode(4, TreeNode(9), TreeNode(10)))
    t2 = TreeNode(2, TreeNode(5, t_11, TreeNode(12)), TreeNode(6, TreeNode(13), t_14))

    root = TreeNode(0, t1, t2)

    lca = get_lowest_common_ancestor(root, t_11, t_14)
    print("lca of {} and {} is {}".format(t_11.data, t_14.data, lca.data))


if __name__ == '__main__':
    main()