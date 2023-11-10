class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length, total, s, startIndex = len(gas), 0, 0, 0
        
        for i in range(length):
            total += gas[i] - cost[i]
            s += gas[i] - cost[i]
            
            if s < 0:  
                s = 0
                startIndex = i + 1
                
        return -1 if (total < 0) else startIndex
                                
            