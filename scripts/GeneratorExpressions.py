nums = [1, 2, 3, 4, 5]
gen = (n**2 for n in nums)
print(next(gen))  # 1
print(next(gen))  # 4
print(list(gen))  # [9, 16, 25]
