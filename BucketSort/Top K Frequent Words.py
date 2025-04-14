class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_count=Counter(words)
        sorted_words=sorted(word_count,key=lambda word:(-word_count[word],word))
        return sorted_words[:k]
        