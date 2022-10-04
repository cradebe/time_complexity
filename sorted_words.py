
# Version 1
def sort_words_sorted(words: list):
    """using built in sorted."""
    #Can also use words.sort()
    #sorted() does not change the integrity of the original list Where as Sort does
    return sorted(words)

# Version 2 O(n)
def sort_words_using_On(words: list):
    """O(n)"""
    sorted_words = []
    while words:
        word = min(words)
        sorted_words.append(word)
        words.pop(words.index(word))
    return sorted_words

# Version 3 O(n2)
def sort_words_using_On2(words: list):
    """O(n2)"""
    for i in range(len(words)):
      for j in range(i + 1, len(words)):
          if words[i] > words[j]:
              temp = words[i]
              words[i] = words[j]
              words[j] = temp
    return words

if __name__ == '__main__':
    words = ['Samkelo', 'Nhlanhla', 'Nhlakanipho', 'Justout', 'Kamogelo', 'Aim']
    print(f'Sort built-in = {sort_words_sorted(words)}')
    print(f'Sort O(n2) = {sort_words_using_On2(words)}')
    print(f'Sort O(n) = {sort_words_using_On(words)}')
