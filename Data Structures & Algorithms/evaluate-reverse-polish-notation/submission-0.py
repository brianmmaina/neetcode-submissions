class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #make a stack
        stack = []

        #if token found, pop two previos elements and perform token operation
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            #if you find an integer, push it to the stack
            else:
                stack.append(int(c))
            #return first position of the stack which should be the result
        return stack[0]