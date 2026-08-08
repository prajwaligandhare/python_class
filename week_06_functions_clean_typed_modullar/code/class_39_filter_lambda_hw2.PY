# 2. filter + lambda se [3,8,1,9,4] mein se sirf 5 se bade rakho.

nums = [3,8,1,9,4]

gretest_num = list(filter(lambda num: num >= 5, nums))

print(gretest_num)