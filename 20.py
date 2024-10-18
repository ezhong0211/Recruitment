class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        corresponding = {"}": "{", ")": "(", "]": "["}
        running_stack = []
        for char in s:
            if char in corresponding.values():
                running_stack.append(char)
            else:
                if len(running_stack) == 0:
                    return False
                if running_stack[-1] == corresponding[char]:
                    running_stack.pop()
                else:
                    return False
        return len(running_stack) == 0
