class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        
        trie = [{'best': min(range(len(wordsContainer)), 
                             key=lambda i: len(wordsContainer[i]))}]
        
        for idx, word in enumerate(wordsContainer):
            node = 0
            for ch in reversed(word):
                if ch not in trie[node]:
                    trie.append({'best': idx})
                    trie[node][ch] = len(trie) - 1
                node = trie[node][ch]
                
                cur_best = trie[node]['best']
                if len(word) < len(wordsContainer[cur_best]):
                    trie[node]['best'] = idx

        ans = []
        for word in wordsQuery:
            node = 0
            for ch in reversed(word):
                if ch not in trie[node]:
                    break
                node = trie[node][ch]
            ans.append(trie[node]['best'])

        return ans