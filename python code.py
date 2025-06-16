class Solution:
    def minCut(self, s: str) -> int:
        
        # Length of the string s
        length = len(s)
      
        # Initialize a 2D list where palindrome[i][j] will be True if the
        # substring s[i:j+1] is a palindrome
        palindrome = [[True] * length for _ in range(length)]
      
        # Fill the palindrome table
        # We start from the end towards the beginning because each cell depends on the next cells
        for start in range(length - 1, -1, -1):
            for end in range(start + 1, length):
                # A substring is a palindrome if its outer characters are equal
                # and the substring excluding the outer characters is a palindrome
                palindrome[start][end] = s[start] == s[end] and palindrome[start + 1][end - 1]
      
        # Initialize a list to store the minimum number of cuts needed for
        # a palindrome partitioning of the substring s[:i+1]
        cuts = list(range(length))
      
        # Calculate the minimum cuts needed for each substring
        for i in range(1, length):
            for j in range(i + 1):
                # If the substring s[j:i+1] is a palindrome
                if palindrome[j][i]:
                    # If j is 0, then s[:i+1] is a palindrome and doesn't need a cut
                    # Otherwise, update the minimum cuts for s[:i+1]
                    cuts[i] = min(cuts[i], 0 if j == 0 else 1 + cuts[j - 1])
      
        # Return the minimum cuts needed for the whole string
        return cuts[-1]
