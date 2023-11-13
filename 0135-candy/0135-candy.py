class Solution:
    def candy(self, ratings: List[int]) -> int:
        length, candy = len(ratings), [1]*len(ratings)
        for i in range(length-1):
            if ratings[i] < ratings[i+1]:
                candy[i+1] = max(1 + candy[i], candy[i+1]) 
        for i in range(length-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                candy[i] = max(1 + candy[i+1], candy[i])
        return sum(candy)