class Node:
    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        node = Node(homepage)
        self.head = Node()
        self.tail = Node()
        self.head.next = node
        self.tail.prev = node
        node.prev = self.head
        node.next = self.tail
        self.cur = node

    def visit(self, url: str) -> None:
        new = Node(url)
        new.next = self.tail
        new.prev = self.cur
        self.cur.next = new
        self.cur = new

    def back(self, steps: int) -> str:
        while self.cur.prev.val != "" and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next.val != "" and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)