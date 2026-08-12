class Solution:
    def isValid(self, s: str) -> bool:
        #create the stack
        stack = []
        #define rules for open to close
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            #if the first charcter is in closeToOpen set
            if c in closeToOpen:
                #if they both match the current selection then pop it
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                #otherwise return false
                else:
                    return False
            #if it is an open bracket, append it to the stack
            else:
                stack.append(c)

        #return true if stack is empty, else return false
        return True if not stack else False