class Node:
    def __init__(self):
        self.links = [None, None]

    def contains_key(self, ind):
        return self.links[ind] is not None

    def get(self, ind):
        return self.links[ind]

    def put(self, ind, node):
        self.links[ind] = node

class Trie:
    def __init__(self):
        self.root = Node()
    
    # insert into the trie
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            # bit = num & (1 << i)
            bit = (num >> i) & 1 # checks whether the bit is zero or 1
            if not node.contains_key(bit):
                node.put(bit, Node())
            node = node.get(bit)
    
    # get the maximum number by iterating through the trie
    def get_max(self, num):
        node = self.root
        max_num = 0
        for i in range(31, -1, -1):
            # bit = num & (1 << i)
            bit = (num >> i) & 1
            if node.contains_key(1 - bit):
                max_num = max_num | (1 << i)
                node = node.get(1 - bit)
            else:
                node = node.get(bit)
        return max_num
    
class Solution:
    def findMaximumXOR(self, nums) -> int:
        trie = Trie()
        
        # insert all the elements of the nums array to trie
        for val in nums:
            trie.insert(val)
        
        # calculate the maximum now.
        ans = 0
        for val in nums:
            ans = max(ans, trie.get_max(val))
        
        return ans