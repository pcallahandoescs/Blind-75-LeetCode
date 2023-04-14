#1. Two sum

nums = input('please enter an array of integers separated by spaces: ')
nums = list(map(int, nums.split()))

target = int(input('please enter a target integer: '))

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
        else:
            pass


