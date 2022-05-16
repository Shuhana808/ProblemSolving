from collections import Counter
from collections import defaultdict

# Accepted

MOD = 1000000007


def find_last(n, k, ar):
    counter = Counter()
    end = -1
    ret = defaultdict(int)

    for start in range(n):

        # print(i, ' ', counter)
        # print('ret', ret)
        while len(counter.keys()) <= k and end < n:
            end += 1
            if end < n:
                counter[ar[end]] += 1

            # print(end,counter)

        ret[start] = end
        if counter[ar[start]] == 1:
            del (counter[ar[start]])
        else:
            counter[ar[start]] -= 1
    # print(ret)

    return ret


def count(n, k, ar):
    last = find_last(n, k, ar)
    dp = defaultdict(int)
    prefix = defaultdict(int)
    dp[n] = 1
    prefix[n] = 1
    for i in range(n - 1, -1, -1):
        la = last[i]
        dp[i] = mod(prefix[i + 1] - prefix[la + 1])
        prefix[i] = mod(prefix[i + 1] + dp[i])

        # for j in range(la, i, -1):
        #     dp[i] = mod(dp[i] + dp[j])

    # print(dp)
    return dp[0]


def mod(elem):
    elem %= MOD

    if elem < 0:
        elem += MOD

    return elem


if __name__ == '__main__':
    n_and_k = input().split()

    n_ = int(n_and_k[0])

    k_ = int(n_and_k[1])
    ar_ = list(map(int, input().split()))
    ret = count(n_, k_, ar_)
    print(ret)
