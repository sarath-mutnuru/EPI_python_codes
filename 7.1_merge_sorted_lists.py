class ListNode(object):
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, nodes = None):
        self.head = None
        for n in nodes:
            self.insert_node(n)

    def insert_node(self, node):
        """ inserts node at the end of the linked list """
        if not self.head:
            self.head = node
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = node
        return

    def print_list(self):
        """ print the data of all nodes in the linked list """
        n = self.head
        while n:
            print(n.data, end=",")
            n = n.next
        return


def merge_lists(head1, head2):
    """ merge the two sorted linked lists and return head """
    t, h = None, None
    l, r = head1, head2
    while l and r:
        if l.data < r.data:
            if t:
                t.next = l
            t, l = l, l.next
        else:
            if t:
                t.next = r
            t, r = r, r.next
        if not h:
            h = t
    if l:
        if t:
            t.next = l
        else:
            t = l

    else:
        if t:
            t.next = r
        else:
            t = r
    if not h:
        h = t

    return h


def merge(head1, head2):
    t = ListNode()
    dummy_head = t
    while head1 and head2:
        if head1.data < head2.data:

            t.next = head1
            head1 = head1.next
            t = t.next
        else:

            t.next = head2
            head2 = head2.next
            t = t.next

    t.next = head1 or head2
    return dummy_head.next


def main():
    linked_list1 = LinkedList(nodes=[ListNode(x) for x in [1, 3, 5, 7, 9]])
    linked_list1.print_list()
    print(end='\n')
    linked_list2 = LinkedList(nodes=[ListNode(x) for x in [2, 4, 6, 8, 10, 12, 14, 16, 18]])
    linked_list2.print_list()
    print(end='\n')
    merged_head = merge(linked_list1.head, linked_list2.head)
    n = merged_head
    while n:
        print(n.data, end = ",")
        n = n.next


if __name__ == '__main__':
    main()
