class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # BFS to build parent graph
        parents = defaultdict(list)
        level = {beginWord}
        visited = set([beginWord])
        found = False
        word_len = len(beginWord)

        while level and not found:
            next_level = set()
            for word in level:
                for i in range(word_len):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet and new_word not in visited:
                            if new_word == endWord:
                                found = True
                            next_level.add(new_word)
                            parents[new_word].append(word)
            visited |= next_level
            level = next_level

        # Backtracking to build all shortest paths
        res = []

        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [p])

        if found:
            backtrack(endWord, [endWord])

        return res
