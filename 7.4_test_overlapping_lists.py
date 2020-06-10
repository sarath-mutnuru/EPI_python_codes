class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


def get_merge_node(head_a, head_b):
    """ check if the linked lists merge and return the merge node """
    dummy_a, dummy_b = ListNode(0, head_a), ListNode(0, head_b)
    n_a, n_b = dummy_a, dummy_b
    len_a, len_b = 0, 0
    while n_a.next:
        n_a = n_a.next
        len_a += 1
    while n_b.next:
        n_b = n_b.next
        len_b += 1

    if n_a != n_b:
        return None

    h_long, h_short = (head_a, head_b) if len_a > len_b else (head_b, head_a)

    for _ in range(abs(len_a - len_b)):
        h_short = h_short.next

    while h_long != h_short:
        h_long, h_short = h_long.next, h_short.next

    return h_long
