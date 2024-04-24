import nltk
from nltk.corpus import stopwords

def analyze_text_file():
    
    # Download stopwords (one-time download)
    nltk.download('stopwords', quiet=True)

    # the path to the text file
    file_path = "/app/random_paragraphs.txt"

    # Read the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Preprocess text (lowercase, remove punctuation)
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

    # Print word counts
    print("Word Counts:")
    for word, count in word_counts.items():
        print(f"\t{word}: {count}")

    # Find most frequent word
    most_frequent_word = max(word_counts, key=word_counts.get)
    most_frequent_word_count = word_counts[most_frequent_word]

    # Print most frequent word
    print("\nMost Frequent Word:")
    print(f"\t'{most_frequent_word}' (appeared {most_frequent_word_count} times)")

    return most_frequent_word, most_frequent_word_count

most_frequent_word, most_frequent_word_count = analyze_text_file()
