"""This solution works but needs to be optimized for runtime."""

def extend_magic_string(S):
        
    magic_string = S
    occurrences = S
    
    sum_occur = 0
    i = 0

    while sum_occur < len(magic_string):
        sum_occur += int(occurrences[i])
        i += 1

    next_occur = occurrences[i:]

    if magic_string[-1] == '1':
        next = '2'
    else:
        next = '1'

    to_add = ''

    for digit in next_occur:
        add_me = int(digit) * next
        to_add += add_me
        if next == '2':
            next = '1'
        else:
            next = '2'

    magic_string += to_add
    
    return magic_string


def execute_query(case):
    
    T = int(case[0])
    N = int(case[1])
    
    if T == 1:
        str_subset = S[:N]
        return str_subset.count('1')
        
    else:
        str_subset = S[:N]
        return str_subset.count('2')


Q = int(raw_input().strip())
cases = []

for i in range(Q):
    test_case = raw_input().split()
    cases.append(test_case)

S = '12211212212211211'
    
    
for case in cases:
    N = int(case[1])
    while len(S) < N:
        new_s = extend_magic_string(S)
        S = new_s
    output = execute_query(case)
    print output 
