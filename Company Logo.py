# A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition.
# Given a string, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
  # Print the three most common characters along with their occurrence count.
  # Sort in descending order of occurrence count.
  # If the occurrence count is the same, sort the characters in alphabetical order.

    s = input()
    cnt = Counter(s)
    sorted_items = sorted(cnt.items(), key=lambda item: (-item[1], item[0]))
    i = 0
    for key, value in sorted_items:
        i += 1
        print(f"{key} {value}")
        if i == 3:
            break
