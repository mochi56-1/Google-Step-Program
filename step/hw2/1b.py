random_word = ""

with open("small.txt") as f:
     for line in f:
        random_word += line.strip()

dictionary = []

with open("words.txt") as f:
    for line in f:
        dictionary.append(line.strip())

POINTS = {
    1: "aehinorst",
    2: "cdlmu",
    3: "bfgpvwy",
    4: "jkqxz"
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
        for point, chars in POINTS.items():
            if char in chars:
                score += point

    return score

for random_word in random_words:
    best_word = ""
    best_score = 0

    for word in dictionary:
        if can_make(word, random_word):
            score = get_score(word)

            if score > best_score:
                best_score = score
                best_word = word

    print(random_word, "=>", best_word, best_score)