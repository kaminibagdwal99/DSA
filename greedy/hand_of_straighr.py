"""

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer
 groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.
"""

import heapq


class Solution:
    def isNStraightHand(self, hand, groupSize) :
        if len(hand)%groupSize !=0:
            return False
        map ={}        
        for i in range(len(hand)):
            map[hand[i]]=1+ map.get(hand[i],0)
        print(map)
        minH = list(map.keys())
        print(minH)
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first+groupSize):
                if i  not in map:
                    return False
                map[i]-=1
                if map[i]==0:
                    if i !=minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
            
a = Solution()
print(a.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))