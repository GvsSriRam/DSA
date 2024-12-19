class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        position, speed = zip(*sorted(zip(position, speed), reverse = True))
        stack = []

        for i in range(len(position)):
            t = (target - position[i]) / speed[i]
            stack.append(t)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)