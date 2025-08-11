nums = [1, 2, 3]
it = iter(nums)      # get iterator
print(next(it))      # 1
print(next(it))      # 2
print(next(it))      # 3
# next(it) would raise StopIteration


class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

for num in Counter(1, 5):
    print(num)  # 1 2 3 4 5
