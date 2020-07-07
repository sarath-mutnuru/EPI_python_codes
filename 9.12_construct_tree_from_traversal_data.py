class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def make_tree(pre_order_vec, in_order_vec):
    if not len(pre_order_vec):
        return None
    root = TreeNode(pre_order_vec[0])

    def make_tree_util(node, preo, ino):
        if not node or not len(preo) or not len(ino):
            return
        L = len(preo)
        p_idx = {val: i for i, val in enumerate(preo)}
        i_idx = {val: i for i, val in enumerate(ino)}
        p_idx_node = p_idx[node.data]
        i_idx_node = i_idx[node.data]

        num_nodes_left = i_idx_node
        num_nodes_right = L - i_idx_node - 1

        if num_nodes_left:
            node.left = TreeNode(preo[p_idx_node+1])
            make_tree_util(node.left, preo[p_idx_node+1 : p_idx_node + num_nodes_left+1], ino[0:i_idx_node])
        if num_nodes_right:
            node.right = TreeNode(preo[p_idx_node+num_nodes_left+1])
            make_tree_util(node.right, preo[p_idx_node+num_nodes_left+1:], ino[i_idx_node+1:])

    make_tree_util(root, pre_order_vec, in_order_vec)

    return root


def pre_order(node):
    vec = []

    def pre_order_util(node):
        if node:
            vec.append(node.data)
            pre_order_util(node.left)
            pre_order_util(node.right)
    pre_order_util(node)
    return vec


def in_order(node):
    vec = []

    def in_order_util(node):
        if node:
            in_order_util(node.left)
            vec.append(node.data)
            in_order_util(node.right)
    in_order_util(node)
    return vec


def main():

    preo = [1, 2, 3] #[3, 9, 20, 15, 7]
    ino = [3, 2, 1] #[9, 3, 15, 20, 7]

    root = make_tree(preo, ino)
    p = pre_order(root)
    i = in_order(root)

    print("pre order : {}, in order :{}".format(p, i))


if __name__ == '__main__':
    main()