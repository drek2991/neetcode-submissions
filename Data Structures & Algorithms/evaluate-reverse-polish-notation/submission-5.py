class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = set()
        ops.add('+')
        ops.add('-')
        ops.add('*')
        ops.add('/')
        while len(tokens) > 0:
            val = tokens.pop(0)
            if val not in ops:
                nums.append(int(val))
            else:
                num2 = nums.pop()
                num1 = nums.pop()
                if val == '+':
                    nums.append(num1+num2)
                elif val == '-':
                    nums.append(num1-num2)
                elif val == '*':
                    nums.append(num1*num2)
                else:
                    nums.append(int(num1/num2))
                
        return nums[0]
            






