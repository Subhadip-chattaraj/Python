class Solution:
    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        stack = []
        ob = ['[', '{', '(']
        cb = [']', '}', ')']
        if x[0] in cb:
            return False
        for i in x:
            if i in ob:
                stack.append(i)
            elif i in cb:
                if len(stack) != 0:
                    n = stack.pop()
                else:
                    return False
                if (i == ']' and n == "[") or (i == '}' and n == '{') or (i == ')' and n == '('):
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True
        return False


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
