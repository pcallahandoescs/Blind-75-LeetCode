#contains duplicate

nums = input('enter an integer array separated by spaces')
nums = list(map(int, nums.split()))

duplicate_found = False

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            duplicate_found = True
            break
    if duplicate_found:
        break

if duplicate_found:
    print('true')
else:
    print('false')