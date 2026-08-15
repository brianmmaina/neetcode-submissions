class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # zipping the pair for each car, position and speed
        pair = [(p, s) for p, s in zip(position, speed)]
        #sorting the cars in descending order, closest to the target first
        pair.sort(reverse=True)
        # initialize stack for result
        stack = []

        # iterate through the list
        for p, s in pair:
            #compute the time to target and append it to the stack
            stack.append((target - p)/s)

            #if the new car time is less or equal to the time before it, it catches up and merges with that fleet so we pop it from the stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        #the number of remaining times in the stack is the number of fleets so we return the length of the stack (size)
        return len(stack)


