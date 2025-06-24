import sys
from collections import Counter

def main():
    if len(sys.argv) < 2:
        print("Palun anna faili nimi käsurea argumendina.")
        return
    
    file_name = sys.argv[1]

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()

        # Sõnade ja tähemärkide arv
        words = text.split()
        total_words = len(words)
        total_characters = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))  # Ilma tühikuteta

        # Viis kõige sagedamini kasutatud sõna ja tähemärki
        word_counts = Counter(words).most_common(5)
        char_counts = Counter(text).most_common(5)

        print(f"Sõnade koguarv: {total_words}")
        print(f"Tähemärkide koguarv (ilma tühikuteta): {total_characters}")
        print("\nViis enim kasutatud sõna:")
        for word, count in word_counts:
            print(f"{word}: {count}")
        
        print("\nViis enim kasutatud tähemärki:")
        for char, count in char_counts:
            print(f"{char}: {count}")
    
    except FileNotFoundError:
        print(f"Faili {file_name} ei leitud.")

if __name__ == "__main__":
    main()