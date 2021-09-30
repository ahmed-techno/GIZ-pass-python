

class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        longest_str  = ''  
        for i in range(len(s)): 
            for j in range(len(s), i, -1):  
                if len(longest_str) >= j-i:   
                    break
                elif s[i:j] == s[i:j][::-1]:
                    longest_str = s[i:j]
                    break
        return longest_str
