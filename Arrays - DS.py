# An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index, (where ), that can be referenced as orray.
# Reverse an array of integers.
# Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.
# Example
# Return
# Function Description
# Complete the function reverseArray in the editor below.
# rseArray has the following parameter(s):
#     int A[n]: the array to reverse
# Returns
#     int[n]: the reversed array
# Input Format
# The first line contains an integer, the number of integers in .
# The second line contains space-separated integers that make up .

def reverseArray(a):
    rev_a = []
    for x in range(len(a)):
        s = a.pop()
        rev_a.append(s)
    return rev_a
