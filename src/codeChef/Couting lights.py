# MCO16105


def count_lights(n,m,ar):


try:

    t = int(input  ())

    for _ in  range(t):
        n_and_m = input().split()

        n = int(n_and_m[0])

        m = int(n_and_m[1])
        ar=[]

        for _ in range(n):
            row = [int(s) for s in input()]
            print(row)
            ar.append(row)

        print(ar)


except:
    pass