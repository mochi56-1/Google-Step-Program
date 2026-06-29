random_words = []

with open("large.txt") as f:
    for line in f:
        random_words.append(line.strip())

dictionary = []

with open("words.txt") as f:
    for line in f:
        dictionary.append(line.strip())

POINTS = {
    "a": 1, "e": 1, "h": 1, "i": 1, "n": 1,
    "o": 1, "r": 1, "s": 1, "t": 1,

    "c": 2, "d": 2, "l": 2, "m": 2, "u": 2,

    "b": 3, "f": 3, "g": 3, "p": 3,
    "v": 3, "w": 3, "y": 3,

    "j": 4, "k": 4, "q": 4, "x": 4, "z": 4
}

def get_char_counts(word):
    char_counts = [0 for _ in range(26)]

    for char in word:
        i = ord(char) - ord('a')
        char_counts[i] += 1

    return char_counts

def can_make(word, random_word):
    word_counts = get_char_counts(word)
    random_counts = get_char_counts(random_word)

    for i in range(26):
        if word_counts[i] > random_counts[i]:
            return False

    return True

def get_score(word):
    score = 0

    for char in word:
        score += POINTS[char]

    return score

total_score = 0

for random_word in random_words:

    best_score = 0
    best_word = ""

    for word in dictionary:

        if can_make(word, random_word):

            score = get_score(word)

            if score > best_score:
                best_score = score
                best_word = word

    total_score += best_score

    print(random_word, "=>", best_word, best_score)

print("合計:", total_score)