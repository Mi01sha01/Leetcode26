class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Record the last occurrence index of each character
        last_index = {char: i for i, char in enumerate(s)}
        
        result = []
        size = 0
        end = 0
        
        for i, char in enumerate(s):
            end = max(end, last_index[char])
            size += 1
            
            # If the current index reaches the maximum end boundary, a partition is complete
            if i == end:
                result.append(size)
                size = 0  # Reset size for the next partition
                
        return result