random_word = ""
dictionary = []

with open("words.txt") as f:
    for line in f:
        dictionary.append(line.strip())

def better_solution(random_word, dictionary):
  sorted_random_word = sorted(random_word)

  answers = []

  for word in dictionary:
        if sorted(word) == sorted_random_word:
            answers.append(word)

  return answers


answer = better_solution(random_word, dictionary)
print(answer)

