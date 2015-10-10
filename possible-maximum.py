import itertools

T = int(raw_input())

test_cases_list = []

for i in range(T):
    test_case = raw_input().split()
    test_cases_list.append(tuple(test_case))
    
def our_function(test_case):
    N = int(test_case[0])
    K = int(test_case[1])
    
    s = set(xrange(1, N + 1))
    
    combos = itertools.combinations(s, 2)
    
    maximum = 0
    
    for i in combos:
        bit_and = i[0] & i[1]
        if maximum < bit_and < K:
            maximum = bit_and
    
    return maximum
  
for test_case in test_cases_list:
    output = our_function(test_case)
    print output
    