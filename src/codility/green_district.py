
from queue import PriorityQueue
from collections import defaultdict


def solution(A, X, Y):

    total_consumption = sum(A)

    pq = PriorityQueue()

    for item in A:
        pq.put(-item)

    min_cost = float('inf')
    costs = defaultdict(lambda: float('inf'))

    while not pq.empty():
        neg_energy = pq.get()
        if not costs:
            costs[X]= total_consumption + neg_energy
            costs[Y] = total_consumption + neg_energy*2
        else:
            # print(costs)
            for cost in list(costs):
                consumption = costs[cost]
                if consumption > 0:
                    costs[cost+X] = min(costs[cost+X], consumption+neg_energy)
                    costs[cost+Y] = min(costs[cost+Y], consumption+neg_energy*2)
                else:
                    min_cost = min(cost, min_cost)

                costs.pop(cost)

        for key in costs:
            if costs[key] <= 0:
                min_cost = min(key, min_cost)

    return min_cost


res = solution([5, 3, 8, 3, 2], 2, 5)
print(res)
solution([5, 3, 8, 3, 2], 2, 5)
res = solution([4, 2, 7], 4, 100)
print(res)
res = solution([2, 2, 1, 2, 2], 2, 3)
print(res)




