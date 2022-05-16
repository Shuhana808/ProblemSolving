#Problem Code: CHEFK1


def calc_consumption_factor(n, m):

    if m < n-1:
        return -1
    k = m-(n-1)

    rem = k % n
    div = int(k/n)

    if n > 2:
        if rem <= 2:
            return div + 2
        else:
            return div + 3
    elif n == 2:
        if rem == 0:
            return div + 1
        else:
            return div + 2
    else:
        return m


try:

    t = int(input  ())

    for _ in  range(t):
        n_and_m = input().split()

        n = int(n_and_m[0])

        m = int(n_and_m[1])

        ret = calc_consumption_factor(n, m)

        print(ret)

except:
    pass


