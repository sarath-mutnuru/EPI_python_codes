class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, items = None):
        self.head = None
        for item in items:
            self.insert_node(ListNode(item, None))

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
        print("\n")
        return


def reverse(head, s, f):
    """ reverse the linked list from sth node to fth node both inclusive - 1 indexed list """
    count = 0
    n = head
    if s>f:
        return
    prev_start, start, end, post_end = [None, ]*4
    while n:
        count += 1
        if count == s - 1:
            prev_start, start = n, n.next
        if count == f:
            end, post_end = n, n.next
        n = n.next
    prev, t = post_end, start
    while t != post_end:
        temp = t.next
        t.next = prev
        prev = t
        t = temp
    prev_start.next = end


def is_palindrome(head):
    len_list = 0
    n = head
    while n:
        len_list += 1
        n = n.next
    s = len_list - len_list//2 + 1
    f = len_list
    reverse(head, s, f)
    ptr1, ptr2 = head, head
    for _ in range(s-1):
        ptr2 = ptr2.next
    while ptr2:
        if ptr1.data != ptr2.data:
            return False
        ptr1, ptr2 = ptr1.next, ptr2.next
    return True


def main():
    linked_list = LinkedList(items=[1])
    len_list = 0
    n = linked_list.head

    while n:
        len_list += 1
        n = n.next
    s = len_list - len_list//2 + 1
    f = len_list
    linked_list.print_list()
    print("---------reversing sec half ------------")
    reverse(linked_list.head, s, f)
    linked_list.print_list()
    print("---------reversing sec half again------------")
    reverse(linked_list.head, s, f)
    linked_list.print_list()

    ispalindrome = is_palindrome(linked_list.head)
    linked_list.print_list()
    print(ispalindrome)


if __name__ == '__main__':
    main()

