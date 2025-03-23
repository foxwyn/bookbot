from stats import count_words, count_chars, char_report

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents
  
def main():
  fp = "books/frankenstein.txt"
  book = get_book_text(fp)
  word_ct = count_words(book)
  char_ct = count_chars(book)
  char_ct_ordered = char_report(char_ct)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {fp}...")
  print("----------- Word Count ----------")
  print(f"Found {word_ct} total words")
  print("--------- Character Count -------")
  
  for entry in char_ct_ordered:
    if entry["char"].isalpha():
      print(f"{entry["char"]}: {entry["num"]}")

main()