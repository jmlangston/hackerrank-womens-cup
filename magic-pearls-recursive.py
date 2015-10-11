N = int(raw_input().strip())

pearls = raw_input().split()
pearls = [int(x) for x in pearls]

final_sum = 0

def restring_pearls(pearls, final_sum):

    if len(pearls) < 2:
        print final_sum % ((10 ** 9) + 7)

    first_smallest = min(pearls)
    pearls.remove(first_smallest)
    second_smallest = min(pearls)
    pearls.remove(second_smallest)

    sum_smallest = first_smallest + second_smallest
    final_sum += sum_smallest

    pearls.append(sum_smallest)

    restring_pearls(pearls, final_sum)

restring_pearls(pearls, final_sum)

# print final_sum % ((10 ** 9) + 7)