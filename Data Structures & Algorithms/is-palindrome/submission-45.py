class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we use two pointers to compare
        l, r = 0, len(s) - 1
        while l < r:
            # if the pointer condition holds but the ch is not alphanumeric, move on
            while l < r and not self.isalphanum(s[l]):
                l += 1
            while r > l and not self.isalphanum(s[r]):
                r -= 1
            
            # if both of them aren't the same while lowercase and alphanumeric return false
            if s[l].lower() != s[r].lower():
                return False
            
            # if it satisfies the condition, we move on to the next characters
            l += 1
            r -= 1
        
        # if we complete the pass from left and right, the string is a isPalindrome
        return True

    
# create function to check alphanumeric validity (define it outside the actual function)
    def isalphanum(self,c):
        return(ord("a") <= ord(c) <= ord('z')
        or ord("0") <= ord(c) <= ord('9')
        or ord("A") <= ord(c) <= ord('Z'))
    