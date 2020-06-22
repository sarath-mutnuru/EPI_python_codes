class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        self.s1.append(val)
        return

    def is_empty(self):
        return not(self.s1 or self.s2)

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        if self.s2:
            return self.s2.pop()
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()


def main():
    q = Queue()
    for i in [1,2,3,4]:
        q.enqueue(i)
    v = []
    while not q.is_empty():
        v.append(q.dequeue())

    print(v)


if __name__ == '__main__':
    main()