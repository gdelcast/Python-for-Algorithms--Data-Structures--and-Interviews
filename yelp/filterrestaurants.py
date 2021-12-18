from typing import List
import heapq

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
        # O(nlogn) time - sorting
        restaurants.sort(key=lambda x: x[0], reverse=True)
        # print(restaurants)
        
        # O(k) space - filtered restaurants
        hm = {}
        for r in restaurants:
            id, rating, vegan, price, distance = r
            if ((veganFriendly==1 and vegan==1) or veganFriendly==0) and price<=maxPrice and distance<=maxDistance:
                hm[id] = rating
        
        # print(hm)
        # O(n) build heap based in ratings values
        return heapq.nlargest(len(restaurants), hm.keys(), key=hm.get)

restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = 0
maxPrice = 50
maxDistance = 10

s = Solution()
print(s.filterRestaurants(restaurants,veganFriendly, maxPrice, maxDistance))