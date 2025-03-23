def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def count_words(text):
  words = text.split()
  ct = len(words)
  return ct
  
def main():
  book = get_book_text("books/frankenstein.txt")
  word_ct = count_words(book)
  print(f"{word_ct} words found in the document")

main()