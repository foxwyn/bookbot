from stats import count_words, count_chars

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents
  
def main():
  book = get_book_text("books/frankenstein.txt")
  word_ct = count_words(book)
  char_ct = count_chars(book)
  print(f"{word_ct} words found in the document")
  print(char_ct)

main()