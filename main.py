def main():
  file = "books/frankenstein.txt"
  with open(file) as f:
    file_contents = f.read()

  print(f"--- Begin report of {file} ---")
  print(f"{number_of_words(file_contents)} words found in the document\n")
  
  char_dict = character_count(file_contents)
  chars = list(char_dict.keys())
  chars.sort()

  for key in chars:
    if key.isalpha():
      print(f"The '{key}' character was found {char_dict[key]} times")
  
  print(f"--- End report  ---")



def number_of_words(text):
  return len(text.split())


def character_count(text):
  char_dict = {}

  for char in text:
    if char.lower() in char_dict:
      char_dict[char.lower()] += 1
      1
    else:
      char_dict[char.lower()] = 1

  return char_dict


if __name__ == "__main__":
  main()
