"""
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.

 

Example 1:

Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
Example 2:

Input: s = "PPALLL"
Output: false
Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
"""

class Solution(object):
    def checkRecord(s):
        """
        :type s: str
        :rtype: bool
        # """
        # final_late, late, absent = 0, 0, s.count("A")
        
        # for i in s:
        #     if i == "L":
        #         late += 1
        #     else:
        #         if late > final_late:
        #             final_late = late
        #         late = 0

        # if late > final_late:
        #     final_late = late

        # if final_late < 3 and absent < 2: return True
        # return False

        Absent, Late = 0, 0
        for c in s:
            if c == 'A':
                Absent += 1
                Late = 0
            elif c == 'L':
                Late += 1
            else:
                Late = 0

            if Absent >= 2 or Late >= 3:
                return False
        return True
        
print(Solution.checkRecord("PPALLP"))
print(Solution.checkRecord("PPALLL"))
print(Solution.checkRecord("LPLPLPLPLPL"))