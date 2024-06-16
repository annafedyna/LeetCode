
def expressiveWords(s: str, words: list[str]) -> int:
    
    count = 0
    
    def count_letters(word):
        dict = []
        count_char = 1
        char = word[0]
        
        for i in range(1,len(word)):
            if word[i] == char:
                count_char += 1
            else:
                dict.append((char, count_char))
                count_char = 1
                char = word[i]
        
        dict.append((char, count_char))
        
        return dict
    
    s_letters = count_letters(s)
    
    for word in words:
        word_letters = count_letters(word)
        
        if all([(s_letters[i][1] >= 3 and s_letters[i][1] >= word_letters[i][1] or (s_letters[i][1] - word_letters[i][1]  == 0)) and s_letters[i][0] == word_letters[i][0] for i in range(len(word_letters))]):
                count += 1
                
    return count
        
print(expressiveWords("dddiiiinnssssssoooo", ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso"]))