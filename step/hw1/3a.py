random_word = ""
dictionary = []

with open("words.txt") as f:
    for line in f:
        dictionary.append(line.strip())

def better_solution(random_word, dictionary):
    sorted_random_word = sorted(random_word)

    new_dictionary = []

    for word in dictionary:
        new_dictionary.append((sorted(word), word))

    # 1番目の要素 sorted(word) でソート
    new_dictionary.sort(key=lambda x: x[0])

    # 二分探索
    left = 0
    right = len(new_dictionary) - 1

    while left <= right:
        mid = (left + right) // 2

        sorted_word, original_word = new_dictionary[mid]

        if sorted_word == sorted_random_word:
            return original_word
        elif sorted_word < sorted_random_word:
            left = mid + 1
        else:
            right = mid - 1

    return None


answer = better_solution(random_word, dictionary)
print(answer)