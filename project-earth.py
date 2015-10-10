args = raw_input().split()
N = int(args[0])
T = int(args[1])

if N % 4 == 0:
    delta = N / 2
elif N % 4 == 1:
    delta = -1
elif N % 4 == 2:
    delta = (N / -2) - 1
else:
    delta = 0

if T + delta < 0:
    print 0
else:
    print int(T + delta)
