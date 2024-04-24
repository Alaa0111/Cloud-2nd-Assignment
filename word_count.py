import nltk
from nltk.corpus import stopwords

def analyze_text_file():
    
    # Download stopwords
    nltk.download('stopwords', quiet=True)

    # the path to the text file
    file_path = "/app/random_paragraphs.txt"

    # Read the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # words to lowercase, remove punctuation
    def preprocess_text(text):
        words = text.split()
        for i in range(len(words)):
            words[i] = words[i].strip(".,!?\"'()[]{}:;").lower() # <strip> to convert each word to lowercase
        return words

    words = preprocess_text(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # Count word occurrences
    word_counts = {}
    for word in filtered_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Sort word counts by number of occurrences
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Print word and its count
    print("Words arranged by number of occurrences:")
    for word, count in sorted_word_counts:
        print(f"\t{word}: {count}")

    # Find most frequent word
    most_frequent_word, most_frequent_word_count = sorted_word_counts[0]

    # Print most frequent word
    print("\nMost Frequent Word:")
    print(f"\t'{most_frequent_word}' (appeared {most_frequent_word_count} times)")

    return most_frequent_word, most_frequent_word_count

most_frequent_word, most_frequent_word_count = analyze_text_file()
