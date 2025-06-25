import sys
from collections import Counter

def read_file(file_name):
    
    # Loeb faili sisu ja tagastab selle tekstina
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Faili {file_name} ei leitud.")
        sys.exit(1)

def count_words_and_characters(text):
    
    # Arvutab sõnade ja mitte-tühikutest tähemärkide koguarvu
    words = text.split()
    non_space_characters = len(text.replace(" ", ""))
    return len(words), non_space_characters

def get_most_common(elements, n=5):
    
    # Tagastab kõige sagedamini esinevad elemendid koos esinemiste arvuga
    return Counter(elements).most_common(n)

def display_results(total_words, total_characters, word_counts, char_counts):
    
    # Kuvab analüüsi tulemused
    print(f"Sõnade koguarv: {total_words}")
    print(f"Tähemärkide koguarv: {total_characters}")
    print("\nViis enim kasutatud sõna:")
    for word, count in word_counts:
        print(f"{word}: {count}")
    print("\nViis enim kasutatud tähemärki:")
    for char, count in char_counts:
        print(f"{char}: {count}")

def main():
    if len(sys.argv) < 2:
        print("Palun anna faili.")
        return

    file_name = sys.argv[1]
    text = read_file(file_name)
    
    total_words, total_characters = count_words_and_characters(text)
    word_counts = get_most_common(text.split())
    char_counts = get_most_common(text.replace(" ", ""))

    display_results(total_words, total_characters, word_counts, char_counts)

if __name__ == "__main__":
    main()
