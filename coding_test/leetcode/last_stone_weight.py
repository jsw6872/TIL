class Solution:
    def lastStoneWeight(self, stones) -> int:
        while len(stones) > 1:
            stones.sort()
            
            if stones[-1] == stones[-2]:
                stones = stones[:-2]
            elif stones[-1] > stones[-2]:
                weight_gap = stones[-1] - stones[-2]
                stones = stones[:-2]
                stones.append(weight_gap)

        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
        # self.lastStoneWeight(stones)

sol = Solution()
print(sol.lastStoneWeight(stones = [2,7,4,1,8,1]))