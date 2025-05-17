class Solution:
    def setZeroes(self, matrix):
        pair = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    pair.append([i,j])
        
        for p in pair:
            r,c=p
            for i in range(len(matrix[0])):
                matrix[i][c]=0
            for i in range(len(matrix)):
                matrix[r][i]=0
        return matrix
    
    def generate(self, numRows: int):
        rep=[[1]]

        for i in range(numRows-1):
            temp = [0]+ rep[-1]+[0]
            res=[]
            for j in range(len(rep[-1])+1):
                res.append(temp[j]+temp[j+1])
            rep.append(res)
        return rep
    
    def maxProfit(self, prices):
        buy_price=prices[0]
        profit=0
        for i in range(1, len(prices)):
            if buy_price>prices[i]:
                buy_price=prices[i]
            else:
                profit=max(profit, prices[i]-buy_price)
        return profit
    
    def maxSubArray(self, nums):
        total,maxsum =0,0
        for i in nums:
            total= total+ i

            if total <0:
                total=0
            maxsum = max(total, maxsum)
        return maxsum

    def nextPermutation(self, nums):
        n= len(nums)
        i=n-2
        # Find the pivot (first decreasing element from the right):
        while i>=0 and nums[i]>nums[i+1]:
            i=i-1

        if i >=0:
            # Step 2: Find the successor (just larger element to swap):
            j=n-1
            while nums[j]<=nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # Step 3: Reverse the decreasing sequence on the right of i
        nums[i + 1:] = reversed(nums[i + 1:])

        return nums
    
    def sortColors(self, nums):
        l,m,h=0,0,len(nums)-1
        while m<=h:
            if nums[m]==0:
                nums[l], nums[m]= nums[m], nums[l]
                l=l+1
                m = m+1
            elif nums[m]==1:
                m=m+1
            else:
                nums[h], nums[m]= nums[m], nums[h]
                h= h-1
        return nums
    
    def rotate(self, matrix) :
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
        return matrix
    
    def merge(self, intervals):
        start = intervals[0][0]
        end = intervals[0][1]
        res =[]

        for i in range(1, len(intervals)):
            if intervals[i][0]<end:
                end = max(end, intervals[i][1])
            else:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start,end])
        return res
    
    def merge_sorted_array(self,nums1,m,n,nums2):
        nums1.extend(nums2)
        nums1.sort()
        for i in range(n):
            nums1.remove(0)
        return nums1
    
    def findDuplicate(self, nums):
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow1 = 0
        while True:
            slow1 = nums[slow1]
            slow=nums[slow]
            if slow==slow1:
                return slow1
            

    def repeatedNumber(self, nums):

        
        
            
        maxnumber = max(nums)
        set = [i for i in range(maxnumber)+1]
        total =0

        for i in set:
            total = total^i

        for i in nums:
            total = total^i

        return [slow1, total]





a= Solution()
# print(a.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
# print(a.generate(numRows=5))

# print(a.maxProfit(prices = [7,1,5,3,6,4]))

# print(a.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
# print(a.nextPermutation(nums = [1,1,5]))
# print(a.sortColors(nums = [2,0,2,1,1,0]))
# print(a.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
# print(a.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
# print(a.merge_sorted_array(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
# print(a.findDuplicate( nums=[1,3,4,2,2]))
print(a.repeatedNumber(nums=[3, 1, 2, 5, 3] ))
