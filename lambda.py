square = lambda num: num * num

print(square(2))

add2Num = lambda a, b : a + b

print(add2Num(10,14))
      
# Create functions 

def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)

print(addTen(7))

# Higher order functions

nums = [5, 7, 12,16, 22]

squared_nums = map(lambda num: num * num, nums)

print(list(squared_nums))


# filter

nums = [5, 8, 12, 15]

odd_nums = filter(lambda num: num % 2 != 0, nums)

print(list(odd_nums))

#

from functools import reduce

nums = [1, 3 ,5 ,6 , 8]

total = reduce(lambda tot, cur: tot + cur, nums)

print(total)


total = reduce(lambda tot, cur: tot + cur, nums, 10)

print(total)

print (sum(nums))

################

names = ['aaa bbb', 'aas asd', 'asa aaa']

char_cnt = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_cnt)
