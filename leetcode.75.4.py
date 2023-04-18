#product of array except self

nums = input('please enter an array of numbers separated by whitespace')
nums = list(map(int, nums.split()))

n = len(nums)
answer = [1] * n

for i in range(n):
    for j in range(n):
        if i != j:
            answer[i] *= nums[j]

print(answer)

