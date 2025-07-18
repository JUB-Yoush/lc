"""
use a stack
push new pages onto the stack
pop old pages off and push onto secondary stack
forward history is pages you went came from

"""


class BrowserHistory:
    def __init__(self, homepage: str):
        self.back_history = [homepage]
        self.front_history = []

    # clear front history when visiting new page
    def visit(self, url: str) -> None:
        self.back_history.append(url)
        self.front_history = []

    # pop repeatedly from back, append to front
    def back(self, steps: int) -> str:
        while steps and len(self.back_history) > 1:
            self.front_history.append(self.back_history.pop())
            steps -= 1
        return self.back_history[-1]

    def forward(self, steps: int) -> str:
        while steps and len(self.back_history) > 1:
            self.back_history.append(self.front_history.pop())
            steps -= 1
        return self.back_history[-1]
