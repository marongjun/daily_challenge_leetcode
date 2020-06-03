class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        refund = []
        send_all_to_a = 0

        for i in range(len(costs)):
            send_all_to_a += costs[i][0]
            refund.append(costs[i][1] - costs[i][0])
        refund.sort(reverse = False)

        min_cost = send_all_to_a
        for i in range(len(costs)//2):
            min_cost = min_cost + refund[i]
        return min_cost

answer = Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
print(answer)