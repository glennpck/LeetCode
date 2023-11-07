class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        citations.sort()
        
        for i in range(l):
            
            if citations[i] >= l - i:
                return l - i
            
        return 0