file = open('puzzle/09.in', 'r')
content = file.read().splitlines()
nums = list(map(int, content))

# part 1
wrong_num = 0
for number in range(25, len(nums)):
    num_diff = set()
    num = set()
    for subnum in range(number-25, number):
        num_diff.add(nums[number] - nums[subnum])
        num.add(nums[subnum])
    if set.intersection(num, num_diff) == set():
        wrong_num = nums[number]
        break
print(wrong_num)

# part 2
start = f_start = num_sum = f_sum = 0
stop = f_stop = 1
while num_sum != wrong_num:
    f_sum = sum(nums[f_start:f_stop])
    num_sum = sum(nums[start:stop])
    if num_sum < wrong_num:
        stop += 1
    elif stop > start:
        stop -= 1
    if (f_sum < wrong_num < num_sum) or (num_sum < wrong_num < f_sum):
        f_start = start = start + 1
        f_stop = stop
print(min(nums[start:stop]) + max(nums[start:stop]))
