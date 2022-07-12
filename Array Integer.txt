/*Q: Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].*/

def solution(A):
    # write your code in Python 3.6
    sorted_array = sorted(A)
    last_val = sorted_array[-1]
    set_A = set(sorted_array)
    set_N = set([i + 1 for i in range(len(sorted_array))])
    missing = set_N - set_A
    if last_val > 0:
        if set_N.issubset(set_A):
            missing = last_val + 1
            return missing
        else:
            return missing.pop()
    else:
        return 1