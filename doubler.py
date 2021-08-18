def doubler(arr):
    doubled_arr = []
    for item in arr:
        timesTwo = item * 2
        doubled_arr.append(timesTwo)
    print(doubled_arr)

doubler([2, 5, 6])