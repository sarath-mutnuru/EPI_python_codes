
def get_depth_order_tree(root_node):
	ans = []
	if not root_node:
		return None
	curr_depth_nodes = [root_node]
	while curr_depth_nodes:
		ans.append([node.data for node in curr_depth_nodes])
		c = []
		for node in curr_depth_nodes:
			if node.left:
				c.append(node.left)
			if node.right:
				c.append(node.right)
		curr_depth_nodes = c
	return ans


def get_depth_order_tree_altering(root_node):
	ans = []
	if not root_node:
		return None
	curr_depth_nodes = [root_node]
	o = 1
	while curr_depth_nodes:
		o = o * -1
		ans.append([node.data for node in curr_depth_nodes[::o * -1]])
		c = []
		for node in curr_depth_nodes:
			if node.left:
				c.append(node.left)
			if node.right:
				c.append(node.right)
		curr_depth_nodes = c
	return ans





