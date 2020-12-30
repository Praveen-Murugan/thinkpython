"""
Write a function that takes a list of numbers and returns the cumulative sum; that
is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For
example, the cumulative sum of [1, 2, 3] is [1, 3, 6].

"""

def cumulative_sum(num_list):
    sum_list = []
    next_num = 0

    for num in num_list:
        num += next_num
        sum_list.append(num)
        next_num = num

    return sum_list
l = [1, 10, 15]
print(cumulative_sum(l))
