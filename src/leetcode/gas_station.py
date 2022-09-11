class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        fuel=0
        index=0
        for i in range(len(gas)):
            fuel+=gas[i]-cost[i]
            if fuel<0:
                index=i+1
                fuel=0
        return index