from collections import Counter
def closeStrings(word1: str, word2: str) -> bool:
    return Counter(word1).values() == Counter(word2).values(), Counter(word1).keys() , Counter(word2).keys()

print(closeStrings('cabbba', 'abbccc'))