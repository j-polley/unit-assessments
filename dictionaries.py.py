from collections import Counter

def count_word_frequencies(file_name):
    """Read a file and count the frequency of each word."""
    word_counts = Counter()

    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Normalize words to lowercase and remove punctuation
                words = line.strip().lower().split()
                normalized_words = [word.strip(".,!?;:\"'()") for word in words]
                word_counts.update(normalized_words)

    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
        return None

    return word_counts

def print_top_words(word_counts, n=5):
    """Print the top n most common words and their frequencies."""
    if word_counts:
        print(f"Top {n} most common words:")
        for word, count in word_counts.most_common(n):
            print(f"{word}: {count}")

def main():
    """Main function to execute the word frequency analysis."""
    input_file = "textfile.txt"

    # Create a sample text file for testing
    with open(input_file, 'w') as file:
        file.write("This is a test. This test is only a test. If this were a real emergency, real information would follow. This is just a test.")

    # Count word frequencies
    word_counts = count_word_frequencies(input_file)

    # Print the top 5 most common words
    print_top_words(word_counts, n=5)

if __name__ == "__main__":
    main()
