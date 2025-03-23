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