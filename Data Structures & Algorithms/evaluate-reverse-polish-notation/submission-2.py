class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        while len(tokens) > 0:
            val = tokens.pop(0)
            if val.isdigit():
                nums.append(int(val))
            else:
                if len(nums) < 2:
                    print("Error")
                    return -69
                num2 = nums.pop()
                num1 = nums.pop()
                if val == '+':
                    nums.append(num1+num2)
                elif val == '-':
                    nums.append(num1-num2)
                elif val == '*':
                    nums.append(num1*num2)
                else: #//
                    nums.append(num1//num2)
        return nums[0]
            


#         ["4","13","5","/","+"] = 6


# nums = []
# ops = [4, 13, 5, /, +]

# #search for operator
# nums = [4, 13, 5]
# ops = [/, +]

# remove 1 op, remove 2 ints









