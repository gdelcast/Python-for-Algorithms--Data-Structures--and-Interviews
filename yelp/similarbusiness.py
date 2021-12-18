from collections import defaultdict

class Solution:
    def __init__(self):
        self.reviews = defaultdict(set)

    def findMostSimilarBusiness(self,businessOfInterestId, positiveReviews):
        
        # O(n) time O(n) space - iterate array
        for user,business  in positiveReviews:
            self.reviews[business].add(user)
        if businessOfInterestId not in self.reviews: return

        max_similar, max_similar_business = float('-inf'), None

        # O(n) time - O(1) space - iterate hash map to find most similar business
        for business, users in self.reviews.items():
            if business != businessOfInterestId:
                cur_similar = len(users.intersection(self.reviews[businessOfInterestId]))/len(users.union(self.reviews[businessOfInterestId]))
                if cur_similar > max_similar:
                    max_similar = cur_similar
                    max_similar_business = business

        # O(2n) time - O(n) space
        return max_similar_business, max_similar




positive_reviews = [(1,10),(2,10),(1,11),(2,11),(1,12),(2,12),(3,12)]
s = Solution()
print(s.findMostSimilarBusiness(12, positive_reviews))


