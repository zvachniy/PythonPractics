# importt time.time()
# alist = [7, 2, 3, 10, 12]
# blist = [-1, 1, -5, 4, 6]
# print (list(map(lambda x, y: x * y, alist, blist)))
# [x*y for x, y in zip(alist, blist)]

# s_list = [10, 4, 2, -1, 6]
# filter(lambda x: x < 5, s_list)
# print (list(filter(lambda x: x < 5, s_list)))

def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums
sum_of_first_n = sum(firstn(1000000000))
# time_prog=sum_of_first_n.time()

# print (time_prog)
