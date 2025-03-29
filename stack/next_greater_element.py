"""The next greater element of some element x in an array is the first greater element that is to the
 right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the 
next greater element of nums2[j] in nums2. If there is no next greater element, then the answer
for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]"""


# using stack

def next_greater_element(list):
    res = [-1]*len(list)
    stack = []

    for i in range(len(list)):
        while stack and list[i] > list[stack[-1]]:

            index = stack.pop()
            res[index]= list[i]
        stack.append(i)
        

    return res



print(next_greater_element([4,5,2,10,8]))