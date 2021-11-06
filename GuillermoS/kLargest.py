import heapq
class Solution(object):
    def kthlargest(self, arr, k):     # O(klogn) time

        # HEAP MIN
        # heapq.heapify(arr)
        # out = []
        # for i in range(k):
        #     out.append(heapq.heappop(arr))

        #HEAP MAX
        heapq._heapify_max(arr)
        out = []
        for i in range(k):
            out.append(heapq.heappop(arr))
            heapq._heapify_max(arr)


        # ONE LINE SOLUTION HEAP MAX
        #out = heapq.nlargest(k,arr)
        print(out)

    def mostKfrequent(self, arr, k):
        hm = {}
        for n in arr:
            if n not in hm:
                hm[n] = 1
            else:
                hm[n] +=1
        # one line return
        print(heapq.nlargest(k, hm, key=hm.get))
        
        # DOESNT WORK
        # print(hm)
        # heap = []
        # for e in hm.keys():
        #     heapq.heappush(heap,e)
        #     heapq._heapify_max(heap)
        # print(heap)

s = Solution()
#arr = [9,2,1,4,3,6,7,5,10,31,22,66]
arr = [2,2,2,2,1,1,2,3]
k = 2
#s.kthlargest(arr,k)
s.mostKfrequent(arr,k)