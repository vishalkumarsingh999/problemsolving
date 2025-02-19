'''
Inclusion-Exclusion Principle Approach:
For a more intuitive approach, you can use the inclusion-exclusion principle:
For each element in the set, include it in the sum by multiplying it by 2^(𝑛−1),
where 𝑛 is the number of elements in the set.
This is because each element will appear in exactly 2^(𝑛−1) subsets.
'''

def sum_of_all_sub_set(s):
    n=len(s)
    all_sum=sum(i*(2**(n-1)) for i in s)
    return all_sum


if __name__ == '__main__':
    total=sum_of_all_sub_set({1,2,3})
    print(total)