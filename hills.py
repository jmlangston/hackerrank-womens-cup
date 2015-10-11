def parse_input():
    T = int(raw_input())
    cases = []
    for i in range(1, T + 1):
        dict_name = "dict_" + str(i)
        dict_name = {}
        case = raw_input().split()
        dict_name['N'] = int(case[0])
        dict_name['M'] = int(case[1])
        bridges = []
        for i in range(dict_name['M']):
            bridge = raw_input().strip()
            bridges.append(bridge)
        dict_name['bridges'] = bridges
        cases.append(dict_name)
    # print "T", T
    # print "LIST OF CASES", cases
    return cases

def check_trap(case):
    print "SUCCESS!"

cases = parse_input()
print cases

for case in cases:
    check_trap(case)
