# ```
# build a prefix tree that contains all parts of a sting
# -> super duper burger's
#   --> super duper burger's
#   --> duper burger's
#   --> burgers
# ```

class TrieNode:
    def __init__(self):
        self.map = {}
        self.is_word = False
        self.business_names = set()

class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insertBusinessName(self, business_name):
        # Enable case insensitive
        business_name_split = business_name.lower().split(" ")
        split_business_name_length = len(business_name_split)
        for i in reversed(range(split_business_name_length)):
            if i == split_business_name_length-1:
                word = business_name_split[i]
            else:
                word = business_name_split[i] + " " + word
            self.insert(word, business_name)
    def insert(self, word, business_name):
        node = self.trie
        for char in word:
            if char not in node.map:
                node.map[char] = TrieNode()
            node.business_names.add(business_name)
            node = node.map[char]
        node.business_names.add(business_name)
        node.is_word = True


    def searchBusinessName(self, search_term):
        node = self.trie

        # Enable case insensitive
        search_term = search_term.lower()
        for char in search_term:
            if char not in node.map:
                return None
            node = node.map[char]
        return search_term, node.business_names




if __name__ == "__main__":
    trie = Trie()
    
    business_names = ["burger king", "burger queen", "McDonald's", "super duper burger's", "subway", "pizza hut"]

    for business_name in business_names:
        trie.insertBusinessName(business_name)

    search_terms = ["bur", "burger", "burger's", "ger", "sub", "pizza hut", "McD", "mcd"]
    for word in search_terms:
        print(trie.searchBusinessName(word))
