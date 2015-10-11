Q = int(raw_input().strip())

cases = []

for i in range(Q):
    test_case = raw_input().split()
    cases.append(test_case)

S = '122112122122112112'

def extend_magic_string(S):
    pass

def execute_query(case):
    T = int(case[0])
    N = int(case[1])

    if len(S) < N:
        extend_magic_string(S)

    if T == 1:
        str_subset = S[:N]
        print str_subset.count('1')

    else:
        str_subset = S[:N]
        print str_subset.count('2')

for case in cases:
    execute_query(case)
