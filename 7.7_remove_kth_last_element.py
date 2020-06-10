class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


def remove_kth_from_last(head, k):
    """ remove kth node from last in linked list """
    ptr1, ptr2 = head, head
    for _ in range(k):
        ptr2 = ptr2.next
    dummy = ListNode(0, head)
    n = dummy
    while ptr2:
        n = ptr1
        ptr1, ptr2 = ptr1.next, ptr2.next
    n.next = ptr1.next
    del ptr1
    return dummy.next
