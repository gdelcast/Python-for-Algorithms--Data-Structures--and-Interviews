# do not use hash map extra space and do it O(n) time
# 1<= a[i] <= n

class Solution(object):
    def findduplicates(self, nums):

        out = []

        for n in nums:
            value = abs(n)
            print(nums[value])
            
            if nums[value]<0:
                out.append(abs(n))
            else:
                nums[value] = nums[value] *-1
            print(nums)

        print( out)


s = Solution()
s.findduplicates([2,4,5,3,1,4,5,7,9,0])