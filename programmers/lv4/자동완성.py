class TrieNode:
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode(None)
    
    def insert(self, word):
        parent = self.root
        
        for char in word:
            if not char in parent.children:
                parent.children[char] = TrieNode(char)
        
            parent = parent.children[char]
            parent.count += 1
            
            
    def search(self, word):
        parent = self.root
        
        for i, char in enumerate(word):
            if parent.count == 1:
                return i
            if char in parent.children:
                parent = parent.children[char]
            else:
                return 0
            
        return len(word)
        
        
def solution(words):
    trie = Trie()
    
    for word in words:
        trie.insert(word)
    
    answer = 0
    for word in words:
        answer += trie.search(word)

    return answer