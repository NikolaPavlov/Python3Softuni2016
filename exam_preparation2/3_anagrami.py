ERROR_MSG = 'INVALID INPUT'
NOANAGRAM_MSG = 'NO ANAGRAMS'


try:
    input_file = input()
    word_for_anagram = input()
except:
    print(ERROR_MSG)


def check_for_anagram(word1, word2):
    word1_list = list(word1)
    word1_list.sort()
    word2_list = list(word2)
    word2_list.sort()
    if word1_list == word2_list:
        return True


anagrams = []
with open(input_file, encoding='utf-8') as f:
    for line in f:
        word_on_the_line = line.strip()
        if word_on_the_line == word_for_anagram:
            continue
        elif check_for_anagram(word_for_anagram, word_on_the_line):
            anagrams.append(word_on_the_line)

if anagrams.__len__() == 0:
    print(NOANAGRAM_MSG)
else:
    anagrams_sorted = sorted(anagrams)
    for word in anagrams_sorted:
        print(word)
