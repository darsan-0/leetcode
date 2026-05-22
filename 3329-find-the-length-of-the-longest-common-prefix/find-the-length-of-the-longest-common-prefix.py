class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        # Use a HashSet for O(1) constant time lookups
        prefixes = set()
    
        # Step 1: Extract and store every possible prefix from arr1
        for num in arr1:
            s = str(num)  # Convert number to string to work with individual digits
            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])  # Add sliced prefix (e.g., "1", "10", "100")
                
        max_len = 0
        
        # Step 2: Check prefixes of numbers in arr2 against the stored set
        for num in arr2:
            s = str(num)  # Convert number to string
            for i in range(1, len(s) + 1):
                # If the current prefix exists in our set, check if it's the longest seen so far
                if s[:i] in prefixes:
                    max_len = max(max_len, i)
                
        return max_len
