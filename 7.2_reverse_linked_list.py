class ListNode:
    def __init__(self, data = 0, next = None):
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self, nodes):
        self.head = None
        for node in nodes:
            self.insert_node(node)

    def insert_node(self, node):
        if not self.head:
            self.head = node
            return
        n = self.head
        while n.next:
            n = n.next
        n.next = node
        return

    def print_list(self):
        n = self.head
        while n:
            print(n.data, end=',')
            n = n.next
        return


def reverse(head, s, f):
    """ reverse linked list from sth node to fth node with 1-idxed, both inclusive """
    n = head
    count = 0
    start, end = None, None
    while n:
        count += 1
        if count == s-1:
            prev_start, start = n, n.next
        if count == f:
            end, post_end = n, n.next
        n = n.next
    t = post_end
    n = start
    while n != post_end:
        temp = n.next
        n.next = t
        t = n
        n = temp
    prev_start.next = end
    return


def main():
    linked_list = LinkedList([ListNode(x) for x in [1,2,3,4,5,6,7,8,9]])
    linked_list.print_list()
    print("\n#########---reversing---########")
    reverse(linked_list.head, 2, 5)
    linked_list.print_list()


if __name__ == '__main__':
    main()


