first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [x.__len__() for x in first_strings if x.__len__() > 4]
second_result = [(x, y) for x in first_strings for y in second_strings if x.__len__() == y.__len__() ]
third_result = {x : x.__len__() for x in first_strings + second_strings if not x.__len__() % 2}

print(first_result)
print(second_result)
print(third_result)
