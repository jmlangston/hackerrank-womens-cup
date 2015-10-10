N = int(raw_input().strip())

pearls = raw_input().split()
pearls = [int(x) for x in pearls]

pearls.sort()
# pearls.reverse()

final_sum = 0

# print "INITIAL LIST", pearls

while len(pearls) > 1:
    sum_pearls = pearls[0] + pearls[1]    # sum of two smallest pearls
    final_sum += sum_pearls                 # add this sum to running total
    pearls[1] = sum_pearls                 # update one of the pearls
    del pearls[0]                            # pop the other pearl
    pearls.sort()
    # print pearls

print final_sum % ((10 ** 9) + 7)
