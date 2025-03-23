def count_words(text):
  words = text.split()
  ct = len(words)
  return ct

def count_chars(text):
  ct = {}

  text_len = len(text)
  i = 0
  while i < text_len:
    c = text[i].lower()

    if c in ct:
      ct[c] += 1
    else:
      ct[c] = 1
    
    i += 1

  return ct


def sort_on(dict):
  return dict["num"]


def char_report(char_ct):
  sorted_chars = []

  for char in char_ct:
    dict_entry = {"char": char, "num": char_ct[char]}
    sorted_chars.append(dict_entry)

  sorted_chars.sort(reverse=True, key=sort_on)
  
  return sorted_chars

