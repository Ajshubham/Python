from collections import Counter

def max_score(s):
  char_counts = Counter(s)

  sorted_chars = sorted(char_counts.keys(), key=char_counts.get, reverse=True)
  score = 0
  index = len(s)
  for char in sorted_chars:
    score += index * char_counts[char]
    index -= 1

  return score

string = "bcaa"
max_score_value = max_score(string)
print(f"Maximum score for '{string}': {max_score_value}")
