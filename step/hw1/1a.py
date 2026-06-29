randome_word =["abdr"]
dictionary = {}

with open("words.txt","r",encoding="utf-8") as f:
    for line in f:
        word=line.strip()
        dictionary[word]=True
        
def better_solution(random_word, dictionary):
    sorted_randome_word = sorted(random_word)

    new_dictionary = {}
    for word in dictionary:
        new_dictionary.append((sorted(word), word))
        sorted(new_dictionary) #リストを一番目の要素でソート

def check(anagram_sub, new_dictionary):
    return anagram_sub in new_dictionary

def anagram(soreted_random_word, new_dictionary):
    for anagram_sub in soreted_random_word:
        if check(anagram_sub,new_dictionary):
            print(anagram_sub)

better_solution(random_word, dictionary)