nums = [1, 2, 3, 4, 5]
gen = (n**2 for n in nums)
print(next(gen))  # 1
print(next(gen))  # 4
print(list(gen))  # [9, 16, 25]


# this solution work only 5 times

# another approach -- infinie

nums = [1]

def generator(nums):
    i = 0
    while True:
        if i >= len(nums):
            nums.append(nums[-1] + 1)  # dodaj następną liczbę
        yield nums[i] ** 2 # zwraca wartosc (co jak return) i pauzuje - ale potem wykona kolejne linijki ( i += 1 ) - po next(gen)
        i += 1

gen = generator(nums)

print(next(gen))  # 1
print(next(gen))  # 4
print(next(gen))  # 9
print(next(gen))  # 16
print(next(gen))  # 25
print(next(gen))  # 25