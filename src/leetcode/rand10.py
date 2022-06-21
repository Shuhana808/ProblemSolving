
from collections import defaultdict

def droppedRequests(requestTime):
    # Write your code here

    time = {}
    dropped = 0
    n = len(requestTime)
    highest_time = requestTime[n - 1]
    summation = [0]*highest_time
    for i in range(0, len(requestTime)):
        t = requestTime[i]

        if t not in time.keys():
            time[t] = 1

        else:
            time[t] = time[t]+1

        summation

        #
        # if time[t] > 3:
        #     dropped=dropped +1
        # elif:




    print(time)

droppedRequests([1,1,1,1,2,3,3,4,5])



