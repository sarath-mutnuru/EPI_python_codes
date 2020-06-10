class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


def even_odd_merge(head):
    """ link all even numbered nodes followed by odd numbered """
    is_odd = True
    n = head
    h_even, h_odd = None, None
    t_even, t_odd = ListNode(), ListNode()
    while n:
        if is_odd:
            if not h_odd:
                h_odd = n
            else:
                t_odd.next = n
            t_odd = n
        else:
            if not h_even:
                h_even = n
            else:
                t_even.next = n
            t_even = n
        is_odd = not is_odd
        n = n.next

    t_even.next = h_odd
    t_odd.next = None
    return h_even
