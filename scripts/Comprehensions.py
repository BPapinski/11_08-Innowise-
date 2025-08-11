nums = [1, 2, 3, 4, 5]
squares = [n**2 for n in nums]
print(squares)  # [1, 4, 9, 16, 25]



even_squares = [n**2 for n in nums if n % 2 == 0]
print(even_squares)  # [4, 16]

unique_lengths = {len(word) for word in ["apple", "banana", "pear", "apple"]}
print(unique_lengths)  # {4, 5, 6}

word_lengths = {word: len(word) for word in ["apple", "banana", "pear"]}
print(word_lengths)  # {'apple': 5, 'banana': 6, 'pear': 4}
