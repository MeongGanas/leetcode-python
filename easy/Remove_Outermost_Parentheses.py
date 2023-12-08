"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
"""
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # splt = []
        # temp = s[0]
        # for i in range(1, len(s)):
        #     if temp.count("(") == temp.count(")"):
        #         splt.append(temp)
        #         temp = ''
        #     temp += s[i]
        # if temp.count("(") == temp.count(")"):
        #     splt.append(temp)

        # res = ""
        # for j in splt:
        #     res += j[1:-1]

        # return res

        result = []
        open_count = 0
    
        for char in s:
            if char == '(':
                if open_count != 0:
                    result.append(char)
                open_count += 1
            else:
                open_count -= 1
                if open_count != 0:
                    result.append(char)
        
        return ''.join(result)

solution = Solution()
print(solution.removeOuterParentheses("(()())(())"))
print(solution.removeOuterParentheses("(()())(())(()(()))"))