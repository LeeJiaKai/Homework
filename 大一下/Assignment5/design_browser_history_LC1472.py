class Node:
    def __init__(self, data):
        self.data = data  # 节点数据
        self.next = None  # 指向下一个节点
        self.prev = None  # 指向前一个节点

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = Node(homepage)

    def visit(self, url: str) -> None:
        new_page = Node(url)
        self.cur.next = new_page
        new_page.prev = self.cur
        self.cur = new_page

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.prev is None:
                break
            self.cur = self.cur.prev
        return self.cur.data

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.next is None:
                break
            self.cur = self.cur.next
        return self.cur.data


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)