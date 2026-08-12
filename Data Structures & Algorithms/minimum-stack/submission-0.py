class MinStack:

    def __init__(self):
        #stores all pushed values
        self.stack = []
        #stores minimum reached so far
        self.minStack = []

    def push(self, val: int) -> None:
        #pushes val to stack
        self.stack.append(val)

        #compute new minumum by comparing current vall to minimum in stack
        val = min(val, self.minStack[-1] if self.minStack else val)
        #if val new minimum, push to minstack
        self.minStack.append(val)

    def pop(self) -> None:
        #pop both stack and minstack so they are lined up
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        #return top of stack
        return self.stack[-1]

    def getMin(self) -> int:
        #return top of minStack which is current minimum
        return self.minStack[-1]
